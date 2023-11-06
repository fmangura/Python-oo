"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, file):
        self.read = open(f"{file}", "r")
        self.words = [line.strip() for line in self.read]
        # print(len(self.words))

    def list(self):
        return self.words

    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    
    def list_special(self, file):
        return [list.strip() for list in self.read if list.strip() and not list.startswith('#')]

