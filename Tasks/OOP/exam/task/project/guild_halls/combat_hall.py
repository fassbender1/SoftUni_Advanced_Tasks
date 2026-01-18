from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_members.warrior import Warrior


class CombatHall(BaseGuildHall):
    MAX_MEMBER_COUNT = 3
    def __init__(self, alias: str):
        super().__init__(alias)

    @property
    def max_member_count(self) -> int:
        return self.MAX_MEMBER_COUNT

    def increase_gold(self, min_skill_level_value: int) -> None:
        for member in self.members:
            if isinstance(member, Warrior) and member.skill_level >= min_skill_level_value:
                member.gold += 300