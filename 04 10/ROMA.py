'''
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

LVIII - 58
MCMXCIV - 1994 
'''

def romamToint(roman):
    roman_nunbers = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    roman = list(roman)
    roman.reverse()
    result = 0
    previus = 0

    for char in roman:
        value = roman_nunbers[char]
        if value < previus:
            result -= value
        else:
            result += value

        previus = value

    return result

print(romamToint('XIV')) #14
print(romamToint('MCMXCIV')) #1994
pergunta = input("digite um número em romano: ")
if pergunta != list:
    print('insira apenas números romanos! ')


print(romamToint(pergunta))









