"""Verify teaching examples in disposable directories; never touch course data."""
from pathlib import Path
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / 'content' / 'recording-kit'
sys.dont_write_bytecode = True


class RecordingKitChecks(unittest.TestCase):
    def run_example(self, lesson, inputs='', filename='solution.py', folder=None):
        def execute(directory):
            target = Path(directory) / filename
            shutil.copyfile(KIT / 'python-path' / f'{lesson:02}' / filename, target)
            result = subprocess.run(
                [sys.executable, '-B', str(target)], input=inputs,
                text=True, encoding='utf-8', capture_output=True, timeout=5,
                cwd=directory, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            return result.stdout
        if folder:
            return execute(folder)
        with tempfile.TemporaryDirectory() as directory:
            return execute(directory)

    def test_packs_and_local_links(self):
        for n in range(1, 11):
            folder = KIT / 'python-path' / f'{n:02}'
            for name in ('TEACHER.md', 'STUDENT.md', 'starter.py', 'solution.py'):
                self.assertTrue((folder / name).is_file(), f'{folder}/{name}')
        for path in KIT.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((path.parent / link.split('#')[0]).exists(), f'{path}: {link}')

    def test_all_code_parses_and_starters_run(self):
        for path in KIT.rglob('*.py'):
            ast.parse(path.read_text(encoding='utf-8'))
        for n in range(1, 11):
            with self.subTest(lesson=n):
                inputs = {2: 'BanA\n', 3: 'print\n', 9: 'q\n', 10: 'q\n'}.get(n, '')
                self.run_example(n, inputs, 'starter.py')

    def test_first_program_and_input(self):
        self.assertEqual(len(self.run_example(1).splitlines()), 3)
        self.assertIn('BanA muon chia se Mat Biec', self.run_example(2, 'BanA\nMat Biec\n'))

    def test_quiz_branches(self):
        self.assertIn('Dung roi!', self.run_example(3, ' PRINT \n'))
        self.assertIn('Chua dung.', self.run_example(3, 'loop\n'))
        self.assertIn('chua nhap', self.run_example(3, '\n'))

    def test_lists_and_status(self):
        self.assertIn('So cuon sach: 3', self.run_example(4))
        for n in (5, 7):
            output = self.run_example(n)
            self.assertIn('1 De Men Phieu Luu Ky con trong', output)
            self.assertIn('2 The Little Prince dang muon', output)

    def test_function_search(self):
        namespace = {'__name__': 'teaching_check'}
        # Avoid executing the demonstration prints while testing the function.
        source = (KIT / 'python-path/06/solution.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        functions = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)], type_ignores=[])
        exec(compile(functions, '<lesson06>', 'exec'), namespace)
        find = namespace['find_titles']
        titles = ['De Men', 'Little Prince', 'Mat Biec']
        self.assertEqual(find(titles, ' MAT '), ['Mat Biec'])
        self.assertEqual(find(titles, 'missing'), [])
        self.assertEqual(find(titles, ''), titles)

    def test_menu_errors_and_state_changes(self):
        for n in (8, 9, 10):
            with self.subTest(lesson=n):
                output = self.run_example(n, 'b\nabc\nb\n99\nb\n1\nb\n1\nf\nDe Men\nr\n1\nf\nDe Men\nq\n')
                self.assertIn('Use a whole-number book ID.', output)
                self.assertIn('Unknown book, or its status already matches.', output)
                self.assertIn('No available books match.', output)
                self.assertIn('1 De Men Phieu Luu Ky', output)

    def test_storage_survives_restart(self):
        for n in (9, 10):
            with self.subTest(lesson=n), tempfile.TemporaryDirectory() as directory:
                self.run_example(n, 'b\n1\nq\n', folder=directory)
                data = json.loads((Path(directory) / 'books.json').read_text(encoding='utf-8'))
                self.assertTrue(data[0]['borrowed'])
                self.assertIn('No available books match.', self.run_example(n, 'f\nDe Men\nq\n', folder=directory))
                self.run_example(n, 'r\n1\nq\n', folder=directory)
                self.assertIn('1 De Men Phieu Luu Ky', self.run_example(n, 'f\nDe Men\nq\n', folder=directory))

    def test_corrupt_file_preserved(self):
        for n in (9, 10):
            for invalid in ('{broken', '{}', '[{"id": 1}]'):
                with self.subTest(lesson=n, invalid=invalid), tempfile.TemporaryDirectory() as directory:
                    path = Path(directory) / 'books.json'
                    path.write_text(invalid, encoding='utf-8')
                    self.assertIn('Could not read books.json:', self.run_example(n, folder=directory))
                    self.assertEqual(path.read_text(encoding='utf-8'), invalid)

    def test_final_rejects_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            book = {'id': 1, 'title': 'Example', 'borrowed': False}
            path = Path(directory) / 'books.json'
            original = json.dumps([book, book])
            path.write_text(original, encoding='utf-8')
            self.assertIn('duplicate', self.run_example(10, folder=directory))
            self.assertEqual(path.read_text(encoding='utf-8'), original)


if __name__ == '__main__':
    unittest.main(verbosity=2)
