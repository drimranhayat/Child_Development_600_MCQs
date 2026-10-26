# Growing Minds — Child Development

Complete website for eight Child Development lectures. `index.html` is in the repository root. No build tools, dependencies or API keys are required.

## Update your GitHub repository

1. Extract this ZIP.
2. Copy the CONTENTS of `Child_Development_Full_Repo` into your existing `child-development` repository folder. Replace matching files. Keep your existing `.git` folder.
3. Verify that index.html, style.css, app.js, data.json and assets/ are directly in the repository root, not inside a nested folder.
4. Commit and push with GitHub Desktop.
5. Under Settings → Pages, choose Deploy from a branch, select main and / (root), and save. If your default branch differs, select that branch.
6. Wait for deployment, then refresh using Ctrl + F5.

No GitHub Actions workflow is required. The previous dist/ directory is unused with this layout.

## Local preview

Run `python -m http.server 8000` here and open http://localhost:8000 . An HTTP server is required because the site uses fetch to load JSON.

## Contents

Eight lectures; 66 topics with examples and timelines; 600 exam-focused MCQs with explanations (75 per lecture); 66 recall prompts; 404 source slide sections with available embedded pictures; assignments and supporting resources. Includes search, bookmarks, browser-local progress, missed-answer review, shuffled options, 10/20/50/100 question pagination, responsive layout and dark mode.

## Maintenance

Edit build_content.py and run `python build_content.py` to regenerate data.json. Original extracted text is in source-material/slides.json. Check JavaScript using `node --check app.js`, then run `python validate_repo.py`. The build also refreshes the per-lecture JSON exports and COVERAGE.md.

## Source fidelity

The Source slides view preserves original wording, including dated estimates and spelling errors. Curated notes clarify selected misleading claims. Original attribution appears in the footer. Available pictures from seven decks are included. Native shape diagrams and original slide layouts are not reproduced. Lecture 6 text was recovered from a legacy file, but its picture layout was unavailable. Original PowerPoint binaries are not included.

Milestones are approximate guides, not individual diagnoses. Source material retains its original attribution; this package grants no rights to third-party course material. No credentials, Git history or account-specific hosting configuration is included.


## Exam study tools

Use Syllabus coverage to find every topic and its mapped questions. Practice offers lecture, topic and question-type filters; one-at-a-time or 10/20/50/100-question views; a question jump menu; and Previous/Next question controls. Clicking any option immediately reveals the correct answer and explanation. The first choice stays recorded until Retry is selected. Review mistakes and Not attempted collect stable question sets so answers remain visible during review. Mixed 50 draws at least six questions from each lecture.

All 600 MCQs are exported in question-bank/600-mcqs.json, with eight lecture-specific JSON files. The authored expansion is maintained in the lecture-01.txt through lecture-08.txt files. Existing question IDs are preserved so prior browser progress can survive this update.

Validation checks counts, distinct stems, options, answer indexes, coverage mappings, exports and image references. It does not prove that a question bank predicts every exam item. Review original slide illustrations and lecturer guidance alongside the bank.

An optional .github/workflows/pages.yml is included and publishes the repository ROOT. If you retained the old workflow, replace it with this one so it no longer publishes the old dist/ content. Branch publishing works with main / (root); alternatively select GitHub Actions and use the included workflow.
