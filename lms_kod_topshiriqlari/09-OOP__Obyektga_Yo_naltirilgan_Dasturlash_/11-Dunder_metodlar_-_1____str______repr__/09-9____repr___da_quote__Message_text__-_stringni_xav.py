class Message:
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return f"Message(text={self.text!r})"
text = input().strip()
if text:
    print(repr(Message(text)))
else:
    print("BAD")