import graphics.graphics_3d.cuboid as cub
import graphics.graphics_3d.sphere as sph
import graphics.circle as circ
import graphics.rectangle as rect

radius = int(input("Enter the radius of the circle:"))

print("area of the circle is:",circ.circle(radius))

len = int(input("Enter the length  of the rectangle:"))
bth = int(input("Enter the breadth of the rectangle"))
print("area of the rectangle  is:",rect.rectangle(len,bth))

print("perimeter  of the rectangle  is:",rect.rectperimeter(len,bth))

