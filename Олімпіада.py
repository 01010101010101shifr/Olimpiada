u = "0"
a = "250"
b = "210"
print('Тест на олімпіаду')
r = input('Готова/ий? ')
if r == 'Так':
    print('Скільки 250 + 210')
c = "460"
v = input('Відповідь: ')
if v == c:
    print('Молодець, вірно!')
    u = u + "1"
    
else:
    print('Ні! Буде 460!')
print('Степінь многочлена (4a^4)+(4a^10)')
c2 = "10"
v2 = input('Відповідь: ')
if v2 == c2:
    print('Вірно!')
    u = u + "1"
    
else:
    print('Ні, це ж 10!')
print('Кут 1 = 128*. Скільки дорівнює суміжний кут до нього?(Відповідь писати тільки цифрами, без літер та символів)')
c3 = "52"
v3 = input('Відповідь: ')
if v3 == c3:
    print('Правильно!')
    u = u + "1"
else:
    print('От халепа!')
print('1^20190')
c4 = "1"
v4 = input('Відповідь: ')
if v4 == c4:
    print('Файно')
    u = u + "1"
else:
    print('Байка з тим')
print('x^2 * x^8')
c5 = "x^10"
v5 = input('Відповідь: ')
if v5 == c5:
    print('Крутяк!')
    u = u + "1"
else:
    print('Що є?')
print('Знайдіть площу прямокутника одна зі сторін якого дорівнює 0.1323 м та менша за іншу на 5.52 см. Відповідь подати у метрах квадратних.')
c6 = "0.0248"
v6 = input('Відповідь: ')
if v6 == c6:
    print('Вауві!')
    u = u + "1"
else:
    print('YAKTAK?')
print('70! / 69!')
c7 = "70"
v7 = input('Відповідь: ')
if v7 == c7:
    print('Розумом!')
    u = u + "1"
else:
    print('Значить так?!')
print('Катет 1 = 21см. Катет 2 = 35 см. Назвіть довжину Гіпотенузи. Відповідь подайте в метрах і без одиниць вимірювання')
c8 = "40.82"
v8 = input('Відповідь: ')
if v8 == c8:
    print('Вав!')
    u = u + "1"
else:
    print('Чево?')
print('458 - x^3 = 5!. Відповідь подати в форматі: a√b')
c9 = "3√338"
v9 = input('Відповідь: ')
if v9 == c9:
    print('Ні#іга собі!!')
    u = u + "1"
else:
    print('М-да(')
print('2√104976. Відповідь подати в такому-ж форматі.')
cs = "324"
vs = input('Відповідь: ')
if vs == cs:
    print('ОГО!')
    u = u + "1"
else:
    print('Game Over')
if u > 5:
    print(u'/10. Ти у II етапі!')
else:
    print(u'/10. Нажаль, ви не пройшли(')
print('Дякую за роботу!')