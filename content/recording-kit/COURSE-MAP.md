# CodingBuddy curriculum map

Private editorial plan · proposed course structure · not a public availability claim

## The first learning paths

| Course | Starting knowledge | Finish with | Recording plan | Current preparation |
|---|---|---|---|---|
| Python: những chương trình hữu ích đầu tiên / Your first useful programs | Run a file; onboarding provided | Small interactive programs and a search function | PY01–PY06 | Six lesson packs with speaking notes, tasks and code |
| Python: tủ sách chia sẻ của lớp mình / Classroom book exchange | Python foundation course or equivalent | Local book tracker with search, loans and JSON storage | BK01–BK04 | Four lesson packs with speaking notes, tasks and code |
| Web: trang đầu tiên của bạn / Your first website | Comfortable creating and opening files | A readable, responsive resource page | WB01–WB04 | Lesson briefs below; full scripts still to write |
| Web: hướng dẫn kỹ năng số dễ hiểu / A useful digital guide | Web foundation course or equivalent | A guide revised after another person tries it | DG01–DG03 | Existing written example plus briefs below |
| Python: đọc nhật ký lãng phí thực phẩm / Understanding a food-waste log | Python lists, loops, functions, dictionaries | CSV analysis with an evidence-based conclusion | DT01–DT04 | Existing written example and dataset plus briefs below |

These are two foundation courses and three applied courses. Release the first two together once complete. The remaining eleven recordings are a later batch, not a prerequisite for starting to record now.

## Teaching decisions

- Teach at a beginner pace without assuming all 10–15-year-olds have the same experience. Offer one optional stretch task per lesson; do not require it to progress.
- Vietnamese narration first, English lesson summaries and edited English captions. Code identifiers stay consistent across languages.
- Start with the useful result, teach the smallest missing concept, then ask the learner to make a change.
- Students need computer access for coding. A phone can play the videos but is not the assumed coding setup.
- Focus on Python's standard library and plain HTML/CSS. Accounts, hosting, external APIs, JavaScript frameworks and AI services are unnecessary for these first projects.
- “Meaningful” means a clearly identified person or problem and an attempt to test usefulness. A sample project is not evidence of community impact.

## Next batch: web foundations

### WB01 · Give a page structure

**Outcome:** open a local HTML file with a heading, introduction and ordered instructions.

**Demo:** create a school-library guide; explain doctype, html/lang, head/title and body, then h1, p and ol/li. View in a browser after saving. Distinguish the browser tab title from the visible heading.

**Task:** replace the example with a guide to a school club or classroom resource. **Check:** page has one clear main heading and steps in an intentional order. **Mistake to show:** editing without saving, then refreshing and seeing stale content. **Assets to prepare:** blank index.html and a completed semantic page. **Target:** 6–9 minutes.

### WB02 · Links, images and useful navigation

**Outcome:** navigate to a section and explain an image with alternative text.

**Demo:** add internal links to section IDs and one locally stored illustration. Explain relative paths and meaningful link text.

**Task:** add two sections and a contents list; use an original screenshot with no private information, or omit the image. **Check:** links land at the intended headings and a missing image still has useful text. **Mistake:** mismatched filename or section ID. **Assets:** one original diagram, local image folder, broken-path example. **Target:** 6–9 minutes.

### WB03 · Make the page readable

**Outcome:** apply a reusable CSS rule and explain how spacing helps readers.

**Demo:** connect style.css; set text size, line-height, max-width, padding and link/focus styling. Compare an overly wide paragraph with a readable column.

**Task:** choose a restrained palette and improve the same page. **Check:** body text and links are legible, focus remains visible, headings have a clear order. **Mistake:** CSS filename does not match the linked href. **Assets:** before/after CSS. **Target:** 7–10 minutes.

### WB04 · Make it work on a small screen

**Outcome:** fix a layout that overflows and review keyboard use.

**Demo:** viewport metadata, flexible width, max-width:100% on images, a simple media query only where needed. Resize the browser and tab through links.

