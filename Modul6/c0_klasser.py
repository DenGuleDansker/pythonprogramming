class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def moved(self, dx, dy):
        return Point(self._x + dx, self._y + dy)

p = Point(3, 4)
print(p.moved(3, 8))
print(Point.moved(p, 3, 8))  

print(Point.x) # <function Point.x at 0x0000029...F60>
print(p.x) # <bound method Point.x of <__main__.Point object at 0x0000028...BA0>>
print(p.x()) # 3
print(Point.x(p)) # 3
print(p.y()) # 12

p = p.moved(3,8)
print(p.x()) # 6
print(Point.x(p)) # 6
print(p.y()) # 12
print(Point.y(p)) #12 
