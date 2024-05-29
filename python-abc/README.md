0. Abstract Animal Class and its Subclasses
mandatory
Background:
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s ABC package facilitates the creation of abstract base classes.

Objective:
Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.
Resources:
Python ABC documentation: https://docs.python.org/3/library/abc.html
Instructions:
Setting up the Abstract Class:

Import the necessary components from the abc module.
Define the Animal class, ensuring it inherits from ABC to mark it as abstract.
Inside the Animal class, declare an abstract method named sound using the @abstractmethod decorator.
Implementing the Subclasses:

Create a subclass named Dog that inherits from the Animal class.
Implement the sound method in the Dog class to return the string “Bark”.
Similarly, create a subclass named Cat that also inherits from the Animal class.
Implement the sound method in the Cat class to return the string “Meow”.
Hints:

The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a TypeError.

1. Shapes, Interfaces, and Duck Typing
mandatory
Background:
Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

Objective:
Create an abstract class named Shape with two abstract methods: area and perimeter.
Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
Test the shape_info function with instances of both Circle and Rectangle.
Resources:
Python ABC documentation: https://docs.python.org/3/library/abc.html
Concept of Duck Typing: https://realpython.com/lessons/duck-typing/
Instructions:
Shape Abstract Class:

Define an abstract class Shape using the ABC package.
Within Shape, declare two abstract methods: area and perimeter.
Circle and Rectangle Classes:

Create a Circle class that inherits from Shape. The constructor (__init__) should accept a radius. Implement the area and perimeter methods.
Create a Rectangle class, also inheriting from Shape. Its constructor should accept the width and height. Implement the area and perimeter methods.
shape_info Function:

Define a function named shape_info that takes a single argument.
Without explicitly checking the type of the argument, call its area and perimeter methods (relying on duck typing).
Print the area and perimeter of the shape passed to the function.
Testing:

Instantiate a Circle and a Rectangle.
Pass each object to the shape_info function and observe the output.
Hints:

While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
Duck typing in the shape_info function implies that you shouldn’t use isinstance checks. Instead, trust that the passed object adheres to the Shape interface.

2. Extending the Python List with Notifications
mandatory
Background:
In Python, you can extend built-in classes to add or modify behavior. The list class provides a collection of methods and functionalities that handle list operations. By extending the list class, you can provide custom behaviors while retaining the original functionalities.

Objective:
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).

Instructions:
Setting up the VerboseList Class:

Define a class VerboseList that inherits from the built-in list class.
Within VerboseList, override the methods that modify the list: append, extend, remove, and pop.
Implementing Notifications:

For the append method: After adding the item to the list, print a message like “Added [item] to the list.”
For the extend method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
For the remove method: Before removing the item from the list, print a message like “Removed [item] from the list.”
For the pop method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
Testing:

Instantiate a VerboseList object.
Test all the overridden methods (append, extend, remove, and pop) and ensure that the appropriate messages are printed for each operation.
Hints:

Remember to call the original method of the list class using the super() function to ensure that the original functionality is retained. For example, for append: super().append(item).
Think about edge cases, such as trying to remove an item that doesn’t exist in the list.

3. CountedIterator - Keeping Track of Iteration
mandatory
Background:
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The iter function, which returns an iterator object, provides the __next__ method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

Objective:
Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.

Instructions:
Setting up the CountedIterator Class:

Define a class CountedIterator.
In the constructor (__init__), initialize two attributes: the iterator object (using the iter function) and a counter to track the number of items iterated.
Provide a method get_count to return the current value of the counter.
Overriding the next Method:

Within the CountedIterator class, override the __next__ method.
In this method, increment the counter each time the __next__ method is called.
Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the StopIteration exception.
Testing:

Instantiate a CountedIterator object using a list or another iterable.
Iterate over items using a loop or manual calls to the __next__ method.
Use the get_count method to retrieve and print the number of items that have been fetched.
Hints:

Remember that the __next__ method should raise a StopIteration exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
You can initialize the iterator object in the CountedIterator constructor using: self.iterator = iter(some_iterable).

4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
mandatory
Background:
In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

Objective:
Construct a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

Instructions:
Parent Classes Setup:

Create a Fish class with methods swim (which prints “The fish is swimming”) and habitat (which prints “The fish lives in water”).
Create a Bird class with methods fly (which prints “The bird is flying”) and habitat (which prints “The bird lives in the sky”).
Implementing FlyingFish:

Construct a FlyingFish class that inherits from both Fish and Bird.
Override the fly method to print “The flying fish is soaring!”.
Override the swim method to print “The flying fish is swimming!”.
Override the habitat method to print “The flying fish lives both in water and the sky!”.
Testing and MRO Exploration:

Instantiate an object of the FlyingFish class.
Call the fly, swim, and habitat methods and observe the outputs.
Use the mro() method or the .__mro__ attribute on the FlyingFish class to investigate the method resolution order. For instance, print(FlyingFish.mro()).
Hints:

Consider the order in which you list the parent classes when defining FlyingFish. It affects the method resolution order.
While multiple inheritance can be a powerful tool, it should be used judiciously, as it can make the code more complex and harder to read.

5. The Mystical Dragon - Mastering Mixins
mandatory
Background:
Mixins are a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.

Objective:
Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.

Instructions:
Creating Mixins:

Design a mixin called SwimMixin with a method swim that prints “The creature swims!”.
Design another mixin called FlyMixin with a method fly that prints “The creature flies!”.
Implementing Dragon:

Construct a class named Dragon that inherits from both SwimMixin and FlyMixin.
Within the Dragon class, you can add additional methods or attributes if desired, such as roar, which could print “The dragon roars!”.
Testing the Dragon’s Abilities:

Instantiate an object of the Dragon class named draco.
Demonstrate draco‘s abilities by calling the swim, fly, and (if implemented) roar methods.
Hints:

While designing mixins, remember that they should be focused, providing a single piece of functionality. They shouldn’t be overly broad or try to manage too much behavior.
Mixins allow for code reusability and can be combined in various ways to give objects different capabilities without setting up complex inheritance hierarchies.


