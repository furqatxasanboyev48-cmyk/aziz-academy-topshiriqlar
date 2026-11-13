from pathlib import Path 
dir_name = input().strip()
text1 = input()
text2 = input()
d = Path(dir_name)
d.mkdir(parents=True, exist_ok=True)
(d/"a.txt").write_text(text1, encoding="utf-8")
(d/ "b.txt").write_text(text2, encoding="utf-8")
son = 0
for p in d.iterdir():
    if p.is_file():
        son += 1
print(son)
    