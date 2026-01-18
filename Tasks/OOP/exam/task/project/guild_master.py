from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior


class GuildMaster:
    def __init__(self):
        self.members: list[BaseGuildMember] = []
        self.guild_halls: list [BaseGuildHall] = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        valid_types = {"Warrior": Warrior, "Mage": Mage}

        if member_type not in valid_types:
            raise ValueError("Invalid member type!")

        if any(m.tag == member_tag for m in self.members) or \
           any(m.tag == member_tag for hall in self.guild_halls for m in hall.members):
            raise ValueError(f"{member_tag} has already been added!")

        member = valid_types[member_type](member_tag, member_gold)
        self.members.append(member)
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        valid_types = {"CombatHall": CombatHall, "MagicTower": MagicTower}

        if guild_hall_type not in valid_types:
            raise ValueError("Invalid guild hall type!")

        if any(h.alias == guild_hall_alias for h in self.guild_halls):
            raise ValueError(f"{guild_hall_alias} has already been added!")

        hall = valid_types[guild_hall_type](guild_hall_alias)
        self.guild_halls.append(hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        hall = next((h for h in self.guild_halls if h.alias == guild_hall_alias), None)
        if hall is None:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        member = next((m for m in self.members if m.__class__.__name__ == member_type), None)
        if member is None:
            raise ValueError("No available members of the type!")

        if len(hall.members) >= hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall, sessions_number: int):
        for _ in range(sessions_number):
            for m in guild_hall.members:
                m.practice()
        total_skill = sum(m.skill_level for m in guild_hall.members)
        return f"{guild_hall.alias} members have {total_skill} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next((m for m in guild_hall.members if m.tag == member_tag), None)
        mem_level = next((m for m in guild_hall.members if m.skill_level == 10), None)
        if member is None or mem_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(
            self.guild_halls,
            key=lambda h: (-len(h.members), h.alias)
        )

        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}"
        ]

        for hall in sorted_halls:
            result.append(f">>>{hall.status()}")

        return "\n".join(result)