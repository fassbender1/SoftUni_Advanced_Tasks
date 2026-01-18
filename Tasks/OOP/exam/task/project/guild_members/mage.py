from project.guild_members.base_guild_member import BaseGuildMember


class Mage(BaseGuildMember):
    ROLE = "Mage"
    SKILL_LEVEL = 1
    MAXIMUM_LEVEL = 10
    def __init__(self, tag: str, gold: int):
        super().__init__(tag, gold, self.ROLE, self.SKILL_LEVEL)

    def practice(self):
        if self.SKILL_LEVEL * 2 <= self.MAXIMUM_LEVEL:
            self.SKILL_LEVEL *= 2
        else:
            self.SKILL_LEVEL = self.MAXIMUM_LEVEL
