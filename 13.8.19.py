price = 0
while True:
    try:
        ticket_amount = input('Сколько билетов вы хотите приобрести? ')
        ticket_amount = int(ticket_amount)
        if type(ticket_amount) == int:
            break
    except ValueError:
        print('Введите целое число.')
for i in range(ticket_amount):
    i = i + 1
    while True:
        try:
            age_for_ticket = input(f'Для какого возраста билет №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный.')
            elif 25 > age_for_ticket >= 18:
                price = price + 990
                print('Стоимость билета: 990 руб.')
            else:
                price = price + 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число.')
if ticket_amount > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом 10%-ой скидки.')
else:
    print(f'Сумма к оплате {price} руб.')
