class Serializer:
    def serialize(self, s):
        return s.strip()
class JsonSerializer(Serializer):
    def serialize(self, s):
        t = super().serialize(s)
        if not t:
            return None
        return '{"v":"' + t + '"}'
s = input()
result = JsonSerializer().serialize(s)
print(result if result else "BAD")
        
    