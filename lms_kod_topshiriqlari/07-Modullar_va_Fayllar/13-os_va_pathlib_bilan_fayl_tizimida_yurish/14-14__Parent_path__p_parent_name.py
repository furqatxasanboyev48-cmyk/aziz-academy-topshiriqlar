from pathlib import Path 
dir_name = input().strip()
filename = input().strip()
p = Path(dir_name) / filename
print(p.parent.name)