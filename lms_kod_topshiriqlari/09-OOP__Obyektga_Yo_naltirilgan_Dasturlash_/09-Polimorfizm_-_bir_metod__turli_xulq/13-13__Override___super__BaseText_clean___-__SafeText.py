class BaseText:
    def clean(self, text):
        return text.strip()
class SafeText(BaseText):
    def clean(self, text):
        t = super().clean(text)
        if not t:
            return None
        return t 
text = input()
result = SafeText().clean(text)
print(result if result else "BAD")