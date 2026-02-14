# CLAUDE.md

This file provides guidance for AI assistants working in this repository.

## Repository Overview

- **Repository:** Take20simpson/Take20simpson
- **Status:** New repository — project structure is being established

## Project Structure

This repository is in its initial setup phase. As files are added, update this section to reflect the directory layout.

```
Take20simpson/
├── CLAUDE.md          # AI assistant guidance (this file)
└── (project files TBD)
```

## Development Workflow

### Git Conventions

- **Default branch:** `main`
- Write clear, descriptive commit messages summarizing the "why" not just the "what"
- Keep commits focused — one logical change per commit
- Do not force-push to `main`

### Code Style

- Follow the conventions established by any linters or formatters configured in the project
- Prefer readability over cleverness
- Keep functions small and focused on a single responsibility

### Testing

- No test framework is configured yet
- When a test framework is added, document the commands here and ensure tests pass before committing

### Building / Running

- No build system is configured yet
- When build tooling is added, document the commands here

## Key Conventions for AI Assistants

1. **Read before editing** — Always read a file before proposing changes to it
2. **Minimal changes** — Only change what is necessary to fulfill the request; avoid unrelated refactors
3. **No secrets** — Never commit `.env` files, credentials, API keys, or other sensitive data
4. **Update this file** — When adding significant tooling, frameworks, or project structure, update this CLAUDE.md to keep it current
5. **Test before committing** — Run available tests and linters before creating commits
6. **Follow existing patterns** — Match the style and conventions already present in the codebase

## Dependencies

No dependencies are configured yet. When a package manager is set up (npm, pip, cargo, etc.), document installation steps here.

## Configuration Files

No project configuration files exist yet. As they are added (e.g., `package.json`, `tsconfig.json`, `.eslintrc`, `pyproject.toml`), document their purpose here.
