class A:

    def __init__(self):
        self.x =7

class B(A):

    def __init__(self):
        super().__init__()
        self.y = self.x + 5

print(B().y)

b = B()
print(b.y)