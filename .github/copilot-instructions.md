<!-- Auto-generated: concise, actionable guidance for AI coding agents. -->
# Copilot instructions for this repository

Purpose: Help AI coding agents become productive quickly in this repository by describing how to discover architecture, developer workflows, conventions, and integration points. Update this file when repository layout or workflows change.

**Repository Status**: A quick scan found no source files or guidance files (`README.md`, `package.json`, `pyproject.toml`, `.github/workflows/*`) at the repository root. If this repository is a submodule or you expect code elsewhere, check with the maintainer.

**First Steps (what to run and why)**
- **Search for entry points**: Look for `package.json`, `pyproject.toml`, `requirements.txt`, `setup.py`, `Cargo.toml`, `go.mod`, `Gemfile`, `build.sbt`, `Dockerfile`, `docker-compose.yml`, and `README.md`.
- **PowerShell commands to run when a stack is detected**:
  - Node: `npm install; npm test` (or `pnpm install; pnpm test` if `pnpm-lock.yaml` present)
  - Python: `python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; pytest` 
  - .NET: `dotnet restore; dotnet build; dotnet test` 
  - Go: `go test ./...` 
  - Docker compose: `docker-compose up --build` (requires Docker Desktop)

**Architecture discovery checklist (how I learn the "big picture")**
- Look for top-level directories named `api`, `services`, `cmd`, `pkg`, `internal`, `web`, `worker`, `infra`, or `deploy` — they often map to service boundaries.
- Inspect config files (`config/*.yaml`, `config/*.json`, `env/*.env`, `*.tf`) to learn runtime wiring and external dependencies.
- Search for `Dockerfile`, `docker-compose.yml`, and `.github/workflows/` to understand deployment and CI flows.
- Trace data flows by locating message/queue code (`rabbitmq`, `kafka`, `sqs`), `grpc`/`proto` files, or REST controllers (e.g., `routes`, `controllers`, `handlers`).

**Project-specific patterns to look for**
- Tests: Prefer `tests/` or files with `test_` / `_test` suffix — run these first to establish a safety net.
- Scripts: Check `package.json` `scripts` or `Makefile` targets for canonical build/test commands.
- Configuration over code: If `config/*.yaml` plus adapter modules are present, follow the config layering used (dev/staging/prod).
- Language idioms: If you see `src/` + `tsconfig.json` → TypeScript monorepo conventions; `src/main.go` → Go binary; `app/__init__.py` → Python package.

**Integration points & external dependencies**
- Check `requirements.txt` / `package.json` / `go.mod` / `Cargo.toml` for external services and SDKs (AWS, GCP, DB clients).
- Look for `*.proto` or `openapi.yaml` to find cross-service contracts.
- Look for `terraform/`, `k8s/`, or `helm/` directories describing infra assumptions and secrets management.

**How to modify code safely (project rules)**
- Always run the repository's test suite and linters using the canonical scripts (`package.json` scripts or `Makefile`) before proposing changes.
- When adding behavior, prefer to follow existing patterns: use the same directory for new handlers, use existing naming conventions for environment variables (`UPPER_SNAKE_CASE`), and match existing logging/metrics patterns.

**Merging guidance (if `copilot-instructions.md` already exists)**
- Preserve user-written rationale and examples. Append automation or detection heuristics only if they are verifiable by reading repository files.

**If no code is present (this repo)**
- Ask the maintainer where the source lives (subfolder, branch, or external repo). Suggest common locations: `./src`, `./app`, or a sibling repo.
- Offer these follow-ups: (1) run the discovery checklist after pointing to the code root, (2) create a minimal README with build commands, or (3) add a `project-metadata.md` describing the stack.

**Examples (what to cite in instructions)**
- If you find `package.json` with `"start": "node ./dist/index.js"`, use that to run the app instead of guessing `node index.js`.
- If there is `docker-compose.yml` referencing `redis` and `postgres`, assume local integration tests use those services and document `docker-compose up` as a test dependency.

If anything above is unclear or you want the file tailored to a specific language or framework, point me to the project root or share the main source files and I'll iterate.
