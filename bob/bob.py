import re


def hey(what):
    def is_question():
        return what.strip().endswith('?')

    def is_yelled_at():
        return re.search(r'[^\W\d_]', what, re.UNICODE) and \
                what.upper() == what

    def is_addressed():
        return what.strip() == ''

    if is_yelled_at():
        return 'Whoa, chill out!'
    if is_question():
        return 'Sure.'
    if is_addressed():
        return 'Fine. Be that way!'
    return 'Whatever.'
