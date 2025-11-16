# Ascendancy Seasonal Campaign System

A digitized version of my personal objective tracking and planning system. I find that the system works best when written and management manually with pen to paper but creating a digital variant for data tracking, remote access, or for people who prefer it is a good way for me to grind rust off of skills while learning some new ones.

## Objective

Develop a fullstack CRUD app, using minimal AI, that fills a gap in my personal planning system, so that I can add to, improve, and demonstrate my skills.

## Intended Stack

**Backend:** FastAPI
**Frontend Web:** React + Vite
**Frontend Mobile:** React-Native
**NeoVim Plugin:** Lua
**TUI**: Rust
**DevOps** Nix, devenv, Github actions, Caddy

### Nix Tooling Overview

All builds and tests are **Nix‑driven**, guaranteeing the same environment you use locally.

| Tool                       | Why this instead of containers                                                                                                                                                     |
| -------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------                                          |
| devenv                     | Declarative dev shells + long‑running services (Postgres, Caddy, hot-reloading FastAPI, Vite server, etc.) that start with `devenv up`. No daemon‑level container runtime needed. |
| Nix                        | Expose each component as a Nix derivation so they can be built, tested, or run directly from the command line (`nix develop .#backend`, `nix build .#frontend`, etc.).                |
| Nix Flakes                 | Easily pin exact pkg versions to reproduce builds for CI and releases.                                                                                                                  |
| Nixpkgs                    | Ready‑made packages without pulling images.                                                                                                                                      |
| Caddy (as a Nix service)   | Handle TLS & reverse‑proxy `devenv` without needing a container.                                                                                                                   |
## Issue Tracking and TODOs

This repository tracks and prioritizes issues using GitHub Projects
https://github.com/users/EmergentMind/projects/1

As a general rule, TODOs and FIXMEs should be addressed prior to PR or converted to Issues for prioritization. 

Using Projects is for practice and demonstration instead of personal preference.
