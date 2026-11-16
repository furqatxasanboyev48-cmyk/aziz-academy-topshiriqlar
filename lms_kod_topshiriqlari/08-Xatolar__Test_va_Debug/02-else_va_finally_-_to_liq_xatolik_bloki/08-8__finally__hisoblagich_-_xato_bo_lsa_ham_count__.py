n = int(input())
success = 0
total = 0
for _ in range(n):
    s = input()
    try:
        int(s)
        success += 1
    except ValueError:
        pass
    finally:
        total += 1
print("success", success)
print("total", total)