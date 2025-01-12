a: int = 5
b: str = 'строка'
c: list = [1,2]

def ident (s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(ident('1241223', 10))

