# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    first_dict = {}
    second_dict = {}
    for x in word:
        if x in first_dict:
            first_dict[x] += 1
        else:
            first_dict[x] = 1
    for x in anagram:
        if x in second_dict:
            second_dict[x] += 1
        else:
            second_dict[x] = 1

    if first_dict == second_dict:
        print("True")
        return True
    else:
        print("False")
        return False


find_anagram("below", "elbow")
find_anagram("hello", "check")
