from ozdb.db import (
    InputBuffer, Row, PrepareResult, StatementType,
    prepare_statement, serialize_row, deserialize_row,
)


def make_buffer(text: str) -> InputBuffer:
    return InputBuffer(buffer=text, buffer_length=len(text), input_length=len(text))


# --- serialize / deserialize ---

def test_serialize_deserialize_roundtrip():
    row = Row(id=1, username="alice", email="alice@example.com")
    data = serialize_row(row)
    result = deserialize_row(data)
    assert result.id == 1
    assert result.username == "alice"
    assert result.email == "alice@example.com"


# --- prepare_statement ---

def test_prepare_insert_success():
    buf = make_buffer("insert 1 alice alice@example.com")
    result, *_ = prepare_statement(StatementType.STATEMENT_INSERT, buf)
    assert result == PrepareResult.PREPARE_SUCCESS

def test_prepare_insert_missing_args():
    buf = make_buffer("insert 1 alice")
    result, *_ = prepare_statement(StatementType.STATEMENT_INSERT, buf)
    assert result == PrepareResult.PREPARE_SYNTAX_ERROR

def test_prepare_select_success():
    buf = make_buffer("select")
    result, *_ = prepare_statement(StatementType.STATEMENT_SELECT, buf)
    assert result == PrepareResult.PREPARE_SUCCESS

def test_prepare_unrecognized_command():
    buf = make_buffer("foobar")
    result, *_ = prepare_statement(StatementType.STATEMENT_INSERT, buf)
    assert result == PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT
