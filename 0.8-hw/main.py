from datetime import date, datetime, timedelta
def get_birthdays_per_week(users: list) -> dict:
    # Перевірка якщо не передано user
    if not users:
        return {}
    CURRENT_DATE = date.today()
    WEEKDAYS = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    birthdays_per_week = {day: [] for day in WEEKDAYS.values()} # Словник днів народження на тиждень
    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_next = birthday.replace(CURRENT_DATE.year)
        # Перевірка на минулий день народження
        if birthday_next < CURRENT_DATE:
            birthday_next = birthday_next.replace(year=CURRENT_DATE.year + 1)
        # Перевірка на потряпляння дати напродження на натупний тиждень
        if CURRENT_DATE <= birthday_next <= CURRENT_DATE + timedelta(days=7):
            day_of_week = birthday_next.weekday()
            name_of_day = WEEKDAYS[day_of_week] # Ім’я дня тижня
        # Перевірка на потряпляння дня народження user на вихідний день, якщо ТАК то переносимо на понеділок
            if name_of_day in ['Saturday', 'Sunday']:
                name_of_day = 'Monday'
            birthdays_per_week[name_of_day].append(name)
    return {day: names for day, names in birthdays_per_week.items() if names}
if __name__ == '__main__':
    users = [
        {'name': 'Jan Koum', 'birthday': datetime(1976, 1, 1).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")