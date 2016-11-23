import re

def abbreviate(words):
    matches = re.findall(r'(\b\w)|(-[a-z])|([a-z][A-Z])', words, re.UNICODE)
    acronyms = [list(filter(None, m))[0].lstrip('-')[-1].upper() for m in matches]
    return ''.join(acronyms)
