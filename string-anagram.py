from collections import Counter

def stringAnagram(dictionary, query):
    dict_counts = Counter([''.join(sorted(word)) for word in dictionary])
    anagramList = []
    for el in query:
        anagramList.append(dict_counts[''.join(sorted(el))])
    return anagramList
