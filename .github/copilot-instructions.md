<!-- Purpose: guidance for AI coding agents working in this repository. Keep short and actionable -->
# Copilot / AI agent instructions for this repository

This file documents the concrete, discoverable project patterns and workflows an AI agent should follow to be immediately productive in this repo.

## Quick facts
- **Entry point / scripts:** `main.py` (present but currently empty).
- **Virtual environment:** `env/` is a checked-in virtualenv. Use `env\Scripts\Activate.ps1` (PowerShell) or run the interpreter directly at `env\Scripts\python.exe`.
- **Packaging / code layout:** No package directory found. New modules should be added as a top-level package directory (e.g. `steganography/`) with an `__init__.py` to make imports explicit.
- **Repo files of interest:** `README.md`, `LICENSE`, `main.py`, `env/` (venv and site-packages).

## What to do first (minimal steps)
1. Inspect `main.py` and `README.md`. `main.py` is currently empty; changes should be small and self-contained.
2. Use the venv Python for all runs to avoid host Python differences:

   PowerShell example:

   ```powershell
   .\env\Scripts\Activate.ps1
   python main.py
   # or without activating:
   .\env\Scripts\python.exe main.py
   ```

3. Install new dependencies into the venv using `env\Scripts\pip.exe install <pkg>` and record them in a `requirements.txt` at the repo root.

## Architecture notes (discoverable)
- There is currently no multi-module architecture to infer; treat this as a single-script repo unless you introduce a package. If you add modules, put them under `steganography/` and add `tests/` for unit tests.
- The `env/Lib/site-packages/` folder contains vendored Python packages — prefer using the venv's `pip` to add new packages rather than modifying `env/Lib` directly.

## Conventions & patterns for edits
- Keep changes minimal and incremental: update `main.py` or add a small package directory and a lightweight `README` section describing new behavior.
- If adding runtime dependencies, add or update `requirements.txt` and prefer pinned versions (e.g., `package==1.2.3`).
- For CLI behavior, implement argument parsing in `main.py` with `argparse` and keep the entrypoint simple:

  - Example: add a `if __name__ == '__main__':` block that calls a `main()` function.

## Testing & verification
- No test framework is present. If you add tests, use `pytest` and put tests under `tests/`.
- To run a quick smoke test after changes, use the venv python to execute the target script, e.g. `env\Scripts\python.exe main.py`.

## Integration points & external services
- No external services or integrations are present in the repository. Do not assume external CI or registries unless new files (e.g., GitHub Actions workflows) are added.

## Pull request / commit guidance for agents
- Make small, focused commits with a short message describing the change.
- When in doubt about design choices (package layout, API shapes), open a PR that is minimal and request review from the repository owner.

## If this file already exists
- If a future run finds this file already present, merge changes conservatively: preserve any human-written notes and only append or clarify repo-specific commands.

---
If any part of the project is not covered here or you want a different convention (package layout, test framework), ask the human maintainer before making wide-reaching changes.
