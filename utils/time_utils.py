from datetime import datetime, timedelta


class DateTimeUtils:

    @classmethod
    def get_time(cls, string_format=False, **kwargs):
        date_time = datetime.now() + timedelta(**kwargs)
        if string_format:
            return cls.datetime_to_string(date_time)
        else:
            return date_time

    @staticmethod
    def datetime_to_string(date_time, format_date="%Y-%m-%d %H:%M:%S") -> str:
        return date_time.strftime(format_date)

    @staticmethod
    def string_to_datetime(date_string) -> datetime:
        date_string = date_string.replace("T", " ")
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def string_to_date(date_string) -> datetime:
        date_string = date_string.replace("T", " ")
        return datetime.strptime(date_string, '%Y-%m-%d')
