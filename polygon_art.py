import random
import turtle

class Polygon:
    def __init__(self,num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()


class EmbeddedPolygon(Polygon):
    def __init__(self,num_sides, size, orientation, location, color, border_size,
                 reduction_ratio, num_embedded):
        self.reduction_ratio = reduction_ratio
        self.num_embedded = num_embedded
        super().__init__(num_sides, size, orientation, location, color, border_size)

    def draw(self):
        for i in range(3):
            super().draw()

            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= self.reduction_ratio
            turtle.penup()

class Run:
    def __init__(self):
        self.choice = 0
        self.reduction_ratio = 0.618
        self.num_embedded = 3

    def art(self):
        art = int(input("Which art do you want to generate?"
                              " Enter a number between 1 to 9 inclusive: "))
        if art not in range(1, 10):
            raise ValueError("Invalid art number")
        else:
            self.choice = art

    def randat(self):
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)

    def run(self):
        for _ in range(20):
            self.randat()
            shape = None

            # Choose shape based on the user's choice
            if self.choice == 1:
                shape = Polygon(3, self.size, self.orientation, self.location, self.color, self.border_size)
            elif self.choice == 2:
                shape = Polygon(4, self.size, self.orientation, self.location, self.color, self.border_size)
            elif self.choice == 3:
                shape = Polygon(5, self.size, self.orientation, self.location, self.color, self.border_size)
            elif self.choice == 4:
                shape = Polygon(random.randint(3, 5), self.size, self.orientation, self.location, self.color,
                                self.border_size)
            elif self.choice == 5:
                shape = EmbeddedPolygon(3, self.size, self.orientation, self.location, self.color, self.border_size,
                                        self.reduction_ratio, self.num_embedded)
            elif self.choice == 6:
                shape = EmbeddedPolygon(4, self.size, self.orientation, self.location, self.color, self.border_size,
                                        self.reduction_ratio, self.num_embedded)
            elif self.choice == 7:
                shape = EmbeddedPolygon(5, self.size, self.orientation, self.location, self.color, self.border_size,
                                        self.reduction_ratio, self.num_embedded)
            elif self.choice == 8:
                shape = EmbeddedPolygon(random.randint(3, 5), self.size, self.orientation, self.location, self.color,
                                        self.border_size, self.reduction_ratio, self.num_embedded)
            elif self.choice == 9:
                if random.randint(0, 1) == 0:
                    shape = Polygon(random.randint(3, 5), self.size, self.orientation, self.location, self.color,
                                    self.border_size)
                else:
                    shape = EmbeddedPolygon(random.randint(3, 5), self.size, self.orientation, self.location,
                                            self.color, self.border_size, self.reduction_ratio, self.num_embedded)

            if shape:
                shape.draw()

        turtle.update()
        turtle.done()



run = Run()
run.art()

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

run.run()