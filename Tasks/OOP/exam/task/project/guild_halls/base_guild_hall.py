import re
from abc import ABC, abstractmethod
from project.guild_members.base_guild_member import BaseGuildMember


class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members: list[BaseGuildMember] = []

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, value: str) -> None:
        trimmed = value.strip()
        if len(trimmed) < 2 or not re.fullmatch(r'[A-Za-z ]+', trimmed):
            raise ValueError("Guild hall alias is invalid!")
        self.__alias = trimmed

    @property
    @abstractmethod
    def max_member_count(self) -> int:
        pass

    def calculate_total_gold(self) -> int:
        if not self.members:
            return 0
        return sum(member.gold for member in self.members)

    def status(self) -> str:
        if self.members:
            sorted_tags = sorted(member.tag for member in self.members)
            members_str = " *".join(sorted_tags)
        else:
            members_str = "N/A"
        return f"Guild hall: {self.alias}; Members: {members_str}; Total gold: {self.calculate_total_gold()}"

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int) -> None:
        pass
