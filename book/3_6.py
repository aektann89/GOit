invited_guests = ["serhiy", "andrii", "petro"]

print(f"{invited_guests[0].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")
print(f"{invited_guests[1].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")
print(f"{invited_guests[2].title()}, запрошуємо Вас на вечірку на честь свята Hellowin")

print(f"Сталася прикра подія, {invited_guests[0].title()} не зможе прийти на вечірку")
invited_guests[0] = 'illa'
print(f"Тому замість нього запрошується - {invited_guests[0].title()}")

print(f"Шановні гості: {invited_guests[0].title()}, {invited_guests[1].title()}, {invited_guests[2].title()}. Повидомляємо Вам що ми знайшли більший стіл!")
invited_guests.insert(0, 'taras')
invited_guests.insert(2, 'mikola')
print(f"Тому запрошуємо на вечірку також - {invited_guests[0].title()} та {invited_guests[2].title()}")