
import graphics.circle as circ
import graphics.rectangle as rect
from graphics.graphics_3d import cuboid,sphere

radius = int(input("Enter the radius of the circle:"))

print("area of the circle is:",circ.circle(radius))

len = int(input("Enter the length  of the rectangle:"))
bth = int(input("Enter the breadth of the rectangle"))
print("area of the rectangle  is:",rect.rectangle(len,bth))

print("perimeter  of the rectangle  is:",rect.rectperimeter(len,bth))

l1=int(input("Enter the length of the cuboid :"))
b1=int(input("Enter the breadth of the cuboid :"))
h1=int(input("Enter the height of the cuboid :"))
cuboid.areacub(l1,b1,h1)
cuboid.pericub(l1,b1,h1)
r1=int(input("Enter the raduis of the sphere:"))
sphere.areas(r1)
sphere.peris(r1)