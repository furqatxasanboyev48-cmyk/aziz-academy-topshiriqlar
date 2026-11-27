class Notifier:
    def send(self, to, msg):
        raise NotImplementedError
class EmailNotifier(Notifier):
    def send(self, to, msg):
        return f"EMAIL->{to}: {msg}"
class SmsNotifier(Notifier):
    def send(self, to, msg):
        return f"SMS->{to}: {msg}"
kind = input().strip()
to = input().strip()
msg = input().strip()
classes = {"EMAIL": EmailNotifier, "SMS": SmsNotifier}
if kind in classes and to and msg:
    print(classes[kind]().send(to, msg))
else:
    print("BAD")