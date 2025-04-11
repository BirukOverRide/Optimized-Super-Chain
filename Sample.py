"""
Optimized Super Chain (OSC) Example: 

This code demonstrates how the Optimized Super Chain (OSC) principle is applied in a multi-class 
inheritance structure in Python. The OSC principle improves the usage of the Method Resolution 
Order (MRO) by ensuring cooperative multiple inheritance, optimizing the order in which base class 
constructors and methods are called, and reducing redundancy.

In this example, we have the following classes:

1. Animal: A base class representing an animal with a `make_sound` method.
2. Mammal: A subclass of Animal, adding a `is_warm_blooded` attribute and overriding `make_sound`.
3. Bird: A subclass of Animal, adding a `can_fly` attribute and overriding `make_sound`.
4. Bat: A class that demonstrates multiple inheritance from both Mammal and Bird. It uses `super()` 
   to ensure the correct method resolution and initialization order without manually calling base class 
   constructors.

The OSC principle is followed by:
- Using `super()` to call the parent constructors and methods in a clear and predictable way.
- Ensuring that the MRO is respected to avoid redundancy and maintain correct behavior.

This example showcases how OSC improves code clarity and avoids common pitfalls in multiple inheritance.

"""
# Base classes
class Animal:
    def __init__(self, name, **kwargs):
        self.name = name  # Initialization of the 'name' attribute.

    def make_sound(self):
        print(f"{self.name} makes a sound.")  # Default sound for Animal class.

# The 'Mammal' class inherits from Animal
class Mammal(Animal):
    def __init__(self, name, is_warm_blooded, **kwargs):
        super().__init__(name, **kwargs)  # OSC principle: Calls the super class constructor for 'Animal', 
                                         # passing the remaining arguments up the MRO without manually calling 'Animal'.
        self.is_warm_blooded = is_warm_blooded  # Initializing an attribute specific to Mammal.

    def make_sound(self):
        print(f"{self.name} is a mammal, and it roars.")  # Override make_sound to define mammal-specific behavior.

# The 'Bird' class inherits from Animal
class Bird(Animal):
    def __init__(self, name, can_fly, **kwargs):
        super().__init__(name, **kwargs)  # OSC principle: Calls the super class constructor for 'Animal',
                                         # passing remaining arguments up the MRO without manually calling 'Animal'.
        self.can_fly = can_fly  # Initializing an attribute specific to Bird.

    def make_sound(self):
        print(f"{self.name} is a bird, and it chirps.")  # Override make_sound to define bird-specific behavior.

# Multiple Inheritance Class
class Bat(Mammal, Bird):
    def __init__(self, name, is_warm_blooded, can_fly):
        # Use super() to initialize all parent classes via MRO
        super().__init__(name=name, is_warm_blooded=is_warm_blooded, can_fly=can_fly) 
        # OSC principle: super() calls are used to initialize both Mammal and Bird via the MRO, 
        # ensuring that attributes are correctly initialized in the order defined by the Method Resolution Order.

    def mammal_sound(self):
         super().make_sound()  # OSC principle: Calls 'make_sound()' in the Mammal class (via MRO) to ensure consistency.

    def make_sound(self):
        # Calls Mammal's make_sound (via MRO) and adds Bat-specific behavior.
        print(f"{self.name} also squeaks!")  # Bat-specific sound, after Mammal's sound.
        if self.can_fly:
            print(f"{self.name} can fly!")  # Bat-specific behavior, checks if it can fly.
        else:
            print(f"{self.name} cannot fly.")  # Bat-specific behavior, checks if it can't fly.

# Test
bat = Bat("Batty", True, True)  # Initializing Bat class which automatically uses super() to initialize all parents.
bat.make_sound()  # Output: Batty is a mammal, and it roars. Batty also squeaks! Batty can fly!
