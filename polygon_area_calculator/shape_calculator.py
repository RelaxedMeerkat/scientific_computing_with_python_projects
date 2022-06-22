class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width <= 50 and self.width <= 50:
            picture = ""
            for i in range(0,self.height):
                picture += self.width * "*" + "\n"
        else:
            picture = "Too big for picture."
        return picture

    def get_amount_inside(self, polygon):
        polygon_area = polygon.get_area()
        this_area = self.get_area()
        return this_area // polygon_area
# class end

class Square(Rectangle):
    def __init__(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, size):
        self.width = size
        self.height = size

    def set_width(self, size):
        self.set_side(size)

    def set_height(self, size):
        self.set_side(size)
# class end
