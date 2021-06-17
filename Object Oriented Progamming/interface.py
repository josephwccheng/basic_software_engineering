''' https://realpython.com/python-interface/

Python Interface Overview
- An interface acts as a blueprint for designing classes.
- methods are abstract. Abstract method is one that the interface simply defines. It doesn’t implement the methods. 
    This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods.
- Other languages has the interface keyword, where python does not (hence class method)
    - Python doesn't require the class that it's implementing the interface to define all of the interface abstract methods
- Note: Interfaces in Python are handled differently than in most other languages, and they can vary in their design complexity


Informal Interfaces
- An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.
    example: you’ll take the perspective of a data engineer who needs to extract text from various different unstructured file types,
    like PDFs and emails. You’ll create an informal interface that defines the methods that will be in both the PdfParser and EmlParser concrete classes:

'''


class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


'''
    InformalParserInterface defines the two methods .load_data_source() and .extract_text(). These methods are defined but not implemented. The implementation 
    will occur once you create concrete classes that inherit from InformalParserInterface.
'''

''' To use your interface, you must create a concrete class. A concrete class is a subclass of the interface that provides an implementation of the interface’s
    methods. 
    You’ll create two concrete classes to implement your interface. The first is PdfParser, which you’ll use to parse the text from PDF files:
'''


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmlParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass


'''
    So far, you’ve defined two concrete implementations of the InformalPythonInterface. However, note that EmlParser fails to properly define .extract_text(). 
    If you were to check whether EmlParser implements InformalParserInterface, then you’d get the following result:

    check if both PdfParser and EmlParser implement InformalParserInterface 
    >>> issubclass(PdfParser, InformalParserInterface)
    True
    >>> issubclass(EmlParser, InformalParserInterface)
    True

    Note: This would return True, which poses a bit of a problem since it violates the definition of an interface!
'''


'''
    method resolution order (MRO) of PdfParser and EmlParser. This tells you the superclasses of the class in question, as well as the order in which they’re searched 
    for executing a method.
'''
print(PdfParser.__mro__)
print(EmlParser.__mro__)

'''
    Using Metaclasses
    you would want issubclass(EmlParser, InformalParserInterface) to return False when the implementing class doesn’t define all of the interface’s abstract methods
    To do this, you’ll create a metaclass called ParserMeta. You’ll be overriding two dunder methods:
        1. .__instancecheck__()
        2. .__subclasscheck__()

    Create a class called UpdatedInformalParserInterface that builds from the ParserMeta metaclass:
'''


class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass


'''
    create your concrete implementations.
'''


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
print(issubclass(EmlParserNew, UpdatedInformalParserInterface))

'''
    Checking the method resolution order (MRO)
    As you can see, UpdatedInformalParserInterface is a superclass of PdfParserNew, but it doesn’t appear in the MRO. 
    This unusual behavior is caused by the fact that UpdatedInformalParserInterface is a virtual base class of PdfParserNew.
'''
print(PdfParserNew.__mro__)


'''
    Using Virtual Base Classes
    
    From above, issubclass(EmlParserNew, UpdatedInformalParserInterface) returned True, even though UpdatedInformalParserInterface did not appear 
    in the EmlParserNew MRO. That’s because UpdatedInformalParserInterface is a virtual base class of EmlParserNew.
    
    The key difference between these and standard subclasses is that virtual base classes use the .__subclasscheck__() dunder method to implicitly 
    check if a class is a virtual subclass of the superclass. Additionally, virtual base classes don’t appear in the subclass MRO.

    Example: setup for creating your virtual base classes:
        1. The metaclass PersonMeta
        2. The base class PersonSuper
        3. The Python interface Person
'''


class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))


class PersonSuper:
    """A person superclass"""

    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass


'''
    TASK: define two concrete classes, Employee and Friend. The Employee class inherits from PersonSuper, while Friend implicitly inherits from Person:
    Although Friend does not explicitly inherit from Person, it implements .name() and .age(), so Person becomes a virtual base class of Friend. When you 
    run issubclass(Friend, Person) it should return True, meaning that Friend is a subclass of Person.

    .__instancecheck__(). This method is used to check if instances of Friend are created from the Person interface. Your code will call .__instancecheck__()
    when you use isinstance(Friend, Person).
'''
# Inheriting subclasses


class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass


class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """

    def name(self):
        pass

    def age(self):
        pass
