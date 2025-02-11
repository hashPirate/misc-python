import itertools

def read_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set(words)
def find_anagrams(letters, words):
    anagrams = set()
    for i in range(len(letters)):
        for perm in itertools.permutations(letters, i + 1):
            word = ''.join(perm)
            if word in words:
                anagrams.add(word)
    return sorted(anagrams, key=lambda x: (-len(x), x))
def main():
    words = read_words('words.txt')
    letters = input('Enter the letters: ').strip()
    anagrams = find_anagrams(letters, words)
    
    for word in anagrams:
        print(word)
if __name__ == "__main__":
    main()
