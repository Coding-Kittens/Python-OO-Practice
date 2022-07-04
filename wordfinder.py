"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    >>> wf = WordFinder("/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self,filePath):
        self.filePath =filePath
        self.words =[]
        self.get_words(self.filePath)


    def get_words(self,filePath):
        """ opens the file from the filePath and reads each line and puts them in a list"""
        num_of_words_read =0
        file =open(filePath,'r')
        for line in file:
            line = line[:line.find('\n')]
            self.words.append(line)
            num_of_words_read+=1
        file.close()
        print(f'{num_of_words_read} words read')

    def random(self):
        """picks a random word from the words list"""
        return random.choice(self.words)




class SpecialWordFinder(WordFinder):
    """returns a random word that is not a comment or a blank line"""

    def __init__(self, filePath):
        super().__init__(filePath)


    def get_words(self,filePath):
        super().get_words(filePath)
        self.words =[word.strip() for word in self.words if word.strip() !='' and not word.startswith('#')]
