from datetime import timedelta

def is_year_vs(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return delta = timedelta(days=366)
    return delta = timedelta(days=365)

# это я еще не знал про функцию isleap() из модуля calendar))