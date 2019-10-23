def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr1 = [arr[0]]
        for i in range(1, n):
            arr1.append(arr1[i-1] + arr[i])
        (yb, mb, db) = map(int, input().split())
        (yc, mc, dc) = map(int, input().split())

        if mb == 1:
            late_birth = db
        else:
            late_birth = arr1[mb-2] + db

        if mc == 1:
            extra_date = dc
        else:
            extra_date = arr1[mc-2] + dc

        no_days = (yc-yb)*arr1[-1] + 1
        no_days += extra_date
        no_days -= late_birth
        leep = yc//4 - yb//4
        if yb%4==0:
            leep += 1
        if yc%4 == 0:
            leep -= 1

        print(no_days+leep)


if __name__ == "__main__":
    main()
