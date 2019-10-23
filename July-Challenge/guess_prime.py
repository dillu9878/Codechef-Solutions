import sys
import math


def main():
    t = int(input())
    for _ in range(t):
        x = 31623
        print(1, x, flush=True)
        mod1 = int(input())
        num = 1000014129
        kp = num - mod1
        x2 = 31624
        print(1, x2, flush=True)
        mod2 = int(input())
        num1 = 1000077376
        kp2 = num1 -mod2
        p = math.gcd(kp, kp2)
        print(2, p, flush=True)
        inp3 = input()
        if inp3 is not 'Yes':
            break


if __name__== '__main__':
    main()