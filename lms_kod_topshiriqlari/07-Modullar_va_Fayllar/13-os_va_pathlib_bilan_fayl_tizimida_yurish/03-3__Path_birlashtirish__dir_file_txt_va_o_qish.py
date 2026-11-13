from pathlib import Path 
dir_name = input().strip()
filename = input().strip()
text = input()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
file_path = d / filename
file_path.write_text(text, encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))