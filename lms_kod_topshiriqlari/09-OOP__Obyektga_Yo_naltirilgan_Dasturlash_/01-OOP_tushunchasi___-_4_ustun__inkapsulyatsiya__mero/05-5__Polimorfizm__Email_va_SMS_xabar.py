class BaseNotifier:
    def send(self, to, msg):
        raise NotImplementedError
class EmailNotifier(BaseNotifier):
    def send(self, to, msg):
        return f"EMAIL->{to}: {msg}"
class SmsNotifier(BaseNotifier):
    def send(self, to, msg):
        return f"SMS->{to}: {msg}"
kind = input().strip()
to = input().strip()
msg = input().strip()
notifiers = {"EMAIL": EmailNotifier(), "SMS": SmsNotifier()}
if kind in notifiers and to and msg:
    print(notifiers[kind].send(to, msg))
else:
    print("BAD")
        