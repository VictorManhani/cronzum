import typing
import datetime

# https://stackoverflow.com/questions/4610904/calculate-next-scheduled-time-based-on-cron-spec
# https://www.geeksforgeeks.org/writing-cron-expressions-for-scheduling-tasks/
# https://crontab.cronhub.io/
# https://freeformatter.com/cron-expression-generator-quartz.html

class Cronzun:
    cron_expression: str = None
    from_datetime: typing.Union[datetime.datetime, None] = None

    def __init__(self, cron_expression: str, 
                 from_datetime: typing.Union[datetime.datetime, None] = None) -> None:
        # cron_expression = '* * * * * ? *'
        self.cron_expression = cron_expression
        self.from_datetime = self.default(from_datetime, datetime.datetime.now())

    def default(self, value_verified, value_default) -> typing.Union[typing.Any, None]:
        return value_verified if value_verified else value_default

    def set_from_datetime(self, dt: datetime.datetime) -> None:
        self.from_datetime = dt

    def get_next_date(self) -> datetime.datetime:
        cron_expr =      self.cron_expression.split(' ')
        _seconds =       cron_expr[0]
        _minutes =       cron_expr[1]
        _hours =         cron_expr[2]
        _day_of_month =  cron_expr[3]
        _month =         cron_expr[4]
        _day_of_week =   cron_expr[5]
        _year =          cron_expr[6]
    
        from_dt = self.from_datetime
        next_dt = from_dt

        if _seconds == '*':
            seconds = from_dt.second + 1
            seconds = 0 if seconds == 60 else seconds
        else:
            seconds = int(_seconds)
            if not (seconds >= 0 and seconds <= 59):
                raise Exception('Second value must be between 0 and 59!')

        next_dt = datetime.datetime(
            next_dt.year, next_dt.month, next_dt.day,
            next_dt.hour, next_dt.minute, seconds
        )

        # Minutes
        if _seconds != '*' and _minutes == '*':
            if from_dt.second > seconds:
                minutes = from_dt.minute + 1
                minutes = 0 if minutes == 60 else minutes
            elif from_dt.second <= seconds:
                minutes = from_dt.minute
        elif _seconds == '*' and _minutes == '*':
            minutes = from_dt.minute
        else:
            minutes = int(_minutes)
            if not (minutes >= 0 and minutes <= 59):
                raise Exception('Minute value must be between 0 and 59!')

        next_dt = datetime.datetime(
            next_dt.year, next_dt.month, next_dt.day,
            next_dt.hour, minutes, seconds
        )

        # Hours
        if  _minutes != '*' and _hours == '*':
            hours = from_dt.hour + 1
            hours = 0 if hours == 24 else hours
        elif _minutes == '*' and _hours == '*':
            hours = from_dt.hour
        else:
            hours = int(_hours)
            if not (hours >= 0 and hours <= 23):
                raise Exception('Hour value must be between 0 and 23!')

        next_dt = datetime.datetime(
            next_dt.year, next_dt.month, next_dt.day,
            hours, minutes, seconds
        )

        # Day Of Month and Day of Week
        if _hours != '*' and _day_of_month == '*':
            day_of_month = from_dt.day + 1
            day_of_month = 1 if day_of_month == 32 else day_of_month
        elif _hours == '*' and (_day_of_month == '*' or  _day_of_week == '*'):
            day_of_month = from_dt.day
        elif _day_of_month == '?' and '-' in _day_of_week:
            days_of_week = _day_of_week.split('-')
            next_day_of_week = self.adjust_cron_to_pydt(days_of_week[0])
            if next_day_of_week == from_dt.weekday():
                day_of_month = from_dt.day
            else:
                next_week_day_date = from_dt
                while next_week_day_date.weekday() != day_of_week:
                    next_week_day_date += datetime.timedelta(days=1)
                    day_of_month = next_week_day_date.day
        elif _day_of_month == '?' and _day_of_week in \
            ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']:
            day_of_week = {
                'mon': 0, 'tue': 1, 'wed': 2, 
                'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6
            }[_day_of_week]
            next_week_day_date = from_dt
            if day_of_week == from_dt.weekday():
                day_of_month = from_dt.day
            else:
                while next_week_day_date.weekday() != day_of_week:
                    next_week_day_date += datetime.timedelta(days=1)
                    day_of_month = next_week_day_date.day
        else:
            day_of_month = int(_day_of_month)
            hours = 0 if from_dt.hour == next_dt.hour else hours
            minutes = 0 if from_dt.minute == next_dt.minute else minutes
            # seconds = 0 if current_date.second == next_date.second else seconds
            seconds = 0
            if not (day_of_month >= 1 and day_of_month <= 31):
                raise Exception('Day of month value must be between 1 and 31!')

        next_dt = datetime.datetime(
            next_dt.year, next_dt.month, day_of_month,
            hours, minutes, seconds
        )

        # Month
        if _day_of_month == '?' and _month == '*':
            month = from_dt.month
        elif  _day_of_month != '*' and _month == '*':
            month = from_dt.month + 1
            month = 1 if month == 13 else month
        elif _day_of_month == '*' and _month == '*':
            month = from_dt.month
        else:
            month = int(_month)
            day_of_month = 1
            hours = 0 if from_dt.hour == next_dt.hour else hours
            minutes = 0 if from_dt.minute == next_dt.minute else minutes
            # seconds = 0 if current_date.second == next_date.second else seconds
            seconds = 0
            if not (month >= 1 and month <= 12):
                raise Exception('Month value must be between 1 and 12!')

        next_dt = datetime.datetime(
            next_dt.year, month, day_of_month,
            hours, minutes, seconds
        )

        # Year
        if  _month != '*' and _year == '*':
            year = from_dt.year + 1
            year = 1 if year == 9999 else year
        elif _month == '*' and _year == '*':
            year = from_dt.year
        else:
            year = int(_year)
            month = 1
            day_of_month = 1
            hours = 0 if from_dt.hour == next_dt.hour else hours
            minutes = 0 if from_dt.minute == next_dt.minute else minutes
            # seconds = 0 if current_date.second == next_date.second else seconds
            seconds = 0
            if not (year >= 1 and year <= 9999):
                raise Exception('Year value must be between 1 and 9999!')

        next_dt = datetime.datetime(
            year, month, day_of_month, 
            hours, minutes, seconds
        )

        return next_dt

    def adjust_cron_to_pydt(self, day: str) -> int:
        new_dw = int(day)-1
        if new_dw == -1:
            new_dw = 6
        return new_dw

if __name__ == '__main__':
    from_date = datetime.datetime(2023, 5, 10, 2, 0, 0)
    cron = Cronzun('20 * * * * ? *', from_date)
    next_date = cron.get_next_date()
    print('from date:', from_date)
    print('next date:', next_date)