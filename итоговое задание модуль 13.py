ticket = None
while not ticket:
    while not ticket and ticket != 0:
        try:
            ticket = int(input("Введите кол-во билетов: "))
        except ValueError:
            print("Введите целое число!")
    if ticket <= 0:
        print("Введите число больше нуля!")
i_age = None
t_sum = 0
for age in range(1, ticket+1):
    while not i_age and i_age != 0:
        while not i_age and i_age != 0:
            try:
                i_age = int(input("Введите возраст: "))
            except ValueError:
                print("Введите целое число!")
        if i_age < 0 or i_age > 120:
            print("Введите возраст от 0 до 120 лет!")
            i_age = None
    if 18 <= i_age < 25:
        t_sum = t_sum + 990
    elif i_age >= 25:
        t_sum = t_sum + 1390
    i_age = None
if ticket > 3:
    print(f"Полная стоимость билетов {t_sum}")
    t_sum = t_sum * 0.9
    print(f"Стоимость билетов со скидкой {t_sum}")
else: print(f"Стоимость билетов {t_sum}")
