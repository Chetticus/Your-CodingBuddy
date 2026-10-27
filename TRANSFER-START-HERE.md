# Continue CodingBuddy on another device

This repository contains the website source, original Git history, all ten recording packs (scripts, instructor directions, starter/solution files), 19 written lessons, downloadable examples, original demo video, fonts, illustrations, design files, screenshots, and early HTML prototypes.

The teaching videos still need recording. The included `apps/api/assets/demo/sample.mp4` is demo media, not a recording by Nam.

## Install and run

Install Git, Node.js 24 LTS, and the pnpm version specified in `package.json` (11.24.0). Python 3 is needed for the lesson examples and their checks.

```sh
git clone https://github.com/Chetticus/Your-CodingBuddy.git
cd Your-CodingBuddy
pnpm install --frozen-lockfile
node scripts/setup-local-review.mjs
pnpm --filter api build
```

Start the isolated local database in a separate terminal and leave it running:

```sh
node scripts/review-db.mjs
```

Then initialize demo accounts/catalog and the authored courses:

```sh
pnpm --filter api seed
pnpm --filter api exec tsx prisma/seed-project-courses.ts
pnpm --filter web exec next build --webpack
```

Run these in two separate terminals:

```sh
pnpm --filter api start:prod
```

```sh
pnpm --filter web start
```

Open http://localhost:5000. Demo learner: `student1@elearning.local` / `Demo!Student123`. Demo administrator: `admin@elearning.local` / `Demo!Admin123`. These are public development fixtures only. Do not expose the demo environment publicly.

The setup script creates fresh local secrets without overwriting existing environment files. Local database state (including review progress and sessions) is regenerated from seeds, not transferred. No production database is included or required. Dependencies, caches, build outputs, local mail containing login tokens, and private environment files are intentionally excluded.

## Where everything lives

- `content/recording-kit/START-HERE.md`: all ten videos and recording workflow.
- `content/recording-kit/python-path/`: narration, instructor actions, starter and solution files.
- `content/project-lessons/`: all 19 written lessons.
- `apps/web/public/downloads/`: student downloads.
- `apps/web/src/content/`: course metadata, direct-contact enrollment configuration, and charity placeholders.
- `design/redesign/CONTENT-REVIEW.md`: current content inventory and verification.
- `design/redesign/prototypes/`: early interactive design proposals.
- `design/`: design source files and screenshots.
- `transfer/authoring-tools/`: historical scripts used to prepare materials; reference only. Some contain old machine-specific paths and can overwrite later editorial changes. Edit canonical lesson files directly.

All changes are for review. The Community page still contains labeled placeholders, contact/QR details still need Nam's real details, and recording is pending. Pushing this repository does not deploy the website. Chat conversation history is not stored by Git; project decisions and handoff notes are in the documents above.

## Additional transfer archive

`transfer/local-storage/` preserves the 35 local lesson-resource and cover files, including inherited demo assets. The normal seed recreates working references on the new device; this archive is a backup, not a database restore. `transfer/agent-context/` preserves the local agent guidance as reference documents.
