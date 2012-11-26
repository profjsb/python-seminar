#include "Circle.h"
#include <iostream>

int main() {
    geom::Circle c = geom::Circle(0, 0, 1);

    std::cout << "Created new circle with center (" \
         << c.getX() << "," << c.getY() << "), radius " \
         << c.getRadius() << " and area "         \
         << c.getArea() << std::endl;

    return 0;
}
