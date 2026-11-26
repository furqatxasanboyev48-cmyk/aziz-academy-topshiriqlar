class LoggerBase:
    def log(self, msg):
        return f"LOG:{msg}"
class FileLogger(LoggerBase):
    def log(self, msg):
        return "FILE-" + super().log(msg)
msg = input().strip()
if msg:
    print(FileLogger().log(msg))
else:
    print("BAD")
                
                
                
                
                
                
                
                
                
                
                
                
                
