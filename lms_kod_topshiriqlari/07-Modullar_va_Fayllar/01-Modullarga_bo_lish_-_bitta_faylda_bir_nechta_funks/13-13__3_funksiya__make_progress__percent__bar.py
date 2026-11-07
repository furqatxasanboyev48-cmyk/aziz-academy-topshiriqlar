def percent(done, total):
    return done * 100 // total
def bar(p):
    return "%" * (p // 10) + "." * (10 - p // 10)
def make_progress(done, total):
    p = percent(done, total)
    return str(p) + "% " + bar(p)
done, total = map(int, input().split())
print(make_progress(done, total), end="")