from typing import List
from OOP.first_steps_in_OOP.pokemon_battle.project.pokemon_battle import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_to_release = next((pok for pok in self.pokemons if pok.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"
        # for pok in self.pokemons:
        #     if pok.name == pokemon_name:
        #         self.pokemons.remove(pok)
        #         return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}",
                  f"Pokemon count {len(self.pokemons)}"]
        for pok in self.pokemons:
            result.append(f"- {pok.pokemon_details()}")
        return "\n".join(result)

