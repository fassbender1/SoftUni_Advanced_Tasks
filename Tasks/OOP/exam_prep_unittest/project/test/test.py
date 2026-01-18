from unittest import TestCase, main
from project.soccer_player import SoccerPlayer

class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Cristiano", 38, 850, "Real Madrid")
        self.other_player = SoccerPlayer("Lionel Messi", 37, 870, "Barcelona")

    def test_init(self):
        self.assertEqual("Cristiano", self.player.name)
        self.assertEqual(38, self.player.age)
        self.assertEqual(850, self.player.goals)
        self.assertEqual("Real Madrid", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_name_setter_valid(self):
        self.player.name = "Neymar Jr"
        self.assertEqual(self.player.name, "Neymar Jr")

    def test_name_setter_invalid_raises(self):
        with self.assertRaises(ValueError) as cm:
            self.player.name = "Leo"
        self.assertEqual("Name should be more than 5 symbols!", str(cm.exception))

    def test_age_setter_valid(self):
        self.player.age = 25
        self.assertEqual(self.player.age, 25)

    def test_age_setter_invalid_raises(self):
        with self.assertRaises(ValueError) as cm:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(cm.exception))

    # --- Goals property ---
    def test_goals_setter_valid(self):
        self.player.goals = 100
        self.assertEqual(self.player.goals, 100)

    def test_goals_negative_resets_to_zero(self):
        self.player.goals = -5
        self.assertEqual(self.player.goals, 0)

    # --- Team property ---
    def test_team_setter_valid(self):
        self.player.team = "PSG"
        self.assertEqual(self.player.team, "PSG")

    def test_team_setter_invalid_raises(self):
        with self.assertRaises(ValueError) as cm:
            self.player.team = "Chelsea"
        self.assertTrue("Team must be one of the following" in str(cm.exception))

    # --- change_team method ---
    def test_change_team_successful(self):
        result = self.player.change_team("Juventus")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "Juventus")

    def test_change_team_invalid(self):
        result = self.player.change_team("Chelsea")
        self.assertEqual(result, "Invalid team name!")
        self.assertNotEqual(self.player.team, "Chelsea")

    # --- add_new_achievement method ---
    def test_add_new_achievement_first_time(self):
        result = self.player.add_new_achievement("Golden Boot")
        self.assertEqual(result, "Golden Boot has been successfully added to the achievements collection!")
        self.assertIn("Golden Boot", self.player.achievements)
        self.assertEqual(self.player.achievements["Golden Boot"], 1)

    def test_add_new_achievement_increment(self):
        self.player.add_new_achievement("Golden Boot")
        self.player.add_new_achievement("Golden Boot")
        self.assertEqual(self.player.achievements["Golden Boot"], 2)

    # --- __lt__ method ---
    def test_lt_player_has_fewer_goals(self):
        result = self.player < self.other_player
        self.assertEqual(result, f"{self.other_player.name} is a top goal scorer! S/he scored more than {self.player.name}.")

    def test_lt_player_has_more_goals(self):
        result = self.other_player < self.player
        self.assertEqual(result, f"{self.other_player.name} is a better goal scorer than {self.player.name}.")

if __name__ == "__main__":
    main()