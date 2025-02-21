class Point:
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def add(self,another_point):
        self.x += another_point.x
        self.y += another_point.y
        self.z += another_point.z

    def show(self):
        print(f"({self.x},{self.y},{self.z})")