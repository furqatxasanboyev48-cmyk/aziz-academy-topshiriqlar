class Config:
    theme = "light"
mode = input().strip()
if mode in ("CLASS", "INSTANCE"):
    obj = Config()
    if mode == "CLASS":
        Config.theme = "dark"
    else:
        obj.theme = "dark"
    print(f"CLASS={Config.theme} OBJ={obj.theme}")
else:
    print("BAD")