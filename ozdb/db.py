import sys
import re
import struct
from enum import Enum, auto
from dataclasses import dataclass, field    
from typing import Optional, Protocol



class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = auto()
    META_COMMAND_UNRECOGNIZED_COMMAND = auto()

class PrepareResult(Enum): 
    PREPARE_SUCCESS = auto()
    PREPARE_UNRECOGNIZED_STATEMENT = auto()
    PREPARE_SYNTAX_ERROR = auto() 
    PREPARE_NEGATIVE_ID = auto()
    PREPARE_STRING_TOO_LONG = auto()

@dataclass(slots = True)
class Row: 
    id: int
    username: str
    email: str

@dataclass 
class InputBuffer: 
    buffer: str
    buffer_length: int 
    input_length: int

class StatementType(Enum):
    STATEMENT_INSERT = auto()
    STATEMENT_SELECT = auto()
    ROW_TO_INSERT = auto()
    EXECUTE_SUCCESS = auto()


def table_max_pages() -> int: 
    return 400

@dataclass
class Pager: 
    file_descriptor: int
    file_length: int
    num_pages: int
    pages: list[Optional[bytes]]

@dataclass
class Table: 
    page: int
    root_page_num: int
    num_rows: int

@dataclass 
class Cursor: 
    table: Table
    page_num: int
    cell_num: int
    end_of_table: bool

ID_SIZE = 4
USERNAME_SIZE = 32
EMAIL_SIZE = 255

ROW_FORMAT = f"{ID_SIZE}s{USERNAME_SIZE}s{EMAIL_SIZE}s"
ROW_SIZE = struct.calcsize(ROW_FORMAT)

PAGE_SIZE = 4096
ROWS_PER_PAGE = PAGE_SIZE // ROW_SIZE
TABLE_MAX_ROWS = ROWS_PER_PAGE * table_max_pages()


def serialize_row(row: Row) -> bytes:
    return struct.pack(ROW_FORMAT, row.id.to_bytes(ID_SIZE, 'little'), row.username.encode('utf-8'), row.email.encode('utf-8'))

def deserialize_row(data: bytes) -> Row:
    unpacked_data = struct.unpack(ROW_FORMAT, data)
    return Row(id=int.from_bytes(unpacked_data[0], 'little'), username=unpacked_data[1].decode('utf-8').rstrip('\x00'), email=unpacked_data[2].decode('utf-8').rstrip('\x00'))

def row_slot(table: Table, row_num: int) -> int:
    page_num = row_num // ROWS_PER_PAGE
    page = table.Pager.pages[page_num]
    if page is None: 
        page = bytearray(PAGE_SIZE)
        row_offset = row_num % ROWS_PER_PAGE
        byte_offset = row_offset * ROW_SIZE
        return page + byte_offset

def new_table() -> Table:
    pager = Pager (
        file_descriptor = 0,
        file_length = 0,
        num_pages = 0,
        pages = [None] * table_max_pages()
    )

    return Table (
        pager = pager, 
        root_page_num = 0,
        num_rows = 0
    )
    
def free_table(table: Table) -> None: 
    for i in range(table.Pager.num_pages): 
        if table.Pager.pages[i] is not None: 
            del table.Pager.pages[i]


def meta_command_result() -> MetaCommandResult:
    if input_buffer.buffer == ".exit":
        input_buffer.close()
        sys.exit(0)
    else: 
        return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND
    
def execute_statement(statement_type: StatementType):
    match statement_type:
        case StatementType.STATEMENT_INSERT:
            print("This is where we would do an insert")
        case StatementType.STATEMENT_SELECT:
            print("This is where we would do a select")


def new_input_buffer() -> InputBuffer:
    input_buffer = InputBuffer()
    input_buffer.buffer_length = 0
    input_buffer.input_length = 0
    return input_buffer

def print_prompt(): 
    print("db > ", end='')

def read_input(input_buffer): 
    bytes_read = sys.stdin.readline()
    input_buffer.buffer = bytes_read.strip()
    if bytes_read <= 0:
        print("Error reading input")
        sys.exit(1)
    
    input_buffer.input_length = bytes_read - 1
    input_buffer.buffer[bytes_read - 1] = '\0'


def close_input_buffer(input_buffer):
    input_buffer.buffer = None

def main(): 
    table = new_table()
    input_buffer = new_input_buffer() 
    while True: 
        print_prompt()
        read_input(input_buffer)

        if input_buffer.buffer == ".exit": 
            close_input_buffer(input_buffer)
            sys.exit(0)
        else: 
            print(f"unrecognized command: {input_buffer.buffer}")


def prepare_statement(statement_type: StatementType, input_buffer) -> tuple[PrepareResult, Optional[Row]]:
    if input_buffer.buffer.startswith("insert"):
        args_assigned = re.match(r"insert\s+(\d+)\s+(\w+)\s+(\w+)", input_buffer.buffer)
        if not args_assigned: 
            return PrepareResult.PREPARE_SYNTAX_ERROR, None
        row = Row(id=int(args_assigned.group(1)), username=args_assigned.group(2), email=args_assigned.group(3))
        return PrepareResult.PREPARE_SUCCESS, StatementType.STATEMENT_SELECT ,row
    
    elif input_buffer.buffer.startswith("select"):
        return PrepareResult.PREPARE_SUCCESS, StatementType.STATEMENT_SELECT, None
    else: 
        return PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT, None

def execute_insert(statement_type: StatementType, table: Table, row_to_insert: Row) -> None:
    if table.num_rows >= TABLE_MAX_ROWS: 
        print("Error: Table full.")
        return
    
    row_slot = row_slot(table, table.num_rows)
    serialize_row(row_to_insert, row_slot)
    table.num_rows += 1
    return EXECUTE_SUCCESS

def execute_select(statement_type: StatementType, table: Table) -> None:
    for i in range(table.num_rows): 
        row_slot = row_slot(table, i)
        row = deserialize_row(row_slot)
        print(f"({row.id}, {row.username}, {row.email})")
    return EXECUTE_SUCCESS

def execute_statement(statement_type: StatementType, table: Table, row_to_insert: Row) -> None:
    match statement_type:
        case StatementType.STATEMENT_INSERT:
            return execute_insert(statement_type, table, row_to_insert)
        case StatementType.STATEMENT_SELECT:
            return execute_select(statement_type, table)
        
