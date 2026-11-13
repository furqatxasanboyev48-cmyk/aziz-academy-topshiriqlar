import os 
from pathlib import Path 
dir_name = input().strip()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
(d / "a.txt").write_text("a", encoding="utf-8")
(d / "b.txt").write_text("b", encoding="utf-8")
(d / "c.txt").write_text("c", encoding="utf-8")
os_soni = len(os.listdir(dir_name))
path_soni = len(list(d.iterdir()))
if os_soni == path_soni:
    print("YES")
else:
    print("NO")