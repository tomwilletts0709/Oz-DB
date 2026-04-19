# Oz DB

Oz DB is a small database prototype that is currently being shaped into a simple in-memory database.

The intended scope is deliberately narrow:

- store data in memory only
- support a single hard-coded table
- allow two operations:
  - insert a row
  - print all rows

## Schema

The current table shape is:

| Column | Type |
| --- | --- |
| `id` | integer |
| `username` | varchar(32) |
| `email` | varchar(255) |

## Project Layout

- `ozdb/db.py` - the main database prototype, including row serialization helpers and the REPL-style command flow
- `ozdb/storage.py` - a storage wrapper that is still being sketched out
- `ozdb/tokenizer.py` - a simple tokenizer prototype
- `tests/test_db.py` - tests for row serialization and statement preparation
- `oz_db_changelogs.md` - notes about the project direction and original target behavior

## Current State

This repository is still early-stage and some modules are incomplete. The most stable pieces right now are:

- `Row` serialization and deserialization
- basic `insert` and `select` statement preparation

The rest of the database stack is still evolving.

## Running Tests

The test suite is written for `pytest`.

```bash
pytest
```

## Development Notes

- The codebase is moving toward a pager/table/cursor style design.
- Several functions in `ozdb/db.py` are still placeholders or draft implementations.
- If you are extending the project, it is worth keeping the README in sync with the actual command flow and storage model as they settle.
