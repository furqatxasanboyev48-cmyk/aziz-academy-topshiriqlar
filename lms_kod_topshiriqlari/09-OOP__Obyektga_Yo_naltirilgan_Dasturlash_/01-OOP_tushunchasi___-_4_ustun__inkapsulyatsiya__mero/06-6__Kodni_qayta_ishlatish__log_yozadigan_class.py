class LoggerMixin:
    def log(self, msg):
        print(f"LOG:{msg}")
class Service(LoggerMixin):
    def run(self, action):
        self.log(action)
        print("DONE")
action = input().strip()
if action:
    Service().run(action)
else:
    print("BAD")
    