from pathlib import Path 
dir_name = input().strip()
filename = input().strip()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
fp = d / filename
fp.write_text("x", encoding="utf-8")
if d.is_dir():
    print("DIR")
else:
    print("NO")
if fp.is_file():
    print("FILE")
else:
    print("NO")