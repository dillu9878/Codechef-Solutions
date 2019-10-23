def main():
    for _ in range(int(input())):
        (x, y,z) = map(int,  input().split())
        # x = a- b
        # y = b-c
        # z = c-a
        # y + z = b - a
        # x - y - z =  