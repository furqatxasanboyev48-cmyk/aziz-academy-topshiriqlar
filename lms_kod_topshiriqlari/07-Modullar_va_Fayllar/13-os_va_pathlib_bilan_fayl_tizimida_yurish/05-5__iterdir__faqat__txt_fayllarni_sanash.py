from pathlib import Path 
dir_name = input().strip()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
(d/"a.txt").write_text("a", encoding="utf-8")
(d/"b.txt").write_text("b", encoding="utf-8")
(d / "c.md").write_text("c", encoding="utf-8")
txt_count = 0
for p in d.iterdir():
    if p.suffix == ".txt":
        txt_count += 1
print(txt_count)