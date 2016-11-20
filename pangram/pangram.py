import string


def is_pangram(s):
    uniq = []
    for c in s.lower():
        if c in string.ascii_lowercase and c not in uniq:
            uniq.append(c)
            if len(uniq) == len(string.ascii_lowercase):
                break
    return ''.join(sorted(uniq)) == string.ascii_lowercase
