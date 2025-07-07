# from project.player import Player
# from project import player
#
# class Guild:
#     def __init__(self, name: str):
#         self.name = name
#         self.players: list = []
#         self.info = ""
#
#     def assign_player(self, player: Player) -> str:
#         if player.name in self.players:
#             return f"Player {player.name} is already in the guild."
#         if player.guild != "Unaffiliated" and player.guild != self.name:
#             return f"Player {player.name} is in another guild."
#         self.players.append(player.name)
#         player.guild = self.name
#         self.info = player.player_info()
#         return f"Welcome player {player.name} to the guild {player.guild}"
#
#     def kick_player(self, player_name: str) -> str:
#         if player_name not in self.players:
#             return f"Player {player_name} is not in the guild."
#         player.guild = "Unaffiliated"
#         return f"Player {player_name} has been removed from the guild."
#
#     def guild_info(self):
#         result = f"Guild: {self.name}\n"
#         result_two = self.info
#         return result + result_two
from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        second_part = "\n".join(player.player_info() for player in self.players)
        return result + second_part
        # for player in self.players:
        #     result.append(player.player_info())
        # return "\n".join(result)