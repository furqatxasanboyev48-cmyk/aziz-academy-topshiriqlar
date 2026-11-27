class Formatter:
    def format(self, text):
        return text.strip()
class UpperFormatter(Formatter):
    def format(self, text):
        return super().format(text).upper()
class LowerFormatter(Formatter):
    def format(self, text):
        return super().format(text).lower()
kind = input().strip()
text = input().strip()
classes = {"UP": UpperFormatter, "LOW": LowerFormatter}
if kind in classes and text:
    print(classes[kind]().format(text))
else:
    print("BAD")
    
    
    
    
    
    
    
    
    
    
    
    
    