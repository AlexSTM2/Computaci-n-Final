# Clase Elfo
class Elf:

    def __init__(self, name="Zireael", strenght=6, dexterity=5, life=50, intelligence=20, faith=12,
                 char_class="Elf Mage ", ab1_name="Orbe arcano", 
                 ab2_name="Lluvia de estrellas", ab1_damage=0, ab2_damage=0, armor=3,
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
        self.ab1_damage = ab1_damage + self.intelligence * 1.4
        self.ab2_damage = ab2_damage + self.intelligence * 1.2 + self.faith * 1.3
        self.armor = armor
        self.ab1_sound = ab1_sound + "sounds/spell sound 1.mp3"
        self.ab2_sound = ab2_sound + "sounds/stars.mp3"
        self.basic_sound = basic_sound + "sounds/b_attack_mage.mp3"

    def restart_stats(self):
        self.strenght = self.strenght * 0 + 6
        self.dexterity = self.dexterity * 0 + 5
        self.life = self.life * 0 + 50
        self.intelligence = self.intelligence * 0 + 20
        self.faith = self.faith * 0 + 12