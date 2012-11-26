#include "Circle.h"
#include <math.h>

using namespace geom;

Circle::Circle(double x, double y, double r)
{
    this->x = x;
    this->y = y;
    this->r = r;
}

double Circle::getX() {
    return x;
}

double Circle::getY() {
    return y;
}

double Circle::getRadius() {
    return r;
}

double Circle::getArea() {
    return M_PI * r * r;
};

void Circle::setCenter(double x, double y) {
    this->x = x;
    this->y = y;
}

void Circle::setRadius(double r) {
    this->r = r;
}

Circle::~Circle() {
}
