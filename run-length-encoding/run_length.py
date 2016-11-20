import re


def encode(s):
    _s = s.strip()
    if not _s:
        return ''
    res = ''
    i = 1
    counter = 1
    while i < len(_s):
        while i < len(_s) and _s[i-1] == _s[i]:
            i += 1
            counter += 1

        res += str(counter) + _s[i-1] if counter > 1 else _s[i-1]
        counter = 1
        i += 1
    if res[-1] != _s[-1]:  # Weird case
        res += _s[-1]
    return res


def decode(s):
    res = ''
    matches = re.findall(r'(?:(\d+)?([^\d]))', s, re.UNICODE)
    for match in matches:
        res += int(match[0]) * match[1] if len(match[0]) > 0 else match[1]
    return res
