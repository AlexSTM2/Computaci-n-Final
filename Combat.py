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

                ability_sound = pygame.mixer.Sound(attacker.ab1_sound)
                ability_sound.set_volume(0.2)
                ability_sound.play()
                print(attacker.name, "ha utilizado la habilidad", attacker.ab1_name)
                total_dmg = attacker.ab1_damage - defensor.armor
                defensor.life = defensor.life - total_dmg
                print(defensor.name, "ha recibido el ataque, con un daño total de: ",
                      total_dmg)

            elif menu == "2":

                ability_sound = pygame.mixer.Sound(attacker.ab2_sound)
                ability_sound.set_volume(0.2)
                ability_sound.play()
                print(attacker.name, "ha utilizado la habilidad", attacker.ab2_name)
                total_dmg = attacker.ab2_damage - defensor.armor
                defensor.life = defensor.life - total_dmg
                print(defensor.name, "ha recibido el ataque, con un daño total de: ",
                      total_dmg)

            elif menu == "3":

                ability_sound = pygame.mixer.Sound(attacker.basic_sound)
                ability_sound.set_volume(0.2)
                ability_sound.play()
                print(attacker.name, "ha realizado un ataque básico")
                total_dmg = attacker.strenght - defensor.armor
                defensor.life = defensor.life - total_dmg
                print(defensor.name, "ha recibido el ataque, con un daño total de: ",
                      total_dmg)

            if defensor.life > 0:

                time.sleep(3)
                rand = randint(1, 10)

                if rand >= 6:

                    ability_sound = pygame.mixer.Sound(defensor.ab1_sound)
                    ability_sound.set_volume(0.1)
                    ability_sound.play()
                    total_dmg = defensor.ab1_damage - attacker.armor
                    attacker.life -= total_dmg
                    print(defensor.name, "ha utilizado la habilidad", defensor.ab1_name)
                    print("Has recibido el ataque, con un daño total de:", total_dmg)
                    time.sleep(3)
            
                elif rand <= 5:

                    ability_sound = pygame.mixer.Sound(defensor.ab2_sound)
                    ability_sound.set_volume(0.1)
                    ability_sound.play()
                    total_dmg = defensor.ab2_damage - attacker.armor
                    attacker.life -= total_dmg
                    print(defensor.name, "ha utilizado la habilidad", defensor.ab2_name)
                    print("Has recibido el ataque, con un daño total de:", total_dmg)
                    time.sleep(3)

            if defensor.life <= 0:
                print("Has matado a ", defensor.name)
            elif attacker.life <= 0:
                print("Tus puntos de vida han llegado a 0! Has perdidido.")
            else:
                print("Tu vida restante es de: ", attacker.life)
                print("La vida restante de", defensor.name,"es de: ", defensor.life)
        time.sleep(2)
        end = 0.1
        while end > 0:
            sound.set_volume(end)
            end -= 0.005
            time.sleep(0.2)
Combate1= Combat(Varok, Leeroy)