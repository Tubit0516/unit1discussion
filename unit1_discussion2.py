"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    species = "Generic  Parent"

    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Parent Name: {self.name}, Age: {self.age}, Species: {self.species}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    role = "Student"

    def _init_(self, name, age, grade):
        super()._init_(name, age)

        self.grade = grade
        self.is_active = True

    def display_info(self): 
        return f"Child Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Role: {self.role}"
                


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    child1 = ChildClass("Alice", 12, 7)
    child2 = ChildClass("Bob", 14, 9)

    print(f"Class variable accessed via Class: {childClass.role}")
    print(f"Class variable accessed via Object1: {child1.role}")

    child1.hobby = "Coding"
    print(f"Added unique attribute 'hobby' to child1: {child1.hobby}")

    print(f"child1 Namespace (_dict_): {child1._dict_}")
    print(f"child2 Namespace (_dict_): {child2._dict_}")

    print(f"ChildClass Namespace (_dict_): {dict(ChildClass._dict_)}")
          
    if _name_ == "_main_":
        demonstrate_namespaces()
    
# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # 1. Create an object that contains nested mutable data
    original = {"name": "Alice", "skills": ["Python", "Java"]}

    #2. Create a shallow copy
    shallow_copied = copy.copy(original)

    #3. Create a deep copy
    deep_copied = copy.deepcopy(original)

    #4. Modify the original object's nested data
    original ["skills"].append("C++")
    original["name"] = "Bob"
    #5. Display the original object, shallow copy, and a deep copy
    print(f"Original:      {original}")
    print(f"Shallow Copy:  {shallow_copied}")
    print(f"Deep Copy:     {deep_copied}")

    #6. Explanation of the differences
    """
    EXPLANATION:
    - Shallow copy: Copies the outer dictionary object, but references the SAME inner mutable nested list('skills').
      Therefore, appending 'C++' to the original list also updates the shallow copy.
    - Deep Copy: Recursively copies everything, constructing a brand-new nested list.
      Modifying the original does not impact the deep copy at all.
    """




# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    # 1. Create at least one object from the parent class

    parent_obj = Parent("Arthur")
    print(parent_obj.speak())
    

    print("\nTODO: Create and test your child object")
    # 2. Create at least one object from the child class.
    child_obj = Child("Morgan")

    # 3. Demonstrate inheritance by calling methods.
    print(child_obj.speak()) # Inherited method from Parent
    print(child_obj.play()) # Child-specific method
    
    # 4 & 5. Call demonstration functions.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
