s = input()
with open("w7_src.txt", "w", encoding="utf-8") as f:
    f.write(s)
with open("w7_src.txt", "r", encoding="utf-8") as f:
    kontent = f.read()
with open("w7_dst.txt", "w", encoding="utf-8") as f:
    f.write(kontent)
with open("w7_dst.txt", "r", encoding="utf-8") as f:
    print(f.read())
    
    
    
    