from project import player
from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: list = []
        self.info = ""

    def assign_player(self, player: Player) -> str:
        if player.name in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."

        self.players.append(player.name)
        player.guild = self.name
        self.info = player.player_info()
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str) -> str:
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."

        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result_two = self.info
        return result + result_two
