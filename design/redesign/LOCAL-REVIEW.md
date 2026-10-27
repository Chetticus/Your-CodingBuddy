# Local review

The redesigned app is for local review only. Nothing has been pushed, uploaded, or deployed.

## Open

http://localhost:5000

Latest content revision (27 October): five complete written courses, 19 lessons, and a new bilingual Community page with labeled placeholder reports and illustrations. See [content review](CONTENT-REVIEW.md) for course links and replacement instructions. All ten video scripts are also prepared locally.

Paid enrollment now uses direct contact: try http://localhost:5000/checkout/phan-tich-du-lieu-voi-python-va-pandas without signing in. The QR/contact area is deliberately pending until the owner supplies real details. See DIRECT-ENROLLMENT.md for configuration and the manual access workflow.

Review the homepage, Learning path, open practice lesson, Our story, contact, login, and registration pages. Use VI/EN in the header. The practice library has working search, topic filters, notes, exercises, and two offline source downloads.

## Sample account

The isolated review database uses the repository's demo accounts. The learner below has the original course access plus all three newly authored project courses. For learner review:

- Email: student1@elearning.local
- Password: Demo!Student123

These are documented local demo credentials, not credentials for the live website. Existing demo courses and their media are sample content, not Hải Nam's upcoming recordings. No real payment or email provider is connected.

## Restart after the review processes have stopped

From the repository root, use three terminals:

```powershell
node scripts/review-db.mjs
```

```powershell
pnpm --filter api start:prod
```

```powershell
pnpm --filter web start
```

The API needs the existing ignored apps/api/.env created for this local review, and the web app uses apps/web/.env.local. They point only to localhost. The generated signing secret is deliberately not recorded here. The database lives under the ignored .local-review/ directory and listens only on 127.0.0.1:55435.

After source changes, rebuild the API if needed and rebuild the frontend before using the production-style start command. Use pnpm --filter web dev during iteration. Do not run a frontend build against the same .next directory while its dev server is active.

```powershell
node scripts/build-workshop-downloads.cjs
pnpm --filter api build
pnpm --filter web build
```

## Review limits and next content decisions

- The visual direction and copy are a first implementation for feedback.
- The open practice is an authored written exercise. The tutor's planned video series still needs to be recorded.
- Existing course titles, prose, video/audio, and legal documents retain their original language; English interface copy does not imply translated media.
- Some inherited staff and operational text is still Vietnamese.
- The final course offering, tutor portrait if wanted, access/fees, and verified community-impact material need review before deployment.
- Authentication, enrollments, progress, downloads, and payments use the existing contracts. Local demo content is not production data.

## Change summary

Latest revision: exact dark Maker’s Notebook palette, coral code logo and cream ribbon; course-first homepage; restored search, category/level/price filters and sorting; three practical project courses, nine written lessons and four downloadable source files. Existing account, paid checkout, instructor and progress contracts are preserved.

The new project courses are local review content. After the database is running, refresh them without touching production using:

```powershell
pnpm --filter api exec tsx prisma/seed-project-courses.ts
python scripts/check-project-examples.py
```

The seed refuses connections outside the isolated 127.0.0.1:55435/template1 review database. It grants the demo learner access and preserves lesson progress. Other signed-in readers can open all written project lessons as previews; the existing enrollment requirement still controls progress tracking. Free project courses never enter the paid checkout flow.

New CodingBuddy identity, a self-hosted Vietnamese-capable font system, responsive public layouts, persistent language preference, a working open practice project, redesigned course summaries/detail presentation, tutor and contact pages, account-screen styling, and translated core interface copy. Canonical PRODUCT.md and DESIGN.md now describe the student's teaching studio rather than the previous adult marketplace.

## Verification

Latest course-site revision: all 191 frontend tests still pass. Four independent Python tests validate the actual downloadable examples: search and loan transitions, JSON persistence and duplicate validation, expected CSV totals, invalid/missing data. Browser verification covered the seven-course catalog, accent-insensitive Vietnamese search, sorting with preserved search, English course summaries, mobile filter expansion and the free-course filter. The new book-sharing course saved its first lesson as complete, advanced to lesson two, and showed 1/3 progress. Its attached source file downloaded through the existing signed resource endpoint. The revised catalog has no horizontal overflow at the tested 360px phone viewport in either language. All six checked main palette foreground/background pairs exceed 4.5:1 contrast.

The optimized frontend build, including TypeScript, passes. All 191 frontend tests across 19 files pass. Browser checks covered the practice search and filters, language switching, login/logout using the local demo account, enrolled dashboard, course detail, preview modal, lesson access, and mobile navigation. The phone homepage had no horizontal overflow. The course route now renders per request for language preference while keeping the catalog data cache.

The first review still includes inherited Vietnamese labels in portions of the lesson player and staff interfaces. Course prose and sample video assets are original demo material, awaiting replacement with the actual teaching content.
