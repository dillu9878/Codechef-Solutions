def rec(n):
    if n == 1:
        return 1
    c = n
    return c + rec(n)

def main():
    rec(100)