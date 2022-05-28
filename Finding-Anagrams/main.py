# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

a = str(input("Enter the word: "))
b = str(input("Enter another word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word1 = word.lower()
    word2 = anagram.lower()
    sortedWord = sorted(word1)
    sortedAnagram = sorted(word2)
    if sortedWord == sortedAnagram:
        return True
    return False 

print(find_anagram(a, b))



