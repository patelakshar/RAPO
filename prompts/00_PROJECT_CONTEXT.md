# RAPO Project Context

## Project Vision

RAPO is a modular reconnaissance and penetration testing assistant designed to provide a professional, extensible, and maintainable terminal-based workflow for security assessment tasks.

The project is intentionally structured to remain useful for both educational and professional use cases while preserving a clear and disciplined engineering approach.

## Mission

RAPO exists to help users gather security-relevant information efficiently and responsibly. The project focuses on passive reconnaissance, structured reporting, and professional presentation through a Rich terminal interface.

## Goals

- Provide a reliable reconnaissance workflow.
- Keep the codebase simple, modular, and readable.
- Support future offensive security capabilities in a controlled and explicit way.
- Deliver polished CLI output with strong reporting conventions.
- Encourage safe, responsible, and maintainable engineering practices.

## Current Progress

RAPO already includes a number of reconnaissance-oriented modules covering:

- DNS enumeration
- HTTP probing
- Port scanning
- WHOIS lookups
- Technology detection
- SSL analysis
- Security header analysis
- robots.txt scanning
- sitemap.xml scanning

## Current Modules

The project is organized around the following areas:

- Core: CLI entrypoint, router, reporting, and output presentation
- Tools: specialized reconnaissance scanners and analyzers
- Config: settings and environment configuration
- Models: data structures and domain models
- Reporting: structured output preparation
- Utils: shared helper utilities

## Folder Structure

```text
src/
  rapo/
    core/
    tools/
    config/
    models/
    reporting/
    utils/
```

## Current Architecture

The current architecture follows a simple pipeline:

CLI

↓

Router

↓

Modules

↓

Reporting

↓

Rich Output

This architecture is intentionally stable and should remain easy to understand. Each scanner performs a focused task and returns structured data to the router.

## Development Roadmap

The roadmap for RAPO includes:

- Expanding passive reconnaissance coverage
- Adding richer reporting and evidence capture
- Improving module reuse and standardization
- Strengthening output presentation and readability
- Supporting more advanced, explicitly authorized offensive workflows in the future

## Long-Term Vision

RAPO is expected to grow into a professional offensive security framework that remains disciplined, modular, and transparent. Its long-term value will come from maintainability, responsible design, and a consistent user experience.

## Coding Philosophy

RAPO should be built with the following principles in mind:

- Small, focused modules
- Predictable interfaces
- Clear error handling
- Minimal unnecessary abstraction
- Professional output
- Safe and responsible behavior
