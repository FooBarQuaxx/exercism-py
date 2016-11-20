def detect_anagrams(S, L):
    return [word for word in L if len(word) == len(S) and
            S.lower() != word.lower() and
            sorted(S.lower()) == sorted(word.lower())]
