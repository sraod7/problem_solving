def numberToWords(num: int) -> str:
    chunks = []
    while num > 0:
        chunks.append(num % 1000)
        num = num // 1000
    map_ = {
        0: '',
        1: 'thousand',
        2: 'million',
        3: 'billion'
    }

    map_2 = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        '100': 'hundred'
    }

    def convert_(val):
        ret = ''
        if val // 100 > 0:
            r = val // 100
            ret = map_2[str(r)] + ' ' + map_2['100']

        val = val % 100

        if val < 21:
            ret += ' ' + map_2[str(val)]
            return ret

        ret += ' ' + map_2[str((val // 10) * 10)]
        if val % 10 > 0:
            ret += ' ' + map_2[str(val % 10)]

        return ret

    res = ''

    while chunks:
        val = chunks.pop()
        res = res + ' ' + convert_(val) + ' ' + map_[len(chunks)]

    return res


print(numberToWords(1234567891))
