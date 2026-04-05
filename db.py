import sys
from dataclasses import dataclass

@dataclass 
class input_buffer: 
    buffer: str = None
    buffer_length: int 
    input_length: int

def new_input_buffer() -> input_buffer:
    input_buffer = input_buffer()
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

