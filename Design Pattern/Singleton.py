class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. 
    Some possible methods include: base class, decorator, metaclass. 
    We will use the metaclass because it is best suited for this purpose.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        if the class method is called for a derived class, the derived class object is passed as the 
        implied first argument"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Singleton method called")


if __name__ == "__main__":
    inst1 = Singleton()
    inst2 = Singleton()

    if id(inst1) == id(inst2):
        print("Singleton works")
    else:
        print("Singleton doesn't work")
