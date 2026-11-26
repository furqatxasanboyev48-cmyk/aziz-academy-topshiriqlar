class Text:
    def __init__(self, s):
        self.s = s 
    def render(self):
        return self.s
class BoldText(Text):
    def render(self):
        return "**" + super().render() + "**"
print(BoldText(input()).render())