# Oz DB Codebase Notes

Date: 11.04.2026

## What this project is

Oz DB is a small database prototype. The current direction is an in-memory database that starts with a single hard-coded table and supports two basic operations:

- inserting a row
- printing all stored rows

The codebase is still early, so several modules are scaffolds rather than finished implementations.

## File Overview

### `ozdb/db.py`

This is the main entry point and the clearest picture of the current database loop.

It defines a few core concepts:

- `MetaCommandResult`, `PrepareResult`, and `StatementType` enums for representing command and statement states
- `InputBuffer`, which is meant to hold the current line of user input
- helper functions for the REPL-style loop, including:
  - `new_input_buffer()`
  - `print_prompt()`
  - `read_input()`
  - `close_input_buffer()`
  - `prepare_statement()`
  - `execute_statement()`

At the moment, this file is still a prototype. Some functions are placeholders, and a few lines look unfinished or inconsistent, which suggests the command-processing flow is still being built out.

### `ozdb/storage.py`

This module is intended to handle data storage behind the database interface.

The `Storage` class currently:

- stores a `db` reference
- keeps an in-memory `data` dictionary
- includes methods that are clearly meant for save/load/read behavior

This file is also incomplete right now. The structure shows the intended direction, but the method definitions still need cleanup and finishing.

### `ozdb/tokenizer.py`

This file is currently empty.

Based on the project direction, it will likely become responsible for breaking user input into tokens before statements are prepared and executed.

### `ozdb/table.py`

This file is currently empty.

It will probably hold table-related logic once the database starts modelling rows, columns, and table operations more explicitly.

### `tests/test_db.py`

This test file is currently empty.

It is ready to become the place for unit tests around parsing, storage behavior, and the database command loop.

### `oz_db_changelogs.md`

This file contains the current project notes and target features. It says the database should:

- support inserting a row and printing all rows
- stay in memory only, with no disk persistence
- work with a single hard-coded table

It also includes the intended table shape:

- `id` as an integer
- `username` as `varchar(32)`
- `email` as `varchar(255)`

## Current State

The codebase is at an early exploratory stage. The broad architecture is visible, but the implementation is not yet complete.

Right now, the main themes are:

- a REPL-style database loop in `db.py`
- an in-memory storage layer in `storage.py`
- future parsing and table logic waiting to be filled in

## Suggested Next Steps

- clean up the command loop in `ozdb/db.py`
- define the tokenizer and statement preparation flow
- flesh out the hard-coded table model
- add tests for the first working insert/select path
