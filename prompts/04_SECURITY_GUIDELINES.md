# RAPO Security Guidelines

## Safe Defaults

RAPO should default to passive and non-destructive operations. The project should favor reconnaissance and data collection over active interference.

## Passive Reconnaissance First

Prefer passive methods such as DNS lookups, HTTP metadata collection, and header inspection before any more intrusive activity.

## No Destructive Functionality

RAPO must not include destructive behavior by default. Any future offensive capabilities should be clearly separated and require explicit user action.

## Input Validation

All inputs should be validated before use. Target values should be treated carefully, and malformed inputs should be handled gracefully.

## Network Timeout Rules

All network operations should use explicit timeouts. Long waits and hanging requests should be avoided.

## Exception Handling

Network failures, parsing errors, and unexpected data should be handled safely. The tool should degrade gracefully rather than crash.

## Logging

Logs should be concise and useful. Avoid exposing sensitive data or unnecessary verbosity.

## Responsible Disclosure Principles

Any security findings produced by RAPO should be discussed with the same care and professionalism expected in responsible disclosure practices.

## Future Offensive Modules

Any future modules that perform active or potentially intrusive actions must require explicit user authorization and should be clearly documented as such.
