from abc import ABC, abstractmethod


class UObject(ABC):
    
    @abstractmethod
    def get_property(self, prop_name: str):
        pass

    @abstractmethod
    def set_property(self, prop_name: str, new_value):
        pass
