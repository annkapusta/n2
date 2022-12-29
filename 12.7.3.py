per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))

TBC = round(per_cent['ТКБ'] / 100 * money)
SKB = round(per_cent['СКБ'] / 100 * money)
VTB = round(per_cent['ВТБ'] / 100 * money)
SBER = round(per_cent['СБЕР'] / 100 * money)

#print(TBC,",", SKB,",", VTB,",", SBER)

max_number = max(TBC, SKB, VTB, SBER)
print("Максимальная сумма, которую вы можете заработать —", max_number)