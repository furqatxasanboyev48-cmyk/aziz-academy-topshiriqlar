from pathlib import Path 
path_str = input()
print(len(Path(path_str).parts))