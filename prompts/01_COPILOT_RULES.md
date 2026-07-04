# GitHub Copilot Engineering Rules

## Python Standards

- Write readable, production-quality Python.
- Favor clarity over cleverness.
- Keep functions focused and modest in size.
- Follow the existing RAPO style rather than introducing unrelated conventions.

## Type Hints

- Use type hints for function parameters and return values.
- Prefer concrete types where possible.
- Keep signatures explicit and understandable.

## Docstrings

- Add docstrings to public functions and modules.
- Document purpose, arguments, behavior, and return values.
- Keep documentation concise and useful.

## Imports

- Keep imports clean and relevant.
- Avoid unused imports.
- Prefer standard library and existing internal modules over introducing new dependencies without justification.

## Error Handling

- Handle exceptions gracefully.
- Return safe fallback values instead of crashing.
- Avoid broad exception handling without a clear recovery path.
- Ensure network and parsing failures degrade cleanly.

## Logging

- Use logging only when it meaningfully improves observability.
- Avoid excessive or noisy logs in CLI output.
- Keep logging consistent and low-risk.

## Router Integration

- If a new scanner is added, update the router.
- Preserve the current router contract and output structure.
- Keep the router orchestration-focused and minimal.

## Output Integration

- If a new scanner changes user-facing results, update the output renderer.
- Continue using Rich-based presentation rather than dumping raw JSON.
- Ensure new output remains consistent with the existing UI conventions.

## Rich UI Rules

- Use Rich Console, Panel, and Table for terminal output.
- Maintain a consistent banner, color palette, and icon usage.
- Make output readable and polished.
- Avoid cluttered or inconsistent layouts.

## Performance Considerations

- Respect request timeouts.
- Avoid unnecessary network work.
- Keep parsing logic efficient.
- Avoid adding expensive operations to the main scan path without need.

## Testing Requirements

- Verify imports.
- Compile changed Python files.
- Run the CLI against a known target such as example.com.
- Check that the new feature does not break existing behavior.

## Code Quality Requirements

- Keep implementations maintainable.
- Reuse existing code where practical.
- Avoid duplicate logic.
- Preserve backwards compatibility whenever possible.

## Things Copilot Must Never Do

- Never redesign the architecture without necessity.
- Never introduce unnecessary abstraction.
- Never duplicate logic that already exists.
- Never modify unrelated source files without a clear reason.
- Never print raw JSON when a structured Rich report is expected.
- Never break existing CLI behavior.
- Never ship code with syntax issues or unresolved imports.
