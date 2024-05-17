from abc import ABC, abstractmethod
from enum import Enum

class BaseDataForNamed(ABC):
    is_loading: bool

    def __init__(self, is_loading: bool) -> None:
        self.is_loading = is_loading

    @abstractmethod    
    def get_enum_data_for_named(self) -> Enum:
        pass

class BaseException(ABC):
    KEY: str
    __THIS_CLASS: str
    __EXCEPTION_CLASS: str

    def __init__(self, this_class: str, exception_class: str, key: str) -> None:
        self.KEY = key
        self.__THIS_CLASS = this_class
        self.__EXCEPTION_CLASS = exception_class
    
    ### Call this method in the descendant constructor as the last line
    def _debug_print_exception_where_to_string_parameters_this_class_and_exception_class(self) -> None:
        debug_print_exception("\n===start_to_trace_exception===\n")
        debug_print_exception(
            "WhereHappenedException(Class) --> " + self.__THIS_CLASS + "\n" +
            "NameException(Class) --> " + self.__EXCEPTION_CLASS + "\n" +
            "toString() --> " + self.to_string())
        debug_print_exception("\n===end_to_trace_exception===\n")
    
    @abstractmethod
    def to_string(self) -> str:
        pass

class EnumGuilty(Enum):
    DEVELOPER = "developer"
    DEVICE = "device"
    USER = "user"

class LocalException(BaseException):
    ENUM_GUILTY: EnumGuilty
    MESSAGE: str

    def __init__(self, this_class: str, enum_guilty: EnumGuilty, key: str, message: str = "") -> None:
        super().__init__(this_class, "LocalException", key)
        self.ENUM_GUILTY = enum_guilty
        self.MESSAGE = message
        self._debug_print_exception_where_to_string_parameters_this_class_and_exception_class()

    def to_string(self) -> str:
        return "LocalException(enumGuilty: " + self.ENUM_GUILTY.name + ", " + "key: " + self.KEY + ", " + "message (optional): " + self.MESSAGE + ")"

class NetworkException(BaseException):
    STATUS_CODE: int
    NAME_STATUS_CODE: str
    DESCRIPTION_STATUS_CODE: str

    def __init__(self, this_class: str, key: str, status_code: int, name_status_code: str = "", description_status_code: str = "") -> None:
        super().__init__(this_class, "NetworkException", key)
        self.STATUS_CODE = status_code
        self.NAME_STATUS_CODE = name_status_code
        self.DESCRIPTION_STATUS_CODE = description_status_code
        self._debug_print_exception_where_to_string_parameters_this_class_and_exception_class()

    @staticmethod
    def from_key_and_status_code(key: str, status_code: int):
        match status_code:
            case 201:
                return NetworkException() # HERE
            
    
    def to_string(self) -> str:
        return "NetworkException(key: " + self.KEY + ", " + "statusCode: " + self.STATUS_CODE + ", " + "nameStatusCode (optional): " + self.NAME_STATUS_CODE + ", " + "descriptionStatusCode (optional): " + self.DESCRIPTION_STATUS_CODE + ")"

def debug_print(text: str) -> None:
    print(text)

def debug_print_exception(text: str) -> None:
    debug_print("\x1B[31m" + text + "\x1b[0m")