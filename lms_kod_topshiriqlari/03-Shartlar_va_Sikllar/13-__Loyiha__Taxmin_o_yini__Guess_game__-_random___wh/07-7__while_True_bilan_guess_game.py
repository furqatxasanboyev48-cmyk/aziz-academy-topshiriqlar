secret = 9
while True:
     g = int(input())
     if g == secret:
        print("Correct")
        break
     elif g < secret:
        print("Low")
     else:
        print("High")
        
        