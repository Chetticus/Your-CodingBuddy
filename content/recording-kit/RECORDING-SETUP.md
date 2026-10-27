# Recording setup

## A simple first setup

Use your existing computer and microphone/headset. Webcam is optional. Spend the first session checking that your voice and code are clear; do not buy equipment before hearing a test.

If you need recording software, use the [official OBS download](https://obsproject.com/download). OBS documents its Auto-Configuration Wizard, window/display capture, microphone selection and test recordings in the [official quick-start guide](https://obsproject.com/kb/quick-start-guide). Run the wizard for recording, select your editor window as a source, verify the microphone meter, and review a short test before a full take. These are setup instructions; OBS has not been installed or configured for you.

Our starting recording choices: 1920×1080, 30 fps if your computer handles that smoothly; editor text around 22–26 px; a plain high-contrast theme; terminal below the code. Adjust after viewing the test at phone size. Keep one program and its output visible. Hide the file explorer when it makes the code too small.

Record code and voice together. An optional short face-camera introduction is enough. Music is unnecessary during explanations. Turn off notification popups and close private tabs. Use the invented example data provided here.

## Your repeatable session

### Before recording

- [ ] Read `TEACHER.md` and run `solution.py` yourself.
- [ ] Open `starter.py`; save a working copy as `my-work.py` in that same lesson folder. Type into the copy.
- [ ] Keep the original starter and solution intact for the next take.
- [ ] For lessons 09–10, use a disposable working folder. If an earlier take created `books.json`, move that test file aside before a fresh take; never reset a learner's real file.
- [ ] Close messages and private windows; check microphone selection and recording area.
- [ ] Record and listen to 60 seconds: voice audible, no clipping, code readable, correct window captured.

### During recording

- Show the result first, then return to the starter.
- Say what you expect before pressing Run.
- Type one logical change at a time and explain why it exists.
- Leave a few seconds for students to pause at the exercise.
- When demonstrating a bug, explicitly call it a deliberate example. Show how you read the error and verify the fix.
- If you stumble, pause and repeat the sentence. Note the time for editing; avoid restarting the whole lesson.
- Teach the reference solution after the pause prompt, or make that portion a separate optional walkthrough.

### After recording

- [ ] Watch the beginning, all code transitions and the ending; spot-check the rest.
- [ ] Run the exact saved code from the recording, not only the reference file.
- [ ] Check that spoken explanations match visible output.
- [ ] Edit pauses or retakes that obstruct learning; leave useful reasoning in.
- [ ] Generate and proofread Vietnamese captions, then translate and proofread English captions.
- [ ] Check code identifiers in subtitles: `input`, `False`, `return`, `books.json`.
- [ ] Measure the real duration; update the tracker.
- [ ] Save a second copy of the raw recording before deleting or replacing anything.

## Naming and storage

Create your recording folders outside the repository, for example under Videos/CodingBuddy: `raw`, `edited`, `captions`, `covers`. Do not put large videos or personal recordings into Git.

Names: `CB-PY01-vi-take01`, `CB-PY01-vi-final`, `CB-PY01.vi.vtt`, `CB-PY01.en.vtt`. Use BK01–BK04 for the project lessons. Keep original recordings until the reviewed release is safely backed up.

## Recording order

Session A: one pilot take of PY01. Review it before batching.

Session B: PY02–PY04, with breaks and an output check between takes.

Session C: PY05–PY06. Make sure you can explain list versus dictionary and print versus return without reading.

Session D: BK01–BK02. Split BK02 into search and loan handling if it runs long.

Session E: BK03–BK04. Rehearse file persistence and the damaged-file example in a disposable folder.

Session F: beginner pilot and targeted corrections. This is an order of work, not a promise that all lessons can be finished in six days.
