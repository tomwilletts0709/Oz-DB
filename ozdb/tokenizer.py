"""
this is the tokenizer module, which provides functionality for tokenizing text data. It includes various tokenization techniques such as word tokenization, sentence tokenization, and character tokenization. The module also supports custom tokenization rules and can handle different languages and special characters.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass 
class Token:
    value: str
    type: str

@dataclass
class Keyword(Token):
    SELECT = "SELECT"
    FROM = "FROM"
    WHERE = "WHERE"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"



class Tokenizer: 
    def __init__(self, text: str) -> None: 
        self.text = text
        self.position = 0 
    
    def tokenize(self) -> List[Token]: 
        tokens = []
        while self.position < len(self.text): 
            current_char = self.text[self.position]

            if current_char.isspace(): 
                self.position += 1
                continue
            
            if current_char.isalpha(): 
                start_position = self.position
                while self.position < len(self.text) and self.text[self.position].isalpha():
                    self.position += 1
                value = self.text[start_position:self.position]
                token_type = "KEYWORD" if value.upper() in Keyword.__members__ else "IDENTIFIER"
                tokens.append(Token(value=value, type=token_type))
            else: 
                tokens.append(Token(value=current_char, type="SYMBOL"))
                self.position += 1
