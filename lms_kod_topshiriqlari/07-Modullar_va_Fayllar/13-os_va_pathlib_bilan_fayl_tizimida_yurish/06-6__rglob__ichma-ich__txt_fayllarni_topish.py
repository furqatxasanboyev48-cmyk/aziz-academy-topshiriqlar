from pathlib import Path 
root = Path(input().strip())
sub = root / "sub"
sub.mkdir(parents=True, exist_ok=True)
(root / "a.txt").write_text("a", encoding="utf-8")
(sub /"b.txt").write_text("b", encoding="utf-8")
(sub/ "c.txt").write_text("c", encoding="utf-8")
total = 0
for p in root.rglob("*.txt"):
    total += 1
print(total)
