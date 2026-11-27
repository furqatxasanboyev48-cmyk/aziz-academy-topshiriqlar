class Logger:
    def log(self, msg):
        return f"LOG:{msg}"
class TimeLogger(Logger):
    def log(self, msg):
        return "[T] " + super().log(msg)
msg = input().strip()
if msg:
    print(TimeLogger().log(msg))
else:
    print("BAD")