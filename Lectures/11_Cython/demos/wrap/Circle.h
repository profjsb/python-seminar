namespace geom {
    class Circle {
    public:
        Circle(double x, double y, double r);
        ~Circle();
        double getX();
        double getY();
        double getRadius();
        double getArea();
        void setCenter(double x, double y);
        void setRadius(double r);
    private:
        double x;
        double y;
        double r;
    };
}
