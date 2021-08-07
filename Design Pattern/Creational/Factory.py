"""
Factory Method design pattern

Description:
    1) It provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects 
       that will be created
    2) It suggests to replace direct object construction calls(using the new operator) with calls to special factory method. Objects are still
       being called within the factory method. These objects returned by the methods are known as products
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

   @abstractmethod
   def factory_method(self):
      pass

   def some_operation(self):
      product = self.factory_method()
      result = f"Creator: The same creator's code has just worked with {product.operation()}"
      return result
   

class ConcreteCreator1(Creator):
   def factory_method(self) -> Product:
       return ConcreteProduct1()



class ConcreteCreator2(Creator):
   def factory_method(self) -> Product:
       return ConcreteProduct2()


class Product(ABC):
   @abstractmethod
   def operation(self) -> str:
      pass

class ConcreteProduct1(Product):
   def operation(self) -> str:
       return "Result of the ConcreteProduct1"

class ConcreteProduct2(Product):
   def operation(self) -> str:
       return "Result of the ConcreteProduct2"

def client_code(creator: Creator):

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
