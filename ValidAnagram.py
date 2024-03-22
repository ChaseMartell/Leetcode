def validAnagram_dic(string1, string2):
    dictionary_1 = {}
    dictionary_2 = {}

    for c in string1:
        dictionary_1[c] = dictionary_1.get(c, 0) + 1

    for c in string2:
        dictionary_2[c] = dictionary_2.get(c, 0) + 1

    return dictionary_1 == dictionary_2

def validAnagram_sort(string1, string2):
    return sorted(string1) == sorted(string2)

def main():
    print(validAnagram_dic("anagram", "nagaram"))
    print(validAnagram_sort("anagram", "nagaram"))

    print(validAnagram_dic("rat", "car"))
    print(validAnagram_sort("rat", "car"))

if __name__ == "__main__":
    main()
