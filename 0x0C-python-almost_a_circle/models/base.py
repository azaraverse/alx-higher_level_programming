#!/usr/bin/python3
""" DEFINES BASE CLASS
"""
import json
import csv
import turtle


class Base():
    """Base Class for other classes to avoid code duplication"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base Class

        Args:
            id (int): ID attribute of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        'list_dictionaries'

        Args:
            list_dictionaries (list): list of dictionaries.
        Returns:
            JSON string representation of the list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        'list_objs' to a file

        Args:
            list_objs (list): list of instances that inherit of Base
        """
        filename = cls.__name__ + '.json'

        if list_objs is None or len(list_objs) == 0:
            with open(filename, 'w', encoding='UTF-8') as file:
                file.write('[]')
            return
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        # create file or open file if it exists in write mode
        with open(filename, 'w', encoding='UTF-8') as file:
            # write the json_string to the file
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
        representation 'json_string'

        Args:
            json_string (str): string representing a list of dictionaries
        Returns:
            List if the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        """Class method that returns an instance with all attrs
        already set

        Args:
            **dictionary (dict): key-worded argument
        Returns:
            an instance with all attributes already set
        """
        dummy_instance = None
        if cls.__name__ == 'Rectangle':
            dummy_instance = Rectangle(5, 10)
        elif cls.__name__ == 'Square':
            dummy_instance = Square(10)
        else:
            raise ValueError(f'Unsupported class: {cls.__name__}')

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method serialises to a csv file

        Args:
            list_objs (list): list of instances
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='UTF-8', newline='') as csv_file:
            writer = csv.writer(csv_file)

            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
                elif cls.__name__ == 'Square':
                    writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y]
                    )
                else:
                    raise ValueError(f'Unsupported class {cls.__name__}')

    @classmethod
    def load_from_file_csv(cls):
        """Class method that deserialises from a csv file."""
        filename = cls.__name__ + '.csv'
        instances = []

        with open(filename, 'r', encoding='UTF-8') as csv_file:
            if cls.__name__ == 'Rectangle':
                obj = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                obj = ['id', 'size', 'x', 'y']
            else:
                raise ValueError(f'Unsupported class {cls.__name__}')

            reader = csv.DictReader(csv_file, obj)

            dict_list = [
                dict((key, int(value)) for key, value in d.items())
                for d in reader
            ]
            instances = [cls.create(**d) for d in dict_list]
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Uses the Turtle graphics module.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        screen = turtle.Screen()
        screen.title('Drawing Shapes - azara ;)')
        screen.bgcolor('teal')

        my_turtle = turtle.Turtle()
        my_turtle.speed(2.5)
        my_turtle.pensize(2)
        my_turtle.shape('triangle')
        my_turtle.shapesize(.8)

        # Draw Rectangles
        for rectangle in list_rectangles:
            my_turtle.penup()
            my_turtle.goto(rectangle.x, rectangle.y)
            my_turtle.pendown()
            my_turtle.color('white', 'gray')
            my_turtle.begin_fill()
            for _ in range(2):
                my_turtle.forward(rectangle.width)
                my_turtle.left(90)
                my_turtle.forward(rectangle.height)
                my_turtle.left(90)
            my_turtle.end_fill()

        # Draw Squares
        for square in list_squares:
            my_turtle.penup()
            my_turtle.goto(square.x, square.y)
            my_turtle.pendown()
            my_turtle.color('orange')
            for _ in range(4):
                my_turtle.forward(square.size)
                my_turtle.left(90)

        # Close the window on click
        screen.exitonclick()
