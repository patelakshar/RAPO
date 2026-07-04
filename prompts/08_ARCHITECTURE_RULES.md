# RAPO Architecture Rules

## Architecture Overview

RAPO follows a layered architecture:

CLI

↓

Router

↓

Modules

↓

Reporting

↓

Rich Output

## Responsibilities

### CLI

The CLI layer provides the user-facing entrypoint and initiates the scan workflow.

### Router

The router coordinates the execution of the available modules and collects their results into a single structured payload.

### Modules

Each module performs a focused reconnaissance task and returns structured data.

### Reporting

The reporting layer prepares findings and results for presentation.

### Rich Output

The Rich output layer formats the final report in a readable, terminal-native way.

## Dependency Direction

Dependencies should flow downward in the architecture. The CLI may call the router, the router may call modules, and modules should not depend on higher layers.

## Stability Rules

The architecture should remain stable because it provides clarity and consistency. Avoid unnecessary refactoring or layer changes unless the benefit is substantial and well justified.
