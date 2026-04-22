# Oz DB

Oz DB is a learning project: a Python port of `cstack/db_tutorial`, translated from C to Python by hand.

It is intentionally framed this way because the goal is not to ship a polished database product. The goal is to understand how database internals fit together by building them from first principles. That means working through the parts that are usually hidden behind a library or framework:

- the storage engine
- page layout and row serialization
- B-tree indexing
- transaction handling

## Why I Am Building It

The point of the project is following the Feynman principle that if you can't build it you can't understsand it. I essentially want to understand how a database actually works under the hood, and the best way I know to do that is to implement one myself.

This repository is therefore a study log as much as a codebase.

## Rule I Set For Myself

To keep the learning honest, I have set one hard rule:

- no AI assistance for the implementation
- hand-typed code only

That rule matters because the value here is in the act of thinking through the design, making mistakes, and correcting them directly.

## What It Is Today

The current target is still the one described in the changelog:

- an in-memory database only
- a single hard-coded table
- two supported operations:
  - insert a row
  - print all rows

The current schema is:

| Column | Type |
| --- | --- |
| `id` | integer |
| `username` | varchar(32) |
| `email` | varchar(255) |

## What Is Currently Implemented

Based on the changelog and the current code, the project has moved beyond the very first sketch and now includes:

- a `Row` shape for the table data
- row serialization and deserialization helpers
- a statement preparation path for `insert` and `select`
- a REPL-style command loop scaffold in `ozdb/db.py`
- pager, table, and cursor dataclasses that point toward a page-based storage model
- a storage wrapper stub in `ozdb/storage.py`
- an early tokenizer in `ozdb/tokenizer.py`
- a small pytest suite covering row round-tripping and statement parsing

That is enough to show the direction of the system, but not enough to call it complete.

## What Is Not Done Yet

The database is still missing most of the hard parts:

- a finished and consistent parser
- a working, coherent execution path for inserts and selects
- durable storage behavior
- B-tree indexing
- transactions
- cleanup of draft or placeholder code in `ozdb/db.py`
- a stable command-line entry point
- a completed package configuration and broader test coverage

In other words, the skeleton is present, but the database is not finished.

## What I Have Learned So Far

This project has already made a few things concrete for me:

- how much of a database is about careful data layout, not just query logic
- how serialization choices shape everything else downstream
- how quickly a parser, execution layer, and storage layer can get tangled if the boundaries are fuzzy
- why pager-backed storage and fixed-size pages matter
- how much discipline is needed to keep a small database prototype from turning into a pile of half-finished ideas

That is the real value of the project so far.

## Project Layout

- `ozdb/db.py` - the main prototype, including row helpers and the REPL-style flow
- `ozdb/storage.py` - a storage wrapper that is still being sketched out
- `ozdb/tokenizer.py` - an early tokenizer prototype
- `tests/test_db.py` - tests for serialization and statement preparation
- `oz_db_changelogs.md` - the original target behavior and current direction

## Running Tests

The test suite uses `pytest`.

```bash
pytest
```

## Status Note

This repository is a learning project in progress, not a finished database.

That distinction is intentional. It keeps the scope honest and makes it clear that the value here is in the process of building and understanding, not in pretending the work is already done.
# ecomm_tom
