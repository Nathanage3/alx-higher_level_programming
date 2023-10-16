# 0x0C Python - Almost a circle :snake:

> Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. It's often used as a “scripting language” for web applications. This means that it can automate specific series of tasks, making it more efficient. This project covers OOP programing

At the end of this project, I was able to solve these questions:
  
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Tasks :heavy_check_mark:

0. Files, classes and methods must be unit tested and be PEP 8 validated
1. First class Base
2. Class Rectangle that inherits from Base
3. Class Rectangle by adding validation of all setter methods and instantiation (id excluded)
4. Class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
5. Class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #
6. Updated the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
7. Updated the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
8. Updated the class Rectangle by adding the public method def update(self, *args)
9. Updated the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
10. Class Square that inherits from Rectangle
11. Updated the class Square by adding the public getter and setter size
12. Updated the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
13. Updated the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
14. Updated the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
15. Updated the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries 
16. Updated the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file
17. Updated the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
18. Updated the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.
19. Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.
20. Updated the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV
21. Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares

## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [tests/](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/tree/master/0x0C-python-almost_a_circle/tests/test_models)|
| [models/base.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)|
| [models/rectangle.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)|
| [models/square.py](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)|
| [models/](https://github.com/edward0rtiz/holbertonschool-higher_level_programming/tree/master/0x0C-python-almost_a_circle/models)|

## Additional info :construction:
### Resources

- Python 3.5
- PEP 8 1.7

### Try It On Your Machine :computer:	
```bash
git clone https://github.com/edward0rtiz/holbertonschool-higher_level_programming.git
cd 0x0C-python-almost_a_circle
FOR PYTHON SCRIPTS
./main_files/MAIN_FILENAME.py
```
