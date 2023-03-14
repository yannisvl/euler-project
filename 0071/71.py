from fractions import Fraction
import math

min = 1
for paronomasths in range(1000000, 7, -1):
    arithmhths = (paronomasths * 3 - 1)// 7
    c = Fraction(arithmhths, paronomasths)
    temp = c._numerator
    diafora = 3/7 - c
    if diafora < min and diafora!=0:
        min = diafora
        result = temp
        print(result, paronomasths)
print('71 finished')