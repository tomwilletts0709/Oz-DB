"""
This is the storage file for the project. It contains the code for storing the data in the database.
"""

import db


class Storage: 
    def __init__(self, db, data: dict = None) -> None:  
        self.db = db    
        self.data = data if data is not None else {}



        def save_data(self, data: dict) -> None:
            """this method saves the data to the database"""
            self.data.update(data)
            self.db.save(self.data)

        def load_data(self) -> dict: 
            """this method loads the data from the database"""
            self.data = self.db.load()
            return self.data
        
        def delete_data(self, )
            
        

        def read_page(self, page_id: str) -> dict: 
            """this method reads a page from the database"""
            return self.data.get(page_id, {})
