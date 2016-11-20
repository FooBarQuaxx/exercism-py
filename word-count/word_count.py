from collections import Counter
import re


def word_count(s):
    words = re.findall(r'\w+', re.sub(r'[,_.]', ' ', s))
    words = (word.lower() for word in words)
    return dict(Counter(words))
