// One-time, syntax-aware migration of existing static UI text to UiText.
// Never rewrites course data, API calls, navigation, events, or form state.
const fs = require("node:fs");
const path = require("node:path");
const ts = require("../apps/web/node_modules/typescript");
const root = path.resolve(__dirname, "..");
const targets = [
  "components/auth-forms.tsx",
  "components/contact-form.tsx",
  "components/logout-button.tsx",
  "components/account-nav.tsx",
  "components/account-forms.tsx",
  "components/ui/feedback.tsx",
  "components/ui/field.tsx",
  "components/catalog/curriculum.tsx",
  "components/catalog/enroll-cta.tsx",
  "components/learning/lesson-actions.tsx",
  "components/learning/lesson-body.tsx",
  "components/learning/player-curriculum.tsx",
  "components/learning/curriculum-drawer.tsx",
  "components/learning/sync-status.tsx",
  "components/learning/video-player.tsx",
];
function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (entry.name.endsWith(".tsx"))
      targets.push(path.relative(path.join(root, "apps/web/src"), file));
  }
}
for (const group of ["(auth)", "(learner)", "(player)"])
  walk(path.join(root, "apps/web/src/app", group));
const strings = new Set();
for (const target of targets) {
  const file = path.join(root, "apps/web/src", target);
  let source = fs.readFileSync(file, "utf8");
  const tree = ts.createSourceFile(
    file,
    source,
    ts.ScriptTarget.Latest,
    true,
    ts.ScriptKind.TSX,
  );
  const edits = [];
  function visit(node) {
    if (ts.isJsxText(node)) {
      const raw = source.slice(node.pos, node.end);
      const value = raw.replace(/\s+/g, " ").trim();
      if (/[À-ỹ]/.test(value)) {
        strings.add(value);
        edits.push({
          start: node.pos,
          end: node.end,
          text: "<UiText value=" + JSON.stringify(value) + " />",
        });
      }
    }
    ts.forEachChild(node, visit);
  }
  visit(tree);
  if (!edits.length) continue;
  for (const edit of edits.reverse())
    source = source.slice(0, edit.start) + edit.text + source.slice(edit.end);
  if (!source.includes("import { UiText }")) {
    const declaration =
      'import { UiText } from "@/components/language-provider";\n';
    source = source.startsWith('"use client";')
      ? source.replace('"use client";', '"use client";\n' + declaration)
      : declaration + source;
  }
  fs.writeFileSync(file, source);
}
console.log(JSON.stringify([...strings], null, 2));
