"""Markdown catalog for ``ebooks-cli explain <path>``.

Each entry is verbatim markdown. Keys are command-path tuples. The empty tuple
and ``("ebooks-cli",)`` both resolve to the root entry.

Keep bodies self-contained: an agent reading one entry should get enough
context without chaining reads.
"""

from __future__ import annotations

_ROOT = """\
# ebooks-cli

A clonable template for AgentCulture mesh agents. It carries an agent-first CLI
(cited from the teken `python-cli` reference), a mesh identity (`culture.yaml` +
`CLAUDE.md`), the canonical guildmaster skill kit under `.claude/skills/`, and a
buildable/deployable package baseline. Clone it, rename the package, edit
`culture.yaml`, and you have a new agent.

## Verbs

- `ebooks-cli whoami` — identity probe from `culture.yaml`.
- `ebooks-cli learn` — structured self-teaching prompt.
- `ebooks-cli explain <path>` — markdown docs for any noun/verb.
- `ebooks-cli overview` — descriptive snapshot of the agent.
- `ebooks-cli doctor` — check the agent-identity invariants.
- `ebooks-cli cli overview` — describe the CLI surface.

## Exit-code policy

- `0` success
- `1` user-input error
- `2` environment / setup error
- `3+` reserved

## See also

- `ebooks-cli explain whoami`
- `ebooks-cli explain doctor`
"""

_WHOAMI = """\
# ebooks-cli whoami

Reports the agent's identity from `culture.yaml`: nick (`suffix`), backend,
served model, and the package version. Read-only.

## Usage

    ebooks-cli whoami
    ebooks-cli whoami --json
"""

_LEARN = """\
# ebooks-cli learn

Prints a structured self-teaching prompt covering purpose, command map,
exit-code policy, `--json` support, and the `explain` pointer.

## Usage

    ebooks-cli learn
    ebooks-cli learn --json
"""

_EXPLAIN = """\
# ebooks-cli explain <path>

Prints markdown documentation for any noun/verb path. Unlike `--help` (terse,
positional), `explain` is global and addressable by path.

## Usage

    ebooks-cli explain ebooks-cli
    ebooks-cli explain whoami
    ebooks-cli explain --json <path>
"""

_OVERVIEW = """\
# ebooks-cli overview

Read-only descriptive snapshot of the agent: identity (from `culture.yaml`), the
verb surface, and the sibling-pattern artifacts the template carries. Accepts an
ignored `target` so a stray path never hard-fails.

## Usage

    ebooks-cli overview
    ebooks-cli overview --json
"""

_DOCTOR = """\
# ebooks-cli doctor

Checks the agent-identity invariants `steward doctor` verifies:
prompt-file-present and backend-consistency (`claude` → `CLAUDE.md`), plus a
skills-present check. Exits 1 when unhealthy.

prompt-file-present requires the *resident* prompt the declared backend
actually reads. Other harness prompt files recognized under the same backend
name (`AGENTS.override.md`, `.pi/SYSTEM.md`, `QWEN.md`) belong to
interactively available harnesses the mesh daemon never loads; they are
reported by the informational harness-prompts check and never substituted.

## Usage

    ebooks-cli doctor
    ebooks-cli doctor --json
"""

_CLI = """\
# ebooks-cli cli

Noun group for CLI-surface introspection. `cli overview` describes the CLI
itself (distinct from the global `overview`, which describes the agent).

## Usage

    ebooks-cli cli overview
    ebooks-cli cli overview --json
"""


ENTRIES: dict[tuple[str, ...], str] = {
    (): _ROOT,
    ("ebooks-cli",): _ROOT,
    ("whoami",): _WHOAMI,
    ("learn",): _LEARN,
    ("explain",): _EXPLAIN,
    ("overview",): _OVERVIEW,
    ("doctor",): _DOCTOR,
    ("cli",): _CLI,
    ("cli", "overview"): _CLI,
}
