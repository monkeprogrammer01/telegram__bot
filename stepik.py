digits = [43, 5189, 53, 214, 98, 18, 4012, 601, 45, 520]

summa = 0

for i in range(0, len(digits), 3):

    while digits[i] >0:

        summa = summa + digits[i] % 10

        digits[i] = digits[i] // 10
        print("eto summa ",summa)
        print('eto digits', digits)
        print('eto digit[i]', digits[i])

print(summa )