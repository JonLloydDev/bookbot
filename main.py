from stats import getWordCount,charCounts,charReport
import sys

# Check inputs
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
elif not sys.argv[1].strip().lower().endswith('.txt'):
    print('This script expects a .txt file.')
    sys.exit(2)

def getBookText(filePath:str):
    with open(filePath,'r') as f:
        return f.read()

def main():
    book = sys.argv[1]
    text = getBookText(book)
    print(f'Found {getWordCount(text)} total words')
    counts = charCounts(text)
    for k,v in charReport(counts):
        print(f'{k}: {v}')

main()