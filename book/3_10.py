country = ["Egypt", "Italy", "Bulgaria", "Ireland", "India", "Albania", "Brazil", "Hungary", "Greece", "Mexico", "Serbia", "Slovenia", "United Kingdom ", "Poland",]

print(f"Всього {len(country)} країн")
print(f"Список країн: - {country} ")
print(f"Сортований але не змінений список країн: - {sorted(country)}")
print(f"Сортований в зворотньому порядку але не змінений список країн: - {sorted(country, reverse=True)}")
country.reverse()
print(f"Реверсивний список країн: - {country}")