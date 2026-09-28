DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт"]
FREE = "Вікно"

# Тривимірний масив: [3 групи][5 днів][4 пари]
# Заповнюємо базовими предметами
schedule = [[["Математика" for _ in range(4)] for _ in range(5)] for _ in range(3)]

# Додаємо кілька специфічних умов для перевірки:
schedule[0][1] = ["Фізика", FREE, "Історія", FREE]  # Група 1 у Вівторок має вікно
schedule[0][2][0] = "Програмування"                # Група 1, Середа, 1 пара
schedule[1][2][0] = "Програмування"                # Група 2, Середа, 1 пара (Спільна пара!)

print("\n==========================================")
print("=== 1. Найзавантаженіший день (Група 1) ===")
max_pairs = 0
busiest_day = ""

for d in range(5):
    # Рахуємо всі пари в день, де немає "Вікна"
    pairs = sum(1 for subject in schedule[0][d] if subject != FREE)
    if pairs > max_pairs:
        max_pairs = pairs
        busiest_day = DAYS[d]

print(f"Найбільше пар: у {busiest_day} ({max_pairs} пари)")


print("\n=== 2. Пошук днів із 'вікнами' ===")
for g in range(3):
    for d in range(5):
        day = schedule[g][d]
        # Перевіряємо, чи є Вільне вікно між 1-ю та 3-ю парою або 2-ю та 4-ю
        if (day[0] != FREE and day[1] == FREE and day[2] != FREE) or \
           (day[1] != FREE and day[2] == FREE and day[3] != FREE):
            print(f"Група {g + 1} має вікно у {DAYS[d]}")


print("\n=== 3. Перевірка на потокові заняття ===")
for d in range(5):
    for p in range(4):
        # Порівнюємо 1-шу та 2-гу групи
        sub1 = schedule[0][d][p]
        sub2 = schedule[1][d][p]
        if sub1 != FREE and sub1 == sub2:
            print(f"Потокова пара з предмету '{sub1}': {DAYS[d]}, {p + 1}-а пара")