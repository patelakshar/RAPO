# RAPO Review Checklist

Use this checklist before every commit.

## Code Quality
- [ ] Code compiles without errors.
- [ ] Type hints are present where appropriate.
- [ ] Docstrings are added for public functions.
- [ ] No duplicate logic was introduced.
- [ ] Existing RAPO style is followed.

## Integration
- [ ] Router updated if a new scanner or feature was added.
- [ ] Output rendering updated when user-facing results changed.
- [ ] Imports resolve correctly.
- [ ] No unrelated modules were modified.

## UX and Reporting
- [ ] Rich output remains professional and readable.
- [ ] Missing values are handled clearly.
- [ ] No raw JSON is printed where a Rich report is expected.
- [ ] The CLI still behaves as intended.

## Verification
- [ ] Tested with example.com.
- [ ] CLI runs successfully.
- [ ] No obvious regressions were introduced.

## Git Hygiene
- [ ] Git status reviewed.
- [ ] Only intended files are changed.
- [ ] Commit message is clear and specific.
