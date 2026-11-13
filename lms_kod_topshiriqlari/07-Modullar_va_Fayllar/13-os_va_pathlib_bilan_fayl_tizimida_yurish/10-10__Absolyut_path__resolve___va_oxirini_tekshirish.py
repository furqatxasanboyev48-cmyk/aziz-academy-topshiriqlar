from pathlib import Path 
dir_name = input().strip()
filename = input().strip()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
fp = d / filename
yol = str(fp.resolve())
if yol.endswith("/" + dir_name + "/" + filename):
    print("YES")
else:
    print("NO")

