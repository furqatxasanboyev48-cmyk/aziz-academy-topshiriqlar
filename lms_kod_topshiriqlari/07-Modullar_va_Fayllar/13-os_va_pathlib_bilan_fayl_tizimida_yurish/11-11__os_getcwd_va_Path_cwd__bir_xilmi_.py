import os 
from pathlib import Path 
if os.getcwd() == str(Path.cwd()):
    print("YES")
else:
    print("NO")