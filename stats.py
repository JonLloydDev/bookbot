from typing import List, Dict, Union

def getWordCount(text:str) -> int:
    return len(text.split())

def charCounts(text:str) -> Dict[str,int]:
    text = text.lower()
    chars = set(text)
    totalLen = len(text)
    charCounts = {}
    for char in chars:
        charCounts[char] = totalLen - len(text.replace(char,''))
    return charCounts

def charReport(charDict:Dict[str,int]) -> List[List[Union[str,int]]]:
    charDict = [[char,charDict[char]] for char in charDict if char.isalpha()] # Make lists of alpha k-v pairs
    return sorted(charDict, key=lambda x: x[1], reverse=True) # Sort k-v pairs by largest value first