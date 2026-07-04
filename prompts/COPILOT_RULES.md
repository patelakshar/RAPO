# RAPO Copilot Rules

## Mission
RAPO is a lightweight reconnaissance and penetration testing assistant. The goal is to provide clean, modular, and professional tooling that helps users gather security-relevant information from targets quickly and reliably.

## Project Goals
- Keep the project simple, maintainable, and extensible.
- Preserve a consistent CLI experience.
- Favor clear module boundaries over unnecessary abstraction.
- Deliver polished Rich-based terminal output.
- Ensure all new features are verifiable and production-safe.

## Folder Structure
- src/rapo/core/: CLI entrypoints, router orchestration, output rendering.
- src/rapo/tools/: independent scanners and recon modules.
- src/rapo/config/: configuration and environment handling.
- src/rapo/models/: data models and schemas.
- src/rapo/reporting/: reporting support.
- src/rapo/utils/: shared helper utilities.

## Coding Standards
- Write clean, readable Python.
- Use type hints for function signatures.
- Add docstrings to public functions and modules.
- Prefer small, focused functions over large monolithic ones.
- Keep naming consistent and descriptive.
- Follow the existing RAPO style and avoid introducing unrelated patterns.

## Module Interface Rules
- Each tool module should expose a function named scan(target: str) -> dict unless a different interface is explicitly required.
- Return dictionaries with predictable keys and values.
- Avoid side effects outside the module's responsibility.
- Keep modules self-contained and reusable.
- Do not alter unrelated modules unless required for integration.

## Error Handling Standards
- Handle all exceptions gracefully.
- Return safe fallback structures rather than crashing.
- Use meaningful defaults such as empty lists and zero/false values.
- Avoid broad silent failures without a clear fallback.

## Router Integration Rules
- Any new scanner must be imported into the router.
- The router should execute the scanner and include its result in the returned payload.
- Preserve existing router behavior and avoid breaking current modules.
- Keep the router minimal and orchestration-focused.

## Rich UI Conventions
- Use Rich Console, Panel, and Table for terminal output.
- Keep the interface professional and readable.
- Render a clear banner and structured sections.
- Show meaningful values; if data is missing, display N/A or Not Found as appropriate.
- Do not print raw JSON to the terminal.

## Performance Guidelines
- Prefer lightweight requests and timeout handling.
- Respect network timeouts and avoid unnecessary retries.
- Keep parsing logic efficient and deterministic.
- Avoid expensive operations in the main scan path when they are not needed.

## Testing Requirements
- Verify imports after adding modules.
- Compile changed Python files.
- Run the CLI entrypoint with a known target such as example.com.
- Confirm new functionality does not break existing behavior.

## Git Workflow
- Make focused changes scoped to the task.
- Do not modify unrelated files.
- Review the diff before finishing.
- Ensure the working tree is in a clean and intentional state before committing.

## Things That Must Never Be Done
- Do not introduce unnecessary architecture.
- Do not duplicate logic already implemented elsewhere.
- Do not modify unrelated modules without justification.
- Do not print raw JSON where a Rich report is expected.
- Do not break existing CLI behavior.
- Do not leave modules with missing imports, syntax issues, or unhandled exceptions.
