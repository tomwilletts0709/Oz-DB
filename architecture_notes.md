# Oz DB Codebase Notes

Date: 11.04.2026

## What this project is

Oz DB is a database prototype that is still being shaped. The current direction is an in-memory system with a single hard-coded table and support for two core operations:

- inserting a row
- printing all rows

The implementation is still early, but the code now sketches more of the database internals than it did before.

## File Overview

### `ozdb/db.py`

This is the main work-in-progress module and currently shows the broadest view of the system.

It now includes:

- command and prepare-state enums such as `MetaCommandResult`, `PrepareResult`, and `StatementType`
- a `Row` dataclass for the table shape
- `Pager`, `Table`, and `Cursor` dataclasses that suggest a move toward page-based storage
- `InputBuffer` for line input
- helper functions for the command loop, including:
  - `new_input_buffer()`
  - `print_prompt()`
  - `read_input()`
  - `close_input_buffer()`
  - `prepare_statement()`
  - `execute_statement()`

This file is still very unfinished. Some functions are placeholders, some code paths are inconsistent, and the current `prepare_statement()` logic looks like a draft rather than a working parser.

### `ozdb/storage.py`

This module is meant to wrap storage behavior behind the database layer.

The `Storage` class currently:

- keeps a `db` reference
- stores in-memory `data`
- sketches methods for saving, loading, deleting, and reading pages

The structure is there, but the implementation still needs cleanup. Right now it reads more like a design stub than a finished storage layer.

### `ozdb/tokenizer.py`

This file is empty for now.

It is likely intended to become the tokenizer that breaks user input into pieces before statement preparation.

### `ozdb/table.py`

This file is empty for now.

It should eventually hold table-specific behavior once the project moves past the first database skeleton.

### `tests/test_db.py`

This file is empty for now.

It is ready for tests around parsing, command handling, and any future insert/select flow.

### `pyproject.toml`

This file is currently empty, so there is no visible project metadata or dependency configuration in place yet.

### `oz_db_changelogs.md`

This file still captures the original target shape of the project. It says the database should:

- support inserting a row and printing all rows
- stay in memory only, with no persistence to disk
- use a single hard-coded table

It also records the intended schema:

- `id` as an integer
- `username` as `varchar(32)`
- `email` as `varchar(255)`

## Current State

The codebase is clearly moving from a minimal REPL prototype toward a more database-shaped design. The pager/table/cursor pieces are visible now, but most of the implementation is still incomplete.

The main themes are:

- a command loop and statement parser in `ozdb/db.py`
- a storage wrapper in `ozdb/storage.py`
- planned tokenizer and table modules
- no tests or packaging setup yet

## Suggested Next Steps

- finish and simplify the command/prepare flow in `ozdb/db.py`
- decide whether the pager/table/cursor model is the intended direction and make it consistent
- implement the tokenizer and table logic
- add a first test file once the insert/select path is stable
