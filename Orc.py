#Clase orco
class Orco:

    def __init__(self, name="Varok", strenght=15, dexterity=8, life=80, intelligence=10, faith = 10, char_class = "Orc warrior",
                 ab1_name="Corte espiral", ab2_name="Grito de guerra", ab1_damage=0, ab2_damage=0, armor =6,
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
        self.ab1_damage = ab1_damage + self.strenght * 3
        self.ab2_damage = ab2_damage + self.strenght * 1.5 + self.dexterity * 2
        self.armor = armor
        self.ab1_sound = ab1_sound + "sounds/spiral 2.mp3"
        self.ab2_sound = ab2_sound + "sounds/orc 2.mp3"
        self.basic_sound = basic_sound + "sounds/b_attack_orc.mp3"

    def restart_stats(self):
        self.strenght = self.strenght * 0 + 15
        self.dexterity = self.dexterity * 0 + 8
        self.life = self.life * 0 + 80
        self.intelligence = self.intelligence * 0 + 6
        self.faith = self.faith * 0 + 6