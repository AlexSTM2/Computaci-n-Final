# Clase humano
class Human:

    def __init__(self, name="Leeroy", strenght=12, dexterity=5, life=60, intelligence=10, faith=15,
                 char_class="Human paladin ",
                 ab1_name="Filo tormenta", ab2_name="Bendición solar", ab1_damage=0, ab2_damage=0, armor=10,
                 ab1_sound="", ab2_sound="", basic_sound=""):

        self.strenght = strenght
        self.name = name
        self.dexterity = dexterity
        self.life = life
        self.intelligence = intelligence
        self.faith = faith
        self.char_class = char_class
        self.ab1_name = ab1_name
        self.ab2_name = ab2_name
        self.ab1_damage = ab1_damage + self.faith * 1.5 + self.strenght * 1.2
        self.ab2_damage = ab2_damage + self.faith * 2
        self.armor = armor
        self.ab1_sound = ab1_sound + "sounds/thunder sword.mp3"
        self.ab2_sound = ab2_sound + "sounds/healing 1.mp3"
        self.basic_sound = basic_sound + "sounds/basic attack.mp3"
    
    def restart_stats(self):
        self.strenght = self.strenght * 0 + 12
        self.dexterity = self.dexterity * 0 + 7
        self.life = self.life * 0 + 65
        self.intelligence = self.intelligence * 0 + 10
        self.faith = self.faith * 0 + 15