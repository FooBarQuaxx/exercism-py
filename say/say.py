MAX = pow(10, 12) - 1
MIN = 0


class Sayer(object):

    _0to9 = [
        'zero', 'one', 'two',
        'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine',
    ]

    _10to19 = [
        'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]

    _TENS = [
        'twenty', 'thirty',
        'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninty',
    ]

    def say_digits(self, digits, add_add=False):
        assert 0 <= digits < 10
        val = self._0to9[int(digits)]
        return ('and ' if add_add else '') + val

    def say_tens(self, tens, add_add=False):

        assert 0 <= tens < 100

        if tens < 10:
            return self.say_digits(tens, add_add)

        if tens < 20:
            val = self._10to19[tens-10]
        else:
            x = tens // 10
            y = tens - 10 * x
            z = self._TENS[x - 2]
            if y == 0:
                val = z
            else:
                val = '-'.join([z, self.say_digits(y, add_add)])

        return ('and ' if add_add else '') + val

    def say_hundreds(self, hundreds, add_add=False):
        assert 0 <= hundreds < 1e3

        if hundreds < 1e2:
            return self.say_tens(hundreds, add_add)

        x = hundreds // pow(10, 2)
        y = hundreds - x * pow(10, 2)
        z = self.say_tens(x) + ' hundred'
        if y == 0:
            return z
        else:
            return ' and '.join([z, self.say_tens(y)])

    def say_thousands(self, thousands):
        assert 0 <= thousands < 1e6
        if thousands < 1e3:
            return self.say_hundreds(thousands, add_add=True)
        x = thousands // pow(10, 3)
        y = thousands - pow(10, 3) * x
        z = self.say_hundreds(x) + ' thousand'
        if y == 0:
            return z
        else:
            return ' '.join([z, self.say_hundreds(y, add_add=True)])

    def say_milltions(self, millions):
        assert 0 <= millions < 1e9
        if millions < 1e6:
            return self.say_thousands(millions)
        x = millions // pow(10, 6)
        y = millions - pow(10, 6) * x
        z = self.say_hundreds(x) + ' million'
        if y == 0:
            return z
        else:
            return ' '.join([z, self.say_thousands(y)])

    def say_billions(self, billions):
        assert 0 <= billions < 1e12
        if billions < 1e9:
            return self.say_milltions(billions)
        x = billions // pow(10, 9)
        y = billions - pow(10, 9) * x
        z = self.say_hundreds(x) + ' billion'
        if y == 0:
            return z
        else:
            return ' '.join([z, self.say_milltions(y)])
        pass

    def say(self, num):
        if not MIN <= num <= MAX:
            raise AttributeError

        # 0   0 0 000 000 000
        # 11 10 9 876 543 210
        if 0 <= num < 10:
            val = self.say_digits(num)
        elif 10 <= num < 1e2:
            val = self.say_tens(num)
        elif 1e2 <= num < 1e3:
            val = self.say_hundreds(num)
        elif 1e3 <= num < 1e6:
            val = self.say_thousands(num)
        elif 1e6 <= num < 1e9:
            val = self.say_milltions(num)
        else:
            val = self.say_billions(num)

        return val


def say(num):
    try:
        val = Sayer().say(num)
    except AttributeError as e:
        raise e
    else:
        return val
