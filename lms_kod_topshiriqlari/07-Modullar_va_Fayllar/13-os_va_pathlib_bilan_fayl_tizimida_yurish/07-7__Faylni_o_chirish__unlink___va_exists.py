from pathlib import Path 
dir_name = input().strip()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
fayl = d/"x.txt"
fayl.write_text("x", encoding="utf-8")
fayl.unlink()
if fayl.exists():
    print("NOT")
else:
    print("DELETED")