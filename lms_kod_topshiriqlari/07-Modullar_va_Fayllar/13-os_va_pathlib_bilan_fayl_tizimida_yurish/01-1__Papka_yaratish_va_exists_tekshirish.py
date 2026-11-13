from pathlib import Path 
name = input().strip()
p = Path(name)
p.mkdir(parents=True, exist_ok=True)
if p.exists():
    print("YES")
else:
    print("NO")