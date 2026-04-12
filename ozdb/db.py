import sys
import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, TypeVar, Protocol, Field


@dataclass 
class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = auto()
    META_COMMAND_UNRECOGNIZED_COMMAND = auto()

@dataclass
class PrepareResult(Enum): 
    PREPARE_SUCCESS = auto()
    PREPARE_UNRECOGNIZED_STATEMENT = auto()
    PREPARE_SYNTAX_ERROR = auto() 
    PREPARE_NEGATIVE_ID = auto()
    PREPARE_STRING_TOO_LONG = auto()

@dataclass(slots = True)
class Row: 
    id: int =
    username: str = Field(default="")
    email: str = Field(default="")

@dataclass 
class InputBuffer: 
    buffer: str = None
    buffer_length: int 
    input_length: int

@dataclass 
class StatementType(Enum): 
    STATEMENT_INSERT = auto()
    STATEMENT_SELECT = auto()
    ROW_TO_INSERT = auto()

def table_max_pages() -> int: 
    return 400

@dataclass
class Pager: 
    file_desriptor: int
    file_length: int
    num_pages: int
    pages: list[Optional[bytes]]

@dataclass
class Table: 
    Pager: pager
    root_page_num: int

@dataclass 
class Cursor: 
    table: Table
    page_num: int
    cell_num: int
    end_of_table: bool

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
    if bytes_read is <= 0: 
        print("Error reading input")
        sys.exit(1)
    
    input_buffer.input_length = bytes_read - 1
    input_buffer.buffer[bytes_read - 1] = '\0'


def close_input_buffer(input_buffer):
    input_buffer.buffer = None

def main(): 
    input_buffer = new_input_buffer() 

    while True: 
        print_prompt()
        read_input(input_buffer)

        if input_buffer.buffer == "exit": 
            close_input_buffer(input_buffer)
            sys.exit(0)
        else: 
            print(f"unrecognized command: {input_buffer.buffer}")


def prepare_statement(statement_type: StatementType, input_buffer) -> PrepareResult:
    match PrepareResult:
        args_assigned = re.match(r"insert\s+(\d+)\s+(\w+)\s+(\w+)", input_buffer.buffer)
        if args_assigned:
            statement_type = StatementType.STATEMENT_INSERT
            row_to_insert.id = int(args_assigned.group(1))
            row_to_insert.username = args_assigned.group(2)
            row_to_insert.email = args_assigned.group(3)
        if args assigned is =< 3:
            return PrepareResult.PREPARE_SYNTAX_ERROR
        else:
    return PrepareResult.PREPARE_SUCCESS


def execute_statement(statement_type: StatementType):
    print(f"executed: {statement_type}")


