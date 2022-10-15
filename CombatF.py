# Clase combate
# Alex
from random import *
import os
from Constants import *
import pygame, sys
from pygame.locals import *
import time 
pygame.init()


class Combat:
    def __init__(self, attacker, defensor, combat_3):
        MANA = 9
        WIN = False
        RETRY = False
        LIFE_PERCENT = defensor.life * 0.45
        FINAL = 0
        attacker.restart_stats()
        defensor.restart_stats()
        fade_music(BG_MUSIC)
        play_music(COMBAT_MUSIC)
        while WIN == False:
            if RETRY == True:
                RETRY = False
                FINAL = 0
                print("Parece que has sido derrotado...\
                    \nInténtalo nuevamente")
                attacker.restart_stats()
                defensor.restart_stats()
                COMBAT_MUSIC.play()
                COMBAT_MUSIC.set_volume(0.05)
                MANA = 9
            while attacker.life > 0 and defensor.life > 0:
                MENU = 0
                MANA += 2
                if attacker.char_class == "Orc warrior":
                    print("\nOrco guerrero ", attacker.name,"\n")
                    print(ORC_MENU)

                elif attacker.char_class == "Elf mage":
                    print("\nMago Elfo ", attacker.name,"\n")
                    print(ELF_MENU)

                elif attacker.char_class == "Human paladin":
                    print("\nPaladín humano ", attacker.name,"\n")
                    print(HUMAN_MENU)
                print("Mana disponible: ", MANA)
                while MENU == 0:

                    print("\nIngrese la acción a realizar\n")
                    MENU = str(input())
                    print("\n")
                    if MENU != "1" and MENU != "2" and  MENU != "3":
                        print("\nIngrese una opción correcta \n")
                        MENU = 0
                        time.sleep(1)
                        os.system('pause')
                 
                if MENU == "1":
                    if MANA >= 7:
                        ABILITY_SOUND = pygame.mixer.Sound(attacker.ab1_sound)
                        ABILITY_SOUND.set_volume(0.1)
                        ABILITY_SOUND.play()
                        print(MENU_SEPARATOR_TOP)
                        print(attacker.name, "ha utilizado la habilidad: φ", attacker.ab1_name,"φ")
                        TOTAL_DAMAGE = attacker.ab1_damage - defensor.armor
                        defensor.life = defensor.life - TOTAL_DAMAGE
                        print(MENU_SEPARATOR_TOP)
                        print(defensor.name, "❌ ha recibido el ataque ❌, con un daño total de: ",
                            TOTAL_DAMAGE)
                        print(MENU_SEPARATOR_TOP,"\n")
                        MANA-= 7
                    else:
                        print(MENU_SEPARATOR_TOP)
                        print("¡No tienes maná suficiente para utilizar la habilidad!")
                        print(MENU_SEPARATOR_TOP,"\n")
                        NO_MANA_SOUND.play()

                elif MENU == "2":
                    if MANA >= 5:
                        ABILITY_SOUND = pygame.mixer.Sound(attacker.ab2_sound)
                        ABILITY_SOUND.set_volume(0.1)
                        ABILITY_SOUND.play()
                        print(MENU_SEPARATOR_TOP)
                        print(attacker.name, "ha utilizado la habilidad: Ω", attacker.ab2_name,"Ω")
                        TOTAL_DAMAGE = attacker.ab2_damage - defensor.armor
                        defensor.life = defensor.life - TOTAL_DAMAGE
                        print(MENU_SEPARATOR_TOP)
                        print(defensor.name, "❌ ha recibido el ataque ❌, con un daño total de: ",
                            TOTAL_DAMAGE)
                        print(MENU_SEPARATOR_TOP,"\n")
                        MANA -= 5
                    else:
                        print(MENU_SEPARATOR_TOP)
                        print("¡No tienes energía suficiente para utilizar la habilidad!")
                        print(MENU_SEPARATOR_TOP,"\n")
                        NO_MANA_SOUND.play()

                elif MENU == "3":

                    ABILITY_SOUND = pygame.mixer.Sound(attacker.basic_sound)
                    ABILITY_SOUND.set_volume(0.1)
                    ABILITY_SOUND.play()
                    print(MENU_SEPARATOR_TOP)
                    print(attacker.name, "⚔️  ha realizado un ataque básico   ⚔️")
                    TOTAL_DAMAGE = attacker.strenght - defensor.armor
                    defensor.life = defensor.life - TOTAL_DAMAGE
                    print(MENU_SEPARATOR_TOP)
                    print(defensor.name, "❌ a recibido el ataque ❌, con un daño total de: ",
                        TOTAL_DAMAGE)
                    print(MENU_SEPARATOR_TOP,"\n")

                if defensor.life > 0 and defensor.life <= LIFE_PERCENT and combat_3 is True:
                
                        print(MENU_SEPARATOR_TOP)
                        print("El combate ha terminado.")
                        print(MENU_SEPARATOR_TOP,"\n")
                        FINAL = 1
                        defensor.life = 0
                        WIN = True
                elif defensor.life > 0 and FINAL == 0:

                    time.sleep(3)
                    RANDOM_NUM = randint(1, 10)

                    if RANDOM_NUM >= 6:

                        ABILITY_SOUND = pygame.mixer.Sound(defensor.ab1_sound)
                        ABILITY_SOUND.set_volume(0.1)
                        ABILITY_SOUND.play()
                        print(MENU_SEPARATOR_TOP)
                        TOTAL_DAMAGE = defensor.ab1_damage - attacker.armor
                        attacker.life -= TOTAL_DAMAGE
                        print(defensor.name, "ha utilizado la habilidad: φ", defensor.ab1_name,"φ")
                        print(MENU_SEPARATOR_TOP)
                        print("❌ Has recibido el ataque ❌, con un daño total de:", TOTAL_DAMAGE)
                        print(MENU_SEPARATOR_TOP,"\n")
                        time.sleep(3)

                    elif RANDOM_NUM <= 5:

                        ABILITY_SOUND = pygame.mixer.Sound(defensor.ab2_sound)
                        ABILITY_SOUND.set_volume(0.1)
                        ABILITY_SOUND.play()
                        print(MENU_SEPARATOR_TOP)
                        TOTAL_DAMAGE = defensor.ab2_damage - attacker.armor
                        attacker.life -= TOTAL_DAMAGE
                        print(defensor.name, "ha utilizado la habilidad: Ω", defensor.ab2_name,"Ω")
                        print(MENU_SEPARATOR_TOP)
                        print("❌ Has recibido el ataque ❌, con un daño total de:", TOTAL_DAMAGE)
                        print(MENU_SEPARATOR_TOP,"\n")
                        time.sleep(3)
                
                elif defensor.life <= 0:
                    print("+=============================+")
                    print("    Has matado a ", defensor.name)
                    print("+=============================+\n")
                    WIN = True

                if attacker.life <= 0:
                    print(MENU_SEPARATOR_TOP)
                    print("                       †                            ")
                    print("†Tus puntos de vida han llegado a 0! Has perdidido.†")
                    print("                       †                            ")
                    print(MENU_SEPARATOR_TOP,"\n")
                    END = 0.05
                    while END > 0:
                        COMBAT_MUSIC.set_volume(END)
                        END -= 0.001
                        time.sleep(0.05)
                    COMBAT_MUSIC.fadeout(2000)
                    DEATH_SOUND = pygame.mixer.Sound("sounds/death_sound.mp3")
                    DEATH_SOUND.play()
                    DEATH_SOUND.set_volume(0.1)
                    time.sleep(8)
                    RETRY = True
                if FINAL == 0 and defensor.life > 0 and attacker.life > 0:
                    print(MENU_SEPARATOR_TOP)
                    print("Tu vida restante es de: ✚ ", attacker.life,"✚")
                    print("La vida restante de", defensor.name,"es de: ✚ ", defensor.life,"✚")
                    print(MENU_SEPARATOR_TOP,"\n")

        fade_music(COMBAT_MUSIC)
        play_music(BG_MUSIC)
#Combate = Combat(VAROK, LEEROY, False)