**Task:** test at narrow and wide widths and fix one real issue. **Check:** no horizontal scrolling in the example, readable text, reachable links. **Mistake:** fixed-width container wider than the viewport. **Assets:** two test widths and a completion checklist. **Target:** 7–10 minutes.

## Applied web course: a digital guide

### DG01 · Choose one task and one reader

**Outcome:** a four-step guide someone could follow. **Demo:** use the current suspicious-link guide as an example, explaining its limited scope. Ask what the reader is trying to do and which terms need explaining. **Task:** write one audience sentence, one goal and four action-led steps. **Check:** no vague instruction such as “be careful” without a concrete action. **Recording asset:** a rough draft and its revised version. **Target:** 5–8 minutes.

If using the suspicious-link example, keep its existing qualifications: HTTPS alone does not establish trust, and students should not visit suspicious links to test the lesson. Alternatively choose a task you can demonstrate directly, such as organizing files. Verify any software-specific steps against the version shown in the recording.

### DG02 · Turn the draft into a page

**Outcome:** a functioning guide built from the student's text. **Demo:** organize the steps with semantic HTML, style examples and keep phone readability. **Task:** build a guide using the web foundation techniques. **Check:** heading order, links, text and illustrations support the task. **Recording asset:** current `digital-skills-guide.html` as a reference, not as code to claim a student wrote. **Target:** 8–12 minutes.

### DG03 · Observe and revise

**Outcome:** one documented improvement based on a real reader's difficulty. **Demo:** prepare a task for the reader, observe without coaching, then compare before/after wording. If no reader is available yet, label your own test as a rehearsal. **Task:** ask someone to use the page and revise one step. **Check:** note the observation, change and result. **Recording asset:** anonymous test sheet; no testimonial required. **Target:** 5–8 minutes.

## Applied data course: food waste

### DT01 · Read a small table

**Outcome:** explain rows, columns, units and the question being asked. **Demo:** open the existing six-row sample CSV; read it with csv.DictReader and show that grams starts as text. **Task:** print day/item/grams and convert one value to a number. **Check:** distinguish string concatenation from addition. **Assets:** sample CSV and a reader starter. **Target:** 6–9 minutes.

### DT02 · Validate and total

**Outcome:** group valid measurements by day and count rejected rows. **Demo:** walk through the existing read_totals function with one row at a time; introduce float, dictionary accumulation and invalid values. **Task:** add a malformed row to a copy and confirm it is reported as skipped. **Check:** baseline totals Monday 200 g, Tuesday 150 g, Wednesday 230 g, overall 580 g; average per recorded day about 193.3 g. **Assets:** original and deliberately invalid CSVs. **Target:** 8–12 minutes.

### DT03 · Make a comparison visible

**Outcome:** show the daily totals as a clearly labeled chart. **Demo:** create a simple text bar chart using a fixed scale, such as one # for 10 g; print exact totals beside the bars. **Task:** render the three daily totals consistently. **Check:** labels and units, equal scale, no overstated precision. **Assets:** a chart exercise and solution still to author. The current download does not yet include this chart. **Target:** 5–8 minutes.

### DT04 · Say what the data supports

**Outcome:** separate observation, uncertainty and a next question. **Demo:** “Wednesday has the highest total in this sample” versus an unsupported claim about causes. Discuss meal counts, missing days and portion sizes. **Task:** write one observation, one limitation and one question to investigate. Optional personal data collection needs a consistent method and permission where appropriate; it is not needed to complete the course. **Check:** clearly label the dataset as invented and avoid claiming an intervention worked. **Assets:** conclusion worksheet and rubric. **Target:** 5–8 minutes.

## Content beyond videos

Each course needs: a plain-language overview, prerequisites, real outcomes, lesson notes, starter downloads, exercises, hints, explained solutions, a final task and a help route. Add these before selling the completed experience. Do not promise mentoring hours, a certificate, response times or lifetime access until you decide what you can actually provide.

For a preview, use one genuine complete lesson rather than an advertisement. Keep lesson availability truthful. Student project galleries can come later when real submissions and permission exist.
