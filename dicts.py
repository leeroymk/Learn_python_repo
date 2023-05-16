dct: dict = {
    'city': 'Москва',
    'temperature': '20',
}

print(dct['city'])

dct['temperature'] = str(int(dct['temperature']) - 5)

print(dct)

print(dct.get('country', 'There is no such key'))

print(dct.get('country', 'Россия'))

dct['date'] = '27.05.2019'

print(len(dct))
