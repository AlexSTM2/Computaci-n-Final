# Clase combate
# Alex
from random import *
import os
from Constants import *
import pygame, sys
from pygame.locals import *
import time 

pygame.init()
sound = pygame.mixer.Sound("sounds/battle_music.mp3")
sound.play()
sound.set_volume(0.1)

class Combat:
    def __init__(self, attacker, defensor):
        
        while attacker.life > 0 and defensor.life > 0:
            # inicia secuencia de combate
            menu = 0
            if attacker.char_class == "Orc warrior":

                print("Orco guerrero ", attacker.name)
                print("+------------------------+")
                print("|     Acciones           |")
                print("+========================+")
                print("|   1-Corte espiral      |")
                print("+------------------------+")
                print("|   2-Grito de guerra    |")
                print("+------------------------+")
                print("|   3-Ataque básico      |")
                print("+------------------------+")

            elif attacker.char_class == "Elf mage":

                print("Mago Elfo ", attacker.name)
                print("+--------------------------+")
                print("|     Acciones             |")
                print("+==========================+")
                print("|   1-Orbe arcano          |")
                print("+--------------------------+")
                print("|   2-Lluvia de estrellas  |")
                print("+--------------------------+")
                print("|   3-Ataque básico        |")
                print("+--------------------------+")

            elif attacker.char_class == "Human paladin":

                print("Paladín humano ", attacker.name)
                print("+---------------------+")
                print("|     Acciones        |")
                print("+=====================+")
                print("|   1-Filo tormenta   |")
                print("+---------------------+")
                print("|   2-Bendición solar |")
                print("+---------------------+")
                print("|   3-Ataque básico   |")
                print("+---------------------+")

            while menu == 0:

                print("Ingrese la acción a realizar")
                menu = str(input())
                if menu != "1" and menu != "2" and menu != "3":
                    print("Ingrese una opción correcta \n")
                    menu = 0
                    time.sleep(2)
                    os.system('pause')
                
            if menu == "1":

                #ability_sound = pygame.mixer.Sound(attacker.ab1_sound)
                #ability_sound.set_volume(0.2)
                #ability_sound.play()
                print("")
                print("+===============================================================+")
                print(attacker.name, "Ha utilizado la habilidad: φ", attacker.ab1_name,"φ")
                total_dmg = attacker.ab1_damage - defensor.armor
                defensor.life = defensor.life - total_dmg
                print("-----------------------------------------------------------------")
                print(defensor.name, "❌ Ha recibido el ataque ❌, con un daño total de: ",
                      total_dmg)
                print("+===============================================================+")
            elif menu == "2":

                #ability_sound = pygame.mixer.Sound(attacker.ab2_sound)
                #ability_sound.set_volume(0.2)
                #ability_sound.play()
                print("")
                print("+===============================================================+")
                print(attacker.name, "Ha utilizado la habilidad: Ω", attacker.ab2_name,"Ω")
                total_dmg = attacker.ab2_damage - defensor.armor
                defensor.life = defensor.life - total_dmg
                print("-----------------------------------------------------------------")
                print(defensor.name, "❌ Ha recibido el ataque ❌, con un daño total de: ",
                      total_dmg)
                print("+===============================================================+")
            elif menu == "3":

                #ability_sound = pygame.mixer.Sound(attacker.basic_sound)
                #ability_sound.set_volume(0.2)
                #ability_sound.play()
                print("")
                print("+===============================================================+")
                print(attacker.name, "⚔️Ha realizado un ataque básico   ⚔️")
                total_dmg = attacker.strenght - defensor.armor
                defensor.life = defensor.life - total_dmg
                print("-----------------------------------------------------------------")
                print(defensor.name, "❌ Ha recibido el ataque ❌, con un daño total de: ",
                      total_dmg)
                print("+===============================================================+")
            if defensor.life > 0:

                time.sleep(3)
                rand = randint(1, 10)

                if rand >= 6:

                    #ability_sound = pygame.mixer.Sound(defensor.ab1_sound)
                    #ability_sound.set_volume(0.1)
                    #ability_sound.play()
                    print("")
                    print("+===============================================================+")
                    total_dmg = defensor.ab1_damage - attacker.armor
                    attacker.life -= total_dmg
                    print(defensor.name, "ha utilizado la habilidad: φ", defensor.ab1_name,"φ")
                    print("-----------------------------------------------------------------")
                    print("❌ Has recibido el ataque ❌, con un daño total de:", total_dmg)
                    time.sleep(3)
                    print("+===============================================================+")
                elif rand <= 5:

                    #ability_sound = pygame.mixer.Sound(defensor.ab2_sound)
                    #ability_sound.set_volume(0.1)
                    #ability_sound.play()
                    print("")
                    print("+===============================================================+")
                    total_dmg = defensor.ab2_damage - attacker.armor
                    attacker.life -= total_dmg
                    print(defensor.name, "ha utilizado la habilidad: Ω", defensor.ab2_name,"Ω")
                    print("-----------------------------------------------------------------")
                    print("❌ Has recibido el ataque ❌, con un daño total de:", total_dmg)
                    time.sleep(3)
                    print("+===============================================================+")
            if defensor.life <= 0:
                print("")
                print("+=============================+")
                print("    Has matado a ", defensor.name)
                print("+=============================+")
            elif attacker.life <= 0:
                print("")
                print("+==================================================+")
                print("                       †                            ")
                print("†Tus puntos de vida han llegado a 0! Has perdidido.†")
                print("                       †                            ")
                print("+==================================================+")
            else:
                print("")
                print("+===============================================+")
                print("Tu vida restante es de: ✚", attacker.life,"✚")
                print("La vida restante de", defensor.name,"es de: ✚", defensor.life,"✚")
                print("+===============================================+")
        time.sleep(2)
        end = 0.1
        while end > 0:
            sound.set_volume(end)
            end -= 0.005
            time.sleep(0.2)
Combate1 = Combat(Varok, Leeroy)