array = [
    "Курс 1",
    "Курс 2",
    "Курс 3",
    "Курс 4",
    "Курс 5",
    "Курс 6",
    "Курс 7",
    "Курс 8",
    "Курс 9",
    "Курс 10",
]

n = ''
arrayout = []

def grouped(array, n):
    if n == '':
        n = 3
        grouped(array,n)

    else:
        for i in range(0, len(array), n):
            arrayout.append(array[i:i+n])
        print(arrayout)

grouped(array,n)

