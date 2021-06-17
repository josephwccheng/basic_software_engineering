'''
    Source: https://realpython.com/python-interface/
    Formal Interfaces

    Context: informal interfaces would be the wrong approach for larger applications. In order to create a formal Python
    interface, you’ll need a few more tools from Python’s abc module.

    Summary:
        - An informal Python interface is useful for small projects where you’re less likely to get confused as to what the return types of the methods are.
        - As a project grows, the need for a formal Python interface becomes more important as it becomes more difficult to infer return types. This ensures 
            that the concrete class, which implements the interface, overwrites the abstract methods.

    Using abc.ABCMeta
    - To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin ABCMeta from the abc module.
    - Rather than create your own metaclass, you’ll use abc.ABCMeta as the metaclass.
        - Then, you’ll overwrite .__subclasshook__() in place of .__instancecheck__()
        - overwrite .__subclasscheck__(), as it creates a more reliable implementation of these dunder methods.

'''


'''
    Using .__subclasshook__()

    - If you run issubclass() on PdfParserNew and EmlParserNew, then issubclass() will return True and False, respectively.
'''




import abc
class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


print(issubclass(PdfParserNew, FormalParserInterface))
print(issubclass(EmlParserNew, FormalParserInterface))

'''
    Using abc to Register a Virtual Subclass
    - Once you’ve imported the abc module, you can directly register a virtual subclass by using the .register() metamethod.
    - In the next example, you register the interface Double as a virtual base class of the built-in __float__ class:

    Note: By using the .register() meta method, you’ve successfully registered Double as a virtual subclass of float.
'''


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


Double.register(float)
print(issubclass(float, Double))
print(isinstance(1.2345, Double))


'''
    Once you’ve registered Double, you can use it as class decorator to set the decorated class as a virtual subclass:
    The decorator register method helps you to create a hierarchy of custom virtual class inheritance.
'''


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass


print(issubclass(Double64, Double))  # True


'''
    Using Subclass Detection With Registration
        - .__subclasshook__() takes precedence over virtual subclass registration. To ensure that the registered virtual 
            subclasses are taken into consideration, you must add NotImplemented to the .__subclasshook__() dunder method.
        
        Note: Since you’ve used registration, you can see that EmlParserNew is considered a virtual subclass of your FormalParserInterface interface. 
            This is not what you wanted since EmlParserNew doesn’t override .extract_text(). Please use caution with virtual subclass registration! 
'''


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


@FormalParserInterface.register
class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


print(issubclass(PdfParserNew, FormalParserInterface))  # True
print(issubclass(EmlParserNew, FormalParserInterface))  # True


''' 
    Using Abstract Method Declaration
        - An abstract method is a method that’s declared by the Python interface, but it may not have a useful implementation. 
        The abstract method must be overridden by the concrete class that implements the interface in question.
    
    To create abstract methods in Python
        - you add the @abc.abstractmethod decorator to the interface’s methods. 
    
    In the next example,
        - update the FormalParserInterface to include the abstract methods .load_data_source() and .extract_text():
'''


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError


class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


'''
    In the above example
        - you’ve finally created a formal interface that will raise errors when the abstract methods aren’t overridden. 
        - The PdfParserNew instance, pdf_parser, won’t raise any errors, as PdfParserNew is correctly overriding the FormalParserInterface abstract methods. 
        - However, EmlParserNew will raise an error:

        TypeError: Can't instantiate abstract class EmlParserNew with abstract method extract_text
'''

pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()
