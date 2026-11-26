class Logger:
    def log(self, msg):
        return f"LOG: {msg}"
class TimeLogger(Logger):
    def log(self, msg):
        return "[time] " + super().log(msg)
print(TimeLogger().log(input()))    