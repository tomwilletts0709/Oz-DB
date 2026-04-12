import sys
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, TypeVar, Protocol

T = TypeVar('T')

@dataclass 
class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = auto()
    META_COMMAND_UNRECOGNIZED_COMMAND = auto()

@dataclass
class PrepareResult(Enum): 
    PREPARE_SUCCESS = auto()
    PREPARE_UNRECOGNIZED_STATEMENT = auto() 

@dataclass 
class InputBuffer: 
    buffer: str = None
    buffer_length: int 
    input_length: int

@dataclass 
class StatementType(Enum): 
    STATEMENT_INSERT = auto()
    STATEMENT_SELECT = auto()

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


def prepare_statement(input_buffer) -> PrepareResult:
    match PrepareResult:
        case PrepareResult.PREPARE_SUCCESS:
            print("This is where we would do an insert")
        case PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT:
            print("This is where we would do a select")
    return PrepareResult.PREPARE_SUCCESS


def execute_statement(statement_type: StatementType):
    print(f"executed: {statement_type}")


