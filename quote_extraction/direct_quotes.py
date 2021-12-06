import re
from typing import List


class QuoteExtractor:

    def __init__(self, regex=None):
        if not regex:
            self.regex=r"\B[‘\'\"](.*?)[’\'\"\"]+(?=$|\s)\B|\B[’\'\"](.*[^\'\s])+(?=$|\s)"
        else:
            self.regex = regex

    def extract_quotes(self, text: str) -> List[str]:
        matches = re.finditer(self.regex, text, re.MULTILINE)
        quotes = []
        for matchNum, match in enumerate(matches, start=1):
            quotes.append(match.group())
    
        return quotes
            
    
    def replace_quotes(self, text: str, replacement: str) -> str:
    	# original text, with quotes replaced
        return re.sub(self.regex, replacement, text, 0, re.MULTILINE)



