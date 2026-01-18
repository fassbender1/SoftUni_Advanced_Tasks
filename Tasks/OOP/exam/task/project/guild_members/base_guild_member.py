import re
from abc import ABC, abstractmethod


class BaseGuildMember(ABC):
    def __init__(self, tag: str, gold: int, role: str, skill_level: int):
        self.tag = tag
        self.gold = gold
        self.role = role
        self.skill_level = skill_level

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        if not re.fullmatch(r'[A-Za-z0-9]+', value):
            raise ValueError("Tag must contain only letters and digits!")
        self.__tag = value

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    # def gold(self, value):
    #     if value < 0:
    #         raise ValueError(f"Gold must be a non-negative integer!")
    def gold(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Gold must be a non-negative integer!")
        self.__gold = value

    @property
    def role(self):
        return self.__role

    @role.setter
    # def role(self, value):
    #     if value == "" or value == " ":
    #         raise ValueError("Role cannot be empty!")
    #     self.__role = value
    def role(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Role cannot be empty!")
        self.__role = value.strip()
    
    @property
    def skill_level(self):
        return self.__skill_level
    
    @skill_level.setter
    # def skill_level(self, value):
    #     if not 0 > value <= 10:
    #         raise ValueError("Skill level is out of range!")
    #     self.__skill_level = value
    def skill_level(self, value: int) -> None:
        if not isinstance(value, int) or not (1 <= value <= 10):
            raise ValueError("Skill level is out of range!")
        self.__skill_level = value

    @abstractmethod
    def practice(self):
        pass


