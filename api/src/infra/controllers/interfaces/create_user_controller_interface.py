from typing import Dict
from abc import ABC, abstractmethod

class CreateUserControllerInterface(ABC):
    
    @abstractmethod
    def handle(self, user_data: dict)-> dict:
        pass