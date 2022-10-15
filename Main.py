from Constants import *
from CombatF import *
print(PRINCIPAL_MENU)
play_music(MENU_MUSIC)
a = int(input(CHOOSE_OPTION))
if a == 1:
    print(CHARACTER_SELECTION)
    b = int(input(CHOOSE_CHARACTER))
    fade_music(MENU_MUSIC)
    play_music(BG_MUSIC)
    if b == 1:
        print(STORY_TITLE)
        print(FIRST_DIALOGUE_VAROK)
        print(SECOND_DIALOGUE_VAROK)
        print(FIRST_DECISION_VAROK)
        decision_varok = int(input(TAKE_DECISION))
        if decision_varok == 1:
            print(FIRST_CHOICE_VAROK_1)
            print(SECOND_CHOICE_VAROK_1)
            print(SECOND_DECISION_VAROK)
            decision_varok = int(input(TAKE_DECISION))
            if decision_varok == 1:
                print(FIRST_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        COMBAT = Combat(VAROK, RAEGAR,False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                    elif decision_varok == 2:
                        COMBAT = Combat(VAROK, LEEROY, False)
                        if COMBAT_1 is True:
                            print(DIALOGUE_AFTER_COMBAT_1)
                            os.system('pause')
                            COMBAT = Combat(VAROK, PAYNE, False)
                            if COMBAT_2 is True:
                                print(DIALOGUE_AFTER_COMBAT_2)
                                os.system('pause')
                                COMBAT = Combat(VAROK, ZIREAEL, True)
                                if COMBAT_3 is True:
                                    print(DIALOGUE_AFTER_COMBAT_3)
                                    print(FINAL_DECISION_VAROK)
                                    decision_varok = int(input(TAKE_DECISION))
                                    if decision_varok == 1:
                                        print(FINAL_CHOICE_1)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    elif decision_varok == 2:
                                        print(FINAL_CHOICE_2)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    else:
                                        print(ERROR_1)
                                        print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)

            elif decision_varok == 2:
                print(SECOND_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DIALOGUE_VAROK_EXTRA)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, PODRIC, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        os.system('pause')
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                    elif decision_varok == 2:
                        COMBAT = Combat(VAROK, LEEROY, False)
                        os.system('pause')
                        if COMBAT_1 is True:
                            print(DIALOGUE_AFTER_COMBAT_1)
                            os.system('pause')
                            COMBAT = Combat(VAROK, PODRIC, False)
                            if COMBAT_2 is True:
                                print(DIALOGUE_AFTER_COMBAT_2)
                                os.system('pause')
                                COMBAT = Combat(VAROK, ZIREAEL, True)
                                if COMBAT_3 is True:
                                    print(DIALOGUE_AFTER_COMBAT_3)
                                    print(FINAL_DECISION_VAROK)
                                    decision_varok = int(input(TAKE_DECISION))
                                    if decision_varok == 1:
                                        print(FINAL_CHOICE_1)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    elif decision_varok == 2:
                                        print(FINAL_CHOICE_2)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    else:
                                        print(ERROR_1)
                                        print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)
            elif decision_varok == 3:
                print(THIRD_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, PAYNE, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        COMBAT = Combat(VAROK, PAYNE, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)
            else:
                print(ERROR_1)
                print(ERROR_2)
        elif decision_varok == 2:
            print(SECOND_CHOICE_VAROK_1)
            print(SECOND_DECISION_VAROK)
            decision_varok = int(input(TAKE_DECISION))
            if decision_varok == 1:
                print(FIRST_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, PAYNE, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                    elif decision_varok == 2:
                        COMBAT = Combat(VAROK, LEEROY, False)
                        if COMBAT_1 is True:
                            print(DIALOGUE_AFTER_COMBAT_1)
                            os.system('pause')
                            COMBAT = Combat(VAROK, PAYNE, False)
                            if COMBAT_2 is True:
                                print(DIALOGUE_AFTER_COMBAT_2)
                                os.system('pause')
                                COMBAT = (VAROK, ZIREAEL, True)
                                if COMBAT_3 is True:
                                    print(DIALOGUE_AFTER_COMBAT_3)
                                    print(FINAL_DECISION_VAROK)
                                    decision_varok = int(input(TAKE_DECISION))
                                    if decision_varok == 1:
                                        print(FINAL_CHOICE_1)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    elif decision_varok == 2:
                                        print(FINAL_CHOICE_2)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    else:
                                        print(ERROR_1)
                                        print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)

            elif decision_varok == 2:
                print(SECOND_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DIALOGUE_VAROK_EXTRA)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, PODRIC, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = (VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                    elif decision_varok == 2:
                        COMBAT = Combat(VAROK, LEEROY, False)
                        if COMBAT_1 is True:
                            print(DIALOGUE_AFTER_COMBAT_1)
                            os.system('pause')
                            COMBAT = Combat(VAROK, PAYNE, False)
                            if COMBAT_2 is True:
                                print(DIALOGUE_AFTER_COMBAT_2)
                                os.system('pause')
                                COMBAT = Combat(VAROK, ZIREAEL, True)
                                if COMBAT_3 is True:
                                    print(DIALOGUE_AFTER_COMBAT_3)
                                    print(FINAL_DECISION_VAROK)
                                    decision_varok = int(input(TAKE_DECISION))
                                    if decision_varok == 1:
                                        print(FINAL_CHOICE_1)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    elif decision_varok == 2:
                                        print(FINAL_CHOICE_2)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    else:
                                        print(ERROR_1)
                                        print(ERROR_2)
                    else:
                        print(ERROR_1)
                        print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)
            elif decision_varok == 3:
                print(THIRD_CHOICE_VAROK_2)
                print(THIRD_DIALOGUE_VAROK)
                print(THIRD_DECISION_VAROK)
                decision_varok = int(input(TAKE_DECISION))
                if decision_varok == 1:
                    print(FIRST_CHOICE_VAROK_3)
                    COMBAT = Combat(VAROK, LEEROY, False)
                    if COMBAT_1 is True:
                        print(DIALOGUE_AFTER_COMBAT_1)
                        os.system('pause')
                        COMBAT = Combat(VAROK, PAYNE, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)
                elif decision_varok == 2:
                    print(SECOND_CHOICE_VAROK_2)
                    print(FOURTH_DECISION_VAROK)
                    decision_varok = int(input(TAKE_DECISION))
                    if decision_varok == 1:
                        print(DIALOGUE_AFTER_4_DECISION)
                        COMBAT = Combat(VAROK, RAEGAR, False)
                        if COMBAT_2 is True:
                            print(DIALOGUE_AFTER_COMBAT_2)
                            os.system('pause')
                            COMBAT = Combat(VAROK, ZIREAEL, True)
                            if COMBAT_3 is True:
                                print(DIALOGUE_AFTER_COMBAT_3)
                                print(FINAL_DECISION_VAROK)
                                decision_varok = int(input(TAKE_DECISION))
                                if decision_varok == 1:
                                    print(FINAL_CHOICE_1)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                elif decision_varok == 2:
                                    print(FINAL_CHOICE_2)
                                    print(DIALOGUE_FINAL)
                                    fade_music(BG_MUSIC)
                                else:
                                    print(ERROR_1)
                                    print(ERROR_2)

                    elif decision_varok == 2:
                        COMBAT = Combat(VAROK, LEEROY, False)
                        if COMBAT_1 is True:
                            print(DIALOGUE_AFTER_COMBAT_1)
                            os.system('pause')
                            COMBAT = Combat(VAROK, PAYNE, False)
                            if COMBAT_2 is True:
                                print(DIALOGUE_AFTER_COMBAT_2)
                                os.system('pause')
                                COMBAT = Combat(VAROK, ZIREAEL, True)
                                if COMBAT_3 is True:
                                    print(DIALOGUE_AFTER_COMBAT_3)
                                    print(FINAL_DECISION_VAROK)
                                    decision_varok = int(input(TAKE_DECISION))
                                    if decision_varok == 1:
                                        print(FINAL_CHOICE_1)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    elif decision_varok == 2:
                                        print(FINAL_CHOICE_2)
                                        print(DIALOGUE_FINAL)
                                        fade_music(BG_MUSIC)
                                    else:
                                        print(ERROR_1)
                                        print(ERROR_2)
                    else:
                        print(ERROR_1)
                        print(ERROR_2)

                else:
                    print(ERROR_1)
                    print(ERROR_2)

            else:
                print(ERROR_1)
                print(ERROR_2)
        else:
            print(ERROR_1)
            print(ERROR_2)


elif a == 2:
    print(QUIT)
else:
    print(ERROR_1)
    print(ERROR_2)