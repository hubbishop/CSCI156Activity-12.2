__author__ = 'Dark-Knight'


def mean(*num):
    total = 0
    for i in num:
        total += i
    return total / len(num)
print(mean(2,4))
