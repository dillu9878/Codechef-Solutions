def main():
    (n, q) = map(int, input().split())
    d = {}
    for _ in range(n-1):
        (xi, yi) = map(int, input().split())
        if xi not in d:
            d[xi].append(yi)
        else:
            d[xi] = [yi]
        if yi in d:
            d[yi].append(xi)
        else:
            d[yi] = [xi]
    arr = list(map(int, input().split()))
