n = int(input())
log = open("log10.txt", "w")
for _ in range(n):
    s = input()
    try:
        int(s)
        status = "OK"
    except ValueError:
        status = "ERR"
    finally:
        log.write(status + "\n")
log.close()
err_count = 0
with open("log10.txt") as f:
    for line in f:
        if line.strip() == "ERR":
            err_count += 1
print(err_count)