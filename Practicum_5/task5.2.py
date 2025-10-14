import turtle as trt

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

if (xc - x) ** 2 + (yc - y) ** 2 < r ** 2:
    print("Точка внутри окружности.")
elif (xc - x) ** 2 + (yc - y) ** 2 == r ** 2:
    print("Точка на окружности")
else:
    print("Точка вне окружности.")

trt.up()
trt.setposition(xc, yc - r)
trt.down()
trt.circle(r)
trt.up()
trt.setposition(x, y)
trt.down()
trt.dot(10)
trt.done()
print('\n')