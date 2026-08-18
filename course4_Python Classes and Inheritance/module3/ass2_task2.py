'''
Modify the `Grass_Pokemon` subclass so that, when trained, the attack strength for `Grass_Pokemon` instances increases *only*
if they are at level 10 or higher. This means that if they transition from level `9` to level `10`, their `attack` should **not** increase.
 If they transition from `10` to `11`, their `attack` should increment by `attack_boost`. Do not change anything in the parent `Pokemon` class.

To test, create an instance of `Grass_Pokemon` with the `name` as `"Bulby"`.Assign the instance to the variable `p2`.
Create another instance of the `Grass_Pokemon` class with the name set to `"Pika"` and assign that instance to the variable `p3`.
Then, use `Grass_Pokemon` methods to train the `p3` `Grass_Pokemon` instance until it reaches at least level 10.
'''

class Pokemon(object):
    attack  = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health  = 15        # health scores for new Pokemon instances
    p_type  = "Normal"  # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be

    attack_boost  = 3   # When we "train", this is how much we increment our attack,...
    defense_boost = 2   # defense, and...
    health_boost  = 5   # health

    evolution_threshold = 10 # How many times we need to train before we "evolve"

    def __init__(self, name, level = 5):
        self.name  = name   # The name for this *instance*
        self._level = level # The starting level for this instance (the initial underscore signals that it is a private variable)

    @property
    def level(self): # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value): # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1 # Increment the level

        evolved = (self.level % self.evolution_threshold == 0) # Did we "evolve" on this step?
        
        return self.level, evolved # Return a tuple with the current level and whether we evolved

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack  = 15 # base levels for grass pokemon
    defense = 14
    health  = 12
    p_type  = "Grass"

    attack_boost  = 2 # when we "train", how much to increment by
    defense_boost = 3
    health_boost  = 6

    evolution_threshold = 12 # How many times we need to train before we "evolve"

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

    def attack_up(self):
        if self.level >= 10:
            self.attack = self.attack + self.attack_boost
        return self.attack

p1 = Grass_Pokemon('Belle')
print(p1.action())


p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')

while p3.level < 10:
    p3.train()


assert isinstance(p2, Grass_Pokemon), "p2 is not the correct type"
assert isinstance(p3, Grass_Pokemon), "p3 is not the correct type"

assert p2.__str__() == "Pokemon name: Bulby, Type: Grass, Level: 5", "p2 does not have the correct value"
assert p3.level >= 10, "p3 does not have the correct level; only train to level 10"
assert p3.attack_up() >= 17, "p3 does not have the correct attack value at level 10"
