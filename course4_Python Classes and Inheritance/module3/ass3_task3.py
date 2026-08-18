'''
Now, suppose different Pokemon types have strengths against other types. For example, "Water" Pokemon are strong against "Fire" Pokemon.
Along with the  Pokemon  parent class, we have also provided several subclasses 
(note that we are *not* implementing a  Normal_Pokemon  class; "Normal" Pokemon can be instances of the  Pokemon  base class).
We also added a  strong_vs class variable to track which types of Pokemon this type is strong against.

- **Grass** is strong against *Water*
- **Fire** is strong against *Normal* and *Grass*
- **Water** is strong against *Fire*
- **Normal** is not strong against any type

Let's also say that a Pokemon is "weak" against any Pokemon that is "strong" against it.
For example, since *Fire* is strong against *Normal*, that means *Normal* is *weak* against *Fire*.
To capture this relationships, write two methods in the  Pokemon  parent class that will be inherited by the subclasses:

-  is_strong_vs(self, opponent) : accepts an  opponent , which is a  Pokemon  instance.
    It should return  true  if type  p_type  of  opponent  is in  self.strong_vs  and  false  otherwise

-  is_weak_vs(self, opponent) : accepts an  opponent , which is a  Pokemon  instance.
    It should return  true  if the **opponent** is strong against  self  (you probably want to reference  opponent.is_strong_vs )
'''


class Pokemon():
    attack  = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health  = 15        # health scores for new Pokemon instances
    p_type  = "Normal"  # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be

    attack_boost  = 3   # When we "train", this is how much we increment our attack,...
    defense_boost = 2   # defense, and...
    health_boost  = 5   # health

    evolution_threshold = 10 # How many times we need to train before we "evolve"

    strong_vs = []

    def __init__(self, name, level = 5):
        self.name  = name  # The name for this *instance*
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

        self.level   = self.level + 1 # Increment the level

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

    def is_strong_vs(self, opponent):
        return opponent.p_type in self.strong_vs

    def is_weak_vs(self, opponent):
        return opponent.is_strong_vs(self)
    
    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack  = 15
    defense = 14
    health  = 12

    attack_boost  = 2
    defense_boost = 3
    health_boost  = 6

    p_type    = "Grass"

    strong_vs = ["Water"]



class Fire_Pokemon(Pokemon):
    p_type    = "Fire"
    
    strong_vs = ["Grass", "Normal"]


class Water_Pokemon(Pokemon):
    p_type    = "Water"
    
    strong_vs = ["Fire"]

    
