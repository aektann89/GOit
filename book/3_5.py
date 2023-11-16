invited_guests = ["serhiy", "andrii", "petro"]

print(f"{invited_guests[0].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")
print(f"{invited_guests[1].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")
print(f"{invited_guests[2].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")

print(f"Сталася прикра подія, {invited_guests[0].title()} не зможе прийти на вечірку")
invited_guests[0] = 'illa'
print(f"Тому замість нього запрошується - {invited_guests[0].title()}")