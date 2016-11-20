from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day, order):
    day_code = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day)
    c = calendar.Calendar()
    day2wday = list(filter(lambda x: x[0] != 0 and x[1] == day_code, c.itermonthdays2(year, month)))
    res = None
    order_map = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}
    if order in order_map:
        try:
            wday = day2wday[order_map[order]][0]
        except IndexError as e:
            raise MeetupDayException
        else:
            res = date(year, month, wday)

    elif order == 'teenth':
        wday = list(filter(lambda x: 10 <= x[0] < 20, day2wday))[0][0]
        res = date(year, month, wday)
    if not res:
        raise MeetupDayException
    return res


if __name__ == '__main__':
    print(meetup_day(2013, 5, 'Monday', 'teenth'))
