import random

# 1. Створюємо матрицю 3х4 з числами від 1 до 20
matrix = [[random.randint(1, 20) for _ in range(4)] for _ in range(3)]

print("=== Початкова матриця ===")
for row in matrix:
    print(row)

# ---------------------------------------------------------------------
# Завдання 1: Відняти від елементів кожної строки її середнє значення
print("\n=== 1. Відняли середнє арифметичне ===")
for row in matrix:
    avg = sum(row) / len(row)  # шукаємо середнє
    new_row = [round(x - avg, 1) for x in row]  # віднімаємо від кожного елемента
    print(new_row)

# ---------------------------------------------------------------------
# Завдання 2: Зсув матриці на k позицій вправо і вгору
k = 1
m = len(matrix)     # 3 строки
n = len(matrix[0])  # 4 стовпчики

shifted = [[0] * n for _ in range(m)]  # порожня матриця

for i in range(m):
    for j in range(n):
        new_i = (i - k) % m  # зсув вгору
        new_j = (j + k) % n  # зсув вправо
        shifted[new_i][new_j] = matrix[i][j]

print("\n=== 2. Зсув на 1 позицію вправо та вгору ===")
for row in shifted:
    print(row)

# ---------------------------------------------------------------------
# Завдання 3: Видалити рядки і стовпці, де є найбільше число
max_val = max(max(row) for row in matrix)  # найбільше число в матриці

bad_rows = set()
bad_cols = set()

# Шукаємо, в яких рядках і стовпцях стоїть максимум
for i in range(m):
    for j in range(n):
        if matrix[i][j] == max_val:
            bad_rows.add(i)
            bad_cols.add(j)

# Збираємо нову матрицю без них
cleaned_matrix = []
for i in range(m):
    if i in bad_rows:
        continue  # пропускаємо цей рядок
    new_row = [matrix[i][j] for j in range(n) if j not in bad_cols]
    cleaned_matrix.append(new_row)

print(f"\n=== 3. Матриця без максимумів (максимум = {max_val}) ===")
for row in cleaned_matrix:
    print(row)

# ---------------------------------------------------------------------
# Завдання 4: Обертання квадратної матриці 3х3 на 90 градусів (in-place)
sq_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n=== 4. Квадратна матриця ДО повороту ===")
for row in sq_matrix:
    print(row)

# Крок A: Міняємо рядки зі стовпчиками (транспонування)
for i in range(3):
    for j in range(i + 1, 3):
        sq_matrix[i][j], sq_matrix[j][i] = sq_matrix[j][i], sq_matrix[i][j]

# Крок B: Перевертаємо кожен рядок навпаки
for row in sq_matrix:
    row.reverse()

print("\n=== Квадратна матриця ПІСЛЯ повороту на 90° ===")
for row in sq_matrix:
    print(row)