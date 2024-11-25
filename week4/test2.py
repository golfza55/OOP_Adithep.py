a = int(input("ใส่เลข : "))
i = 1

while i < 25:
    ans = a * i
    if a / 2 % 2 != 0:
        print(f"{a} x {i} = {ans}")
    i += 1