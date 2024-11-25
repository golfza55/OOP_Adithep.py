a = int(input("ใส่เลข : "))
for i in range(1,25,1):
    ans = a*i
    if a /2 % 2 != 0 :
            print(f"{a}x{i}={ans}")