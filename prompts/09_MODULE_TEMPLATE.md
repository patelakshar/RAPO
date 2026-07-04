# RAPO Module Template

## Preferred Function Signatures

Use one of the following patterns where appropriate:

```python
def scan(target: str) -> dict:
    """Perform a reconnaissance scan for the target."""
```

or

```python
def analyze(target: str) -> dict:
    """Analyze the target and return structured findings."""
```

## Standard Imports

Use standard library modules and existing RAPO imports where appropriate. Keep imports concise and relevant.

## Standard Error Handling

- Validate input.
- Use timeouts for network activity.
- Catch expected exceptions.
- Return a safe fallback dictionary rather than crashing.

## Return Format

Return a dictionary with clearly named keys and predictable values. Use empty lists and neutral defaults for missing data.

## Naming Conventions

- Use descriptive, lowercase module names.
- Use clear function names that reflect the module's purpose.
- Keep identifiers readable and consistent.

## File Naming

Use file names that reflect the module purpose, such as dns.py, http.py, robots.py, or sitemap.py.

## Documentation Style

Document the module purpose, function behavior, and return values. Keep documentation concise and useful.
