# RAPO Feature Template

## Feature Name
Provide the short name of the feature.

## Objective
Describe the purpose of the feature and the problem it solves.

## Files to Create
- List any new module or support files.

## Files to Modify
- List any existing files that need updates.

## Function Signatures
```python
def scan(target: str) -> dict:
    """Describe the function behavior."""
```

## UI Changes
- Describe any Rich panels, tables, or report sections to add or update.

## Acceptance Criteria
- The feature works with a hostname or URL.
- The feature handles errors gracefully.
- The CLI output remains usable and professional.
- Existing RAPO behavior is not broken.

## Testing Checklist
- [ ] Imports verify successfully.
- [ ] Python files compile.
- [ ] CLI runs with example.com.
- [ ] Output is readable and uses Rich formatting.
- [ ] No unrelated files were changed.
