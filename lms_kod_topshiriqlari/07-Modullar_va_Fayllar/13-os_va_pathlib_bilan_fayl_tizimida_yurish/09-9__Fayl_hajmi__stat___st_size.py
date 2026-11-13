from pathlib import Path 
dir_name = input().strip()
text = input()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
fayl = d/"a.txt"
fayl.write_text(text, encoding="utf-8")
print(fayl.stat().st_size)