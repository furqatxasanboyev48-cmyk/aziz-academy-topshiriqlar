from pathlib import Path 
dir_name = input().strip()
text = input()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
old = d/"old.txt"
old.write_text(text, encoding="utf-8")
new = d/"new.txt"
old.rename(new)
print(new.read_text(encoding='utf-8'))