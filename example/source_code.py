import math
import random
import time
from datetime import datetime
from collections import Counter, defaultdict, namedtuple
import re
import json
import os
import sys
import itertools
import functools
import threading

def math_operations():
    print("\n=== Math Operations ===")
    a, b = 10, 3
    
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print(f"Square root of {a}: {math.sqrt(a)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"Hypotenuse of 3 and 4: {math.hypot(3, 4)}")
    print(f"Trigonometry - sin(π/2): {math.sin(math.pi/2)}")
    print(f"Logarithm base 10 of 100: {math.log10(100)}")

def string_operations():
    print("\n=== String Operations ===")
    s = "  Hello, World!  "
    
    print(f"Original string: '{s}'")
    print(f"Upper case: '{s.upper()}'")
    print(f"Lower case: '{s.lower()}'")
    print(f"Capitalized: '{s.capitalize()}'")
    print(f"Title case: '{s.title()}'")
    print(f"Stripped: '{s.strip()}'")
    print(f"Replace 'World' with 'Python': '{s.replace('World', 'Python')}'")
    print(f"Split by commas: {s.split(',')}")
    print(f"Contains 'Hello'? {'Hello' in s}")
    print(f"Length: {len(s)}")
    print(f"Index of 'World': {s.find('World')}")
    print(f"Formatted string: 'Value: {42}, string: {'text'}'")
    print(f"String repetition: {'abc' * 3}")

def list_operations():
    print("\n=== List Operations ===")
    lst = [1, 2, 3, 4, 5]
    
    print(f"Original list: {lst}")
    print(f"First element: {lst[0]}")
    print(f"Last element: {lst[-1]}")
    print(f"Slicing [1:3]: {lst[1:3]}")
    print(f"Slicing [::2]: {lst[::2]}")
    
    lst.append(6)
    print(f"After append(6): {lst}")
    
    lst.extend([7, 8])
    print(f"After extend([7, 8]): {lst}")
    
    lst.insert(0, 0)
    print(f"After insert(0, 0): {lst}")
    
    lst.remove(3)
    print(f"After remove(3): {lst}")
    
    popped = lst.pop()
    print(f"After pop(): {lst}, popped element: {popped}")
    
    print(f"Index of element 4: {lst.index(4)}")
    print(f"Count of element 2: {lst.count(2)}")
    
    lst.reverse()
    print(f"After reverse(): {lst}")
    
    lst.sort()
    print(f"After sort(): {lst}")
    
    squared = [x**2 for x in lst]
    print(f"Squares of elements: {squared}")

    first, *rest, last = lst
    print(f"Unpacked: first={first}, rest={rest}, last={last}")

def dict_operations():
    print("\n=== Dictionary Operations ===")
    d = {'a': 1, 'b': 2, 'c': 3}
    
    print(f"Original dictionary: {d}")
    print(f"Value for key 'b': {d['b']}")
    print(f"Keys: {d.keys()}")
    print(f"Values: {d.values()}")
    print(f"Key-value pairs: {d.items()}")
    
    d['d'] = 4
    print(f"After adding 'd':4: {d}")
    
    del d['a']
    print(f"After deleting 'a': {d}")
    
    print(f"Get 'b' with default: {d.get('b', 0)}")
    print(f"Get 'x' with default: {d.get('x', 0)}")
    
    d.update({'e': 5, 'f': 6})
    print(f"After update: {d}")

    squares = {x: x**2 for x in range(5)}
    print(f"Dictionary comprehension: {squares}")

    dd = defaultdict(int)
    dd['a'] += 1
    print(f"defaultdict: {dd}")

def set_operations():
    print("\n=== Set Operations ===")
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    
    print(f"Set 1: {s1}")
    print(f"Set 2: {s2}")
    print(f"Union: {s1 | s2}")
    print(f"Intersection: {s1 & s2}")
    print(f"Difference: {s1 - s2}")
    print(f"Symmetric difference: {s1 ^ s2}")
    
    s1.add(5)
    print(f"After add(5): {s1}")
    
    s1.remove(1)
    print(f"After remove(1): {s1}")
    
    print(f"Contains 2? {2 in s1}")

    fs = frozenset([1, 2, 3])
    print(f"Frozen set: {fs}")

def file_operations():
    print("\n=== File Operations ===")
    filename = "test_file.txt"

    with open(filename, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    with open(filename, 'r') as f:
        content = f.read()
        print(f"File content:\n{content}")

    with open(filename, 'r') as f:
        print("File lines:")
        for line in f:
            print(line.strip())

    with open(filename, 'a') as f:
        f.write("Line 4\n")

    print(f"File exists? {os.path.exists(filename)}")

    os.remove(filename)
    print(f"File {filename} deleted")

def regex_operations():
    print("\n=== Regular Expressions ===")
    text = "Phones: 123-456-7890, 555-1234, (987)654-3210"
    pattern = r'\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}'
    
    print(f"Text: {text}")
    matches = re.findall(pattern, text)
    print(f"Found phone numbers: {matches}")

    new_text = re.sub(pattern, "[PHONE]", text)
    print(f"Text after substitution: {new_text}")

    email = "user@example.com"
    email_pattern = r'(\w+)@(\w+\.\w+)'
    match = re.match(email_pattern, email)
    if match:
        print(f"Email matched - user: {match.group(1)}, domain: {match.group(2)}")

def datetime_operations():
    print("\n=== Date and Time ===")
    now = datetime.now()
    print(f"Current datetime: {now}")
    print(f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Day: {now.day}")
    print(f"Hour: {now.hour}")
    print(f"Minute: {now.minute}")
    print(f"Second: {now.second}")
    
    formatted = now.strftime("%m/%d/%Y %H:%M:%S")
    print(f"Formatted datetime: {formatted}")
    
    future = now.replace(year=now.year + 1)
    print(f"Date one year from now: {future}")

    print(f"Timestamp: {now.timestamp()}")

    from datetime import timedelta
    tomorrow = now + timedelta(days=1)
    print(f"Tomorrow: {tomorrow}")

def generator_operations():
    print("\n=== Generators and Iterators ===")

    squares = [x*x for x in range(5)]
    print(f"Squares (list comprehension): {squares}")

    squares_gen = (x*x for x in range(5))
    print(f"Squares (generator): {list(squares_gen)}")

    def count_up_to(n):
        i = 1
        while i <= n:
            yield i
            i += 1
    
    print("Generator function:")
    for num in count_up_to(3):
        print(num)

    def infinite_counter():
        count = 0
        while True:
            yield count
            count += 1
    
    counter = infinite_counter()
    print("First 5 values from infinite generator:")
    for _ in range(5):
        print(next(counter))

    print("Enumerate example:")
    for i, val in enumerate(['a', 'b', 'c']):
        print(f"Index: {i}, Value: {val}")

def decorator_operations():
    print("\n=== Decorators ===")
    
    def simple_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling function {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Function {func.__name__} finished")
            return result
        return wrapper
    
    @simple_decorator
    def greet(name):
        print(f"Hello, {name}!")
    
    greet("Alice")

    def repeat(num_times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(num_times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(3)
    def say_hello():
        print("Hello!")
    
    print("Calling function with repeat decorator:")
    say_hello()

    def class_decorator(cls):
        cls.new_attribute = "Decorated"
        return cls
    
    @class_decorator
    class MyClass:
        pass
    
    print(f"Class with decorator: {MyClass.new_attribute}")

def threading_operations():
    print("\n=== Multithreading ===")
    
    def print_numbers():
        for i in range(1, 6):
            time.sleep(0.5)
            print(f"Number: {i}")
    
    def print_letters():
        for letter in 'abcde':
            time.sleep(0.7)
            print(f"Letter: {letter}")
    
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Both threads completed")

def json_operations():
    print("\n=== JSON Operations ===")
    
    data = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "programming"],
        "married": False
    }

    json_str = json.dumps(data, indent=2)
    print(f"JSON string:\n{json_str}")

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    with open("data.json", "r") as f:
        loaded_data = json.load(f)
    
    print(f"Loaded data: {loaded_data}")

    os.remove("data.json")
    print("File data.json deleted")

def functional_operations():
    print("\n=== Functional Programming ===")
    
    numbers = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x**2, numbers))
    print(f"Squares (map): {squared}")

    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers (filter): {even}")

    product = functools.reduce(lambda x, y: x * y, numbers)
    print(f"Product of numbers (reduce): {product}")

    print("All combinations of 2 elements:")
    for combo in itertools.combinations('ABC', 2):
        print(combo)

    def power(base, exponent):
        return base ** exponent
    
    square = functools.partial(power, exponent=2)
    print(f"Square of 5: {square(5)}")

def class_operations():
    print("\n=== Classes and OOP ===")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def greet(self):
            print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
        
        def __str__(self):
            return f"Person(name={self.name}, age={self.age})"
    
    class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self.student_id = student_id
        
        def study(self):
            print(f"{self.name} is studying")
        
        def __str__(self):
            return f"Student(name={self.name}, age={self.age}, id={self.student_id})"
    
    person = Person("Alex", 25)
    person.greet()
    print(person)
    
    student = Student("Maria", 20, "S12345")
    student.greet()
    student.study()
    print(student)

    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value > 0:
                self._radius = value
            else:
                raise ValueError("Radius must be positive")
        
        @property
        def area(self):
            return math.pi * self._radius ** 2
    
    circle = Circle(5)
    print(f"Circle radius: {circle.radius}")
    print(f"Circle area: {circle.area}")
    circle.radius = 7
    print(f"New radius: {circle.radius}")

def exception_operations():
    print("\n=== Exception Handling ===")
    
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: division by zero!")
            return None
        except TypeError:
            print("Error: invalid data type!")
            return None
        else:
            print("Division successful")
            return result
        finally:
            print("Finally block executed")
    
    print(divide(10, 2))
    print(divide(10, 0))
    print(divide("10", "2"))

    class MyError(Exception):
        pass
    
    try:
        raise MyError("Something went wrong")
    except MyError as e:
        print(f"Caught custom exception: {e}")

def module_operations():
    print("\n=== Modules and Packages ===")
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Directory contents: {os.listdir()}")
    print(f"Platform: {sys.platform}")
    print(f"Python version: {sys.version}")
    print(f"Python path: {sys.path}")

    print(f"Random number: {random.randint(1, 100)}")
    print(f"Random choice: {random.choice(['a', 'b', 'c'])}")
    print(f"Random sample: {random.sample(range(100), 5)}")

def namedtuple_operations():
    print("\n=== Namedtuple ===")
    
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    
    print(f"Point: {p}")
    print(f"x coordinate: {p.x}")
    print(f"y coordinate: {p.y}")

    print(f"As dict: {p._asdict()}")

def counter_operations():
    print("\n=== Counter ===")
    
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_counts = Counter(words)
    
    print(f"Word counts: {word_counts}")
    print(f"Count of 'apple': {word_counts['apple']}")
    print(f"3 most common: {word_counts.most_common(3)}")

    more_words = ["apple", "pear", "pear"]
    word_counts.update(more_words)
    print(f"After update: {word_counts}")

def lambda_operations():
    print("\n=== Lambda Functions ===")
    
    add = lambda x, y: x + y
    print(f"Sum of 3 and 5: {add(3, 5)}")
    
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squares of numbers: {squared}")

    points = [(1, 2), (3, 1), (5, 0)]
    sorted_points = sorted(points, key=lambda p: p[1])
    print(f"Points sorted by y-coordinate: {sorted_points}")

def context_manager_operations():
    print("\n=== Context Managers ===")

    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.time()
            print(f"Elapsed time: {self.end - self.start:.2f} seconds")
    
    with Timer():
        time.sleep(1)
        print("Inside the context manager block")

    from contextlib import contextmanager
    
    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")
    
    with tag("div"):
        print("Some content")

def dataclass_operations():
    print("\n=== Data Classes ===")
    
    from dataclasses import dataclass
    
    @dataclass
    class InventoryItem:
        name: str
        unit_price: float
        quantity: int = 0
        
        def total_cost(self) -> float:
            return self.unit_price * self.quantity
    
    item = InventoryItem("Widget", 9.99, 10)
    print(f"Item: {item}")
    print(f"Total cost: {item.total_cost()}")

def type_hint_operations():
    print("\n=== Type Hints ===")
    
    def greet(name: str) -> str:
        return f"Hello, {name}"
    
    print(greet("Alice"))

    from typing import List, Dict, Tuple
    
    def process_items(items: List[str], counts: Dict[str, int]) -> Tuple[int, int]:
        return len(items), sum(counts.values())
    
    items = ["apple", "banana"]
    counts = {"apples": 3, "oranges": 5}
    print(process_items(items, counts))

def main():
    print("=== Starting Comprehensive Python Feature Tests ===")

    test_functions = [
        math_operations,
        string_operations,
        list_operations,
        dict_operations,
        set_operations,
        file_operations,
        regex_operations,
        datetime_operations,
        generator_operations,
        decorator_operations,
        threading_operations,
        json_operations,
        functional_operations,
        class_operations,
        exception_operations,
        module_operations,
        namedtuple_operations,
        counter_operations,
        lambda_operations,
        context_manager_operations,
        dataclass_operations,
        type_hint_operations
    ]

    for func in test_functions:
        try:
            print(f"\n{'='*30}")
            print(f"Running {func.__name__}")
            print(f"{'='*30}")
            func()
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    main()