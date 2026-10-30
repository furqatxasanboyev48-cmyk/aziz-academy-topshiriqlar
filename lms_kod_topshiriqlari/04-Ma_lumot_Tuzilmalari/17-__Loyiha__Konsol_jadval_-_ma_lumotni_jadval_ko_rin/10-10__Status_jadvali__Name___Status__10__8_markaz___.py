n = int(input())
for _ in range(n):
    name, flag = input().split()
    if flag == "1":
        status = "present"
    else:
        status = "absent"
    print("{}|{}".format(name, status))