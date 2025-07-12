import re

class Search:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "r") as file:
                self.elements = file.readlines()
        except FileNotFoundError:
            raise Exception(f"The file {self.filename} is not found.")
    
    def clean(self):
        """Removes special characters from each line"""
        pat = "[^A-Za-z0-9 ]"
        self.elements = [re.sub(pat, "", line) for line in self.elements]
    
    def getLines(self, word):
        """Search for the word in the lines and return the result as requested"""
        result = [word]
        for index, line in enumerate(self.elements):
            if word.lower() in line.lower():  
                result.append((index + 1, line.strip()))
            if len(result)==1:
                raise Exception(f"Word '{word}' not found")
        return result 