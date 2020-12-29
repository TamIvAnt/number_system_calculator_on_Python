# Функция выбора системы исчисления
def GetNumSystem():
    while True:
        numSystem = input('Выберите систему исчисления: BIN, OCT, DEC, HEX\n')
        if numSystem == 'BIN' or numSystem == '2':
            return 2
        elif numSystem == 'OCT' or numSystem == '8':
            return 8
        elif numSystem == 'DEC' or numSystem == '10':
            return 10
        elif numSystem == 'HEX' or numSystem == '16':
            return 16


# Функция перевода из двоичной системы
def ConvertFromBin(_value, _numSystem):
    if _numSystem == 2:
        return _value
    elif _numSystem == 8:
        return oct(int(_value, 2))
    elif _numSystem == 10:
        return int(_value, 2)
    elif _numSystem == 16:
        return hex(int(_value, 2))


# Функция перевода из восьмеричной системы
def ConvertFromOct(_value, _numSystem):
    if _numSystem == 2:
        return bin(int(_value, 8))[2:]
    elif _numSystem == 8:
        return _value
    elif _numSystem == 10:
        return int(_value, 8)
    elif _numSystem == 16:
        return hex(int(_value, 8))


# Функция перевода из десятичной системы
def ConvertFromDec(_value, _numSystem):
    if _numSystem == 2:
        return bin(int(_value))[2:]
    elif _numSystem == 8:
        return oct(int(_value))
    elif _numSystem == 10:
        return int(_value)
    elif _numSystem == 16:
        return hex(int(_value))


# Функция перевода из шестнадцатиричной системы
def ConvertFromHex(_value, _numSystem):
    if _numSystem == 2:
        return bin(int(_value, 16))[2:]
    elif _numSystem == 8:
        return oct(int(_value, 16))
    elif _numSystem == 10:
        return int(_value, 16)
    elif _numSystem == 16:
        return _value

def ConvertNumber():
    print('Исходная система исчисления:')
    fNumSystem = GetNumSystem()  # Получаем исходную систему исчисления
    value = input('Введите значение: ')  # Получаем исходное число
    print('Система исчисления в которую необходимо перевести число:')
    sNumSystem = GetNumSystem()  # Получаем систему исчисления в которую необходимо перевести
    if fNumSystem == 2:
        print(ConvertFromBin(value, sNumSystem))
    elif fNumSystem == 8:
        print(ConvertFromOct(value, sNumSystem))
    elif fNumSystem == 10:
        print(ConvertFromDec(value, sNumSystem))
    elif fNumSystem == 16:
        print(ConvertFromHex(value, sNumSystem))

def SumNumber():
    print('Cистема исчисления:')
    fNumSystem = GetNumSystem()
    value1 = input('Введите число: ')
    value2 = input('Введите второе число: ')

    if fNumSystem == 2:
        value_bin1 = int(value1, 2)
        value_bin2 = int(value2, 2)
        result = value_bin1 + value_bin2
        result_bin = bin(int(result))[2:]
        print(result_bin)

    elif fNumSystem == 8:
        value_oct1 = int(value1, 8)
        value_oct2 = int(value2, 8)
        result = value_oct1 + value_oct2
        result_oct = oct(int(result))[2:]
        print(result_oct)

    elif fNumSystem == 10:
        print(int( int(value1) + int(value2) ))

    elif fNumSystem == 16:
        value_hex1 = int(value1, 16)
        value_hex2 = int(value2, 16)
        result = value_hex1 + value_hex2
        result_hex = hex(int(result))[2:]
        print(result_hex)

def AwayNumber():
    print('Cистема исчисления:')
    fNumSystem = GetNumSystem()
    value1 = input('Введите число: ')
    value2 = input('Введите второе число: ')

    if fNumSystem == 2:
        value_bin1 = int(value1, 2)
        value_bin2 = int(value2, 2)

        if value_bin1 < value_bin2:
            result = value_bin2 - value_bin1
            result_bin = bin(int(result))[2:]
            print('-' + result_bin)
        else:
            result = value_bin1 - value_bin2
            result_bin = bin(int(result))[2:]
            print(result_bin)


    elif fNumSystem == 8:
        value_oct1 = int(value1, 8)
        value_oct2 = int(value2, 8)

        if value_oct1 < value_oct2:
            result = value_oct2 - value_oct1
            result_oct = oct(int(result))[2:]
            print('-' + result_oct)
        else:
            result = value_oct1 - value_oct2
            result_oct = oct(int(result))[2:]
            print(result_oct)


    elif fNumSystem == 10:
        print(int( int(value1) - int(value2) ))

    elif fNumSystem == 16:
        value_hex1 = int(value1, 16)
        value_hex2 = int(value2, 16)

        if value_hex1 < value_hex2:
            result = value_hex2 - value_hex1
            result_hex = hex(int(result))[2:]
            print('-' + result_hex)
        else:
            result = value_hex1 - value_hex2
            result_hex = hex(int(result))[2:]
            print(result_hex)


def ActionChoice():
    action_def = input('Что делаем: Переводим; Слогаем; Отнимаем;\n')

    if action_def == '1':
        ConvertNumber()
    elif action_def == '2':
        SumNumber()
    elif action_def == '3':
        AwayNumber()

def main():
    print('ВАС ПРЕВЕТСТВУЕТ КАЛЬКУЛЯТОР СС - TAMIVANT ')
    ActionChoice()


main()