from pathlib import Path 
root = Path(input().strip())
sub = root / "sub"
sub.mkdir(parents=True, exist_ok=True)
(root / "a.txt").write_text("abc", encoding="utf-8")
(root / "b.md").write_text("xxxx", encoding="utf-8")
(sub /"c.txt").write_text("hello", encoding="utf-8")
total_size = 0
for p in root.rglob("*.txt"):
    total_size += p.stat().st_size
print(total_size)



