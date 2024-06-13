import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the maximum

# Function to draw a single triangle
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Function to draw nested triangles with rotation around the fixed center
def draw_nested_triangles(num_triangles, initial_size, step_size, rotation_angle):
    for i in range(num_triangles):
        size = initial_size + i * step_size
        pen.penup()
        # Calculate the centroid offset for the current size
        centroid_y = -size * (math.sqrt(3) / 6)
        pen.goto(0, 0)  # Move to the original center
        pen.setheading(0)
        pen.goto(pen.xcor(), pen.ycor() + centroid_y)
        pen.setheading(rotation_angle * i)  # Rotate for the next triangle
        pen.pendown()
        draw_triangle(size)
        pen.penup()
        pen.goto(0, 0)  # Reset to the original center
        pen.pendown()

# Parameters
num_triangles = 20
initial_size = 20
step_size = 20
rotation_angle = 5  # Angle to rotate each subsequent triangle

# Draw the nested triangles
draw_nested_triangles(num_triangles, initial_size, step_size, rotation_angle)

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
