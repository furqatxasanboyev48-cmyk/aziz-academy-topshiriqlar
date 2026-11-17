score = int(input())
try:
    if score < 0 or score > 100:
        raise ValueError("oraliqdan tashqari")
except ValueError:    
    print("OUT")
else:
    print("OK")