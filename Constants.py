#Personajes - constantes
from Human import *
from Elf import *
from Orc import *
import pygame,sys
from pygame.locals import *
import time
pygame.init()
ORC_MENU =   "+------------------------+\
            \n|     Acciones           |\
            \n+========================+\
            \n|   1-Corte espiral   φ  |\
            \n|       Coste = 7        |\
            \n+------------------------+\
            \n|   2-Grito de guerra  Ω |\
            \n|       Coste = 5        |\
            \n+------------------------+\
            \n|   3-Ataque básico  ⚔️   |\
            \n+------------------------+"

ELF_MENU =  "+--------------------------+\
            \n|     Acciones             |\
            \n+==========================+\
            \n|   1-Orbe arcano          |\
            \n+--------------------------+\
            \n|   2-Lluvia de estrellas  |\
            \n+--------------------------+\
            \n|   3-Ataque básico        |\
            \n+--------------------------+"

HUMAN_MENU =  "+---------------------+\
             \n|        Ataques      |\
             \n+=====================+\
             \n|   1-Filo tormenta   |\
             \n+---------------------+\
             \n|   2-Bendición solar |\
             \n+---------------------+\
             \n|   3-Ataque básico   |\
             \n+---------------------+"

MENU_SEPARATOR_TOP ="+===============================================================+"
COMBAT_MUSIC = pygame.mixer.Sound("sounds/battle_music.mp3")
NO_MANA_SOUND = pygame.mixer.Sound("sounds/orc_nomana.mp3")
NO_MANA_SOUND.set_volume(0.4)
MENU_MUSIC = pygame.mixer.Sound("sounds/main theme.mp3")
BG_MUSIC = pygame.mixer.Sound("sounds/rpg music.mp3")
def play_music(music):
    time.sleep(2)
    music.play(-1)
    music.set_volume(0.07)
def fade_music(music):
    time.sleep(3)
    END = 0.05
    while END > 0:
        music.set_volume(END)
        END -= 0.001
        time.sleep(0.05)
    music.fadeout(1000)

VAROK = Orco()
LEEROY = Human()
ZIREAEL = Elf()
PODRIC = Human("Podric")
PAYNE = Human("Payne")
RAEGAR = Elf("Raegar")

PRINCIPAL_MENU = ("+===========================+\n"
                  "|  Cuentos de Astharok      |\n"
                  "+===========================+\n"
                  "| 1-    Iniciar juego       |\n"
                  "+---------------------------+\n"
                  "| 2-    Salir del juego     |\n"
                  "+---------------------------+")
CHOOSE_OPTION = "Elija una opción: "

CHOOSE_CHARACTER = "Elija un personaje: "

CHARACTER_SELECTION = ("+==============================================================================+\n"
                       "|                               ELIJA SU PERSONAJE                             |\n"
                       "+==============================================================================+\n"

                       "+==============================================================================+\n"
                       "| 1-                        Varok, el matagigantes                             |\n"
                       "+------------------------------------------------------------------------------+\n"
                       "| Un valiente guerrero orco perteneciente al legendario reino de Orgrimmar.    |\n"
                       "| Su lealtad esta ligada a su pueblo, siendo uno de los comandantes mas        |\n"
                       "| valiosos de las fuerzas de guerra unidas del Norte.                          |\n"
                       "+==============================================================================+")

STORY_TITLE = "La Historia de Varok, el matagigantes.\n"

FIRST_DIALOGUE_VAROK = ("Era una mañana fria en el Norte, la vanguardia habia partido hacia unas dos horas, planeaban\n"
                        "recuperar el Fuerte Negro que se encontraba en dirección al sureste. Los Harranhim habian\n"
                        "mejorado su logistica y nos habian tomado por sorpresa. Hace 2 meses que nos vimos forzados\n"
                        "a retroceder y hoy, por fin, es nuestro turno de contratacar, de mi y mis camaradas depende\n"
                        "el resultado de esta mision.\n"
                        "\n\n"
                        "-Soldado orco: “Comandante Varok! El resto de las tropas esta listo para partir. Esperamos\n"
                        "sus ordenes.”\n"
                        "-Lord Varok: “Partiremos en 5 minutos, quiero a las unidades de avanzada y arqueros listos,\n"
                        "tomaremos la ofensiva por los bosques en caso de que haya exploradores merodeando la zona.”\n"
                        "-Soldados: “Si, señor!”\n"
                        "\n\n")

SECOND_DIALOGUE_VAROK = ("El ejercito avanzo por el bosque encantado. Varok se sentía atemorizado, tenia el peso de\n"
                         "todas las vidas que se arriesgaban en la misión. Finalmente llegaron a la desembocadura del\n"
                         "rio, bajando por el bosque, cuando de repente encontraron un explorador de Harranhim.\n"
                         "\n"
                         "El explorador parecía haber encontrado las pertenencias de uno de los soldados de la\n"
                         "vanguardia orca, se veía un poco confundido y también asustado, generalmente los\n"
                         "exploradores humanos eran espías implacables, pero este al tener a todo el ejercito orco\n"
                         "en frente, parece que el frio del norte le había congelado la lengua y lo hubiera\n"
                         "paralizado. Incluso parecía un desertor, pues no aparecía estar armado, o al menos no\n"
                         "a la vista.\n"
                         "En ese momento uno de los soldados de la unidad de los trolls, el llamado\n"
                         "Trundle destructor de icebergs, bajo de su bisonte, puso su garrote de hielo sobre el\n"
                         "pecho del chico, si, el mismo garrote que se decia que podia ocasionar un cataclismo\n"
                         "del explorador y exclamo.\n"
                         "\n\n"
                         "-Trundle: “Vaya vaya, que tenemos aquí, un humano espía, apartado de la manada!”\n"
                         "-Trundle: “Esta rata inmunda ha matado a uno de los nuestros, quien sabe si no han sido "
                         "emboscados todos ya.”\n"
                         "-Todos. “Mátenlo! Córtenle la cabeza!”. Gritaron todos.\n"
                         "-“Lord Vol’jin!”. Dijo Trundle, que hacemos con este humano.\n"
                         "\n\n"
                         "Lord vol’jin. Líder de la tribu troll. Sumamente orgulloso y sin piedad. Era obvio que ese\n"
                         "muchacho estaría muerto antes de soltar una palabra. Y decían que los orcos son los menos\n"
                         "inteligentes, y aun así, un orco sabe cuando dejar vivo a un enemigo y cuando no.\n"
                         "En ese momento Vol’jin hablo.\n"
                         "\n\n"
                         "-“Vuelve a la formación Destructor de Icebergs, serás una leyenda en cuentos y canciones,\n"
                         "pero aquí eres un soldado a mi cargo.”\n"
                         "-“Lord Varok decidirá que será del espía. Siendo que el es el comandante de esta misión.”\n"
                         "\n\n"
                         "Lord Vol’jin sumamente orgulloso, no idolatraba a nadie con su mismo título, creo que nunca\n"
                         "idolatro ni siquiera a su Gran Jarl, y aun así, le había dado la palabra a Varok, quien por\n"
                         "supuesto, la tomo.\n")

FIRST_DECISION_VAROK = ("+=====================================================================+\n"
                        "| 1)	“Dime tu nombre”                                              |\n"
                        "+---------------------------------------------------------------------+\n"
                        "| 2)	“Estas en un terrible aprieto. Como murió ese camarada mío?   |\n"
                        "|       Responde ahora mismo.”                                        |\n"
                        "+=====================================================================+")

FIRST_CHOICE_VAROK_1 = ("\nNo da respuesta alguna de lo asustado que esta. En ese momento dijo.\n"
                        "-“Estaba huyendo, perdi a mi montura y subi costa arriba para poder vendarme las heridas.”\n")

SECOND_CHOICE_VAROK_1 = ("\n-Chico: “Cuando cruce el rio, vi el cuerpo en la nieve, solo le quite su comida,\n"
                         "lo juro!”\n" 
                         "-Lord Varok: “Si murió aquí, los tuyos lo mataron.”\n"
                         "-Chico: “No tengo idea de eso. No se nada mas.”\n"
                         "-Lord Varok: “Eres consciente de que si no me dices morirás?\n"
                         "-Chico: “Si, y no le temo a la muerte. Solo los dioses saben si soy culpable o no.”\n"
                         "-Chico: “Así que vamos! Golpea fuerte, Lord orco.”\n"
                         "Varok observo al chico por un segundo, le impresionaba su valentía a pesar de estar rodeado\n"
                         "de un ejército. Sin embargo, pensó en su decisión y dijo:\n"
                         "-“Confisquen todas sus pertenencias y revisen si esta armado.”\n"
                         "-Soldado orco: “Si, señor. Que hacemos con el?”.\n"
                         "\n\n"
                         "Esa era la gran pregunta, ¿qué hacer con él? No podía dejarlo libre, pero matarlo no sería\n"
                         "una buena opción tampoco. Quizá tiene información valiosa, o quizá no.\n"
                         "En ese momento, varok pensó, no podía dejarlo libre, pero matarlo no sería una buena opción\n" 
                         "tampoco. Quizá tiene información valiosa, o quizá no.\n")

SECOND_DECISION_VAROK = ("+=====================================================================================+\n"
                         "| 1)	“Déjenlo libre”                                                               |\n"
                         "+-------------------------------------------------------------------------------------+\n"
                         "| 2)	“Captúrenlo, lo llevaremos prisionero. Puede que tenga información valiosa.”  |\n"
                         "+-------------------------------------------------------------------------------------+\n"
                         "|  3)	“Mátenlo, si lo dejamos libre podría alertar a sus camaradas.“                |\n"
                         "+=====================================================================================+")

FIRST_CHOICE_VAROK_2 = ("Lord Varok decidio dejar escapar al chico. Sus hombres no lo tomaron bien, pero aun asi\n"
                        "el era la maxima autoridad, y se hacia lo que el decia.\n")

SECOND_CHOICE_VAROK_2 = ("Lord Varok perdono la vida del chico y lo tomo prisionero, pues creia que mantenerlo con vida"
                         "le serviria en el futuro.\n"
                         "Minutos mas tarde el chico se le acerca y le dice:\n"
                         "\n\n"
                         "-“Me salvo la vida, Ser.”\n" 
                         "-“No soy un caballero chico. Y no te salve la vida, simplemente decidí que no morirás hoy.”\n"
                         "-“Lo siento, había olvidado ese detalle, los orcos no son caballeros, pero sabe que Señor,\n"
                         "mostrar clemencia es un acto que pocos caballeros muestran y usted la mostro, lo hace mas\n"
                         "caballero que a otros\n"
                         "\n\n"
                         "A pesar de no estar en las costumbres de los orcos, las palabras del chico prisionero por "
                         "un momento lo animaron, por eso no le molesto.”\n" 
                         "\n\n"
                         "-“Ben, Ser.\n"
                         "-“¿Qué?”\n"
                         "-“Mi nombre, Ben, se lo debía. No pensé que importaría decirlo si de todas formas iba\n"
                         "a morir”.\n"
                         "\n\n"
                         "A Varok le causo gracia su comentario, pues en parte tenía razón, no importa la información\n"
                         "que des, si el que dicta la sentencia te considera hombre muerto, es algo que el aprendió\n"
                         "desde joven. Después de eso se alejó del chico y notifico a las tropas que había que\n"
                         "emprender viaje, el sol se estaba escondiendo y todavía faltaba un largo recorrido.\n")

THIRD_CHOICE_VAROK_2 = ("Lord Varok decidio matar al chico, preferia cargar con la muerte de un joven humano que\n"
                        "correr el riesgo de ser emboscado en una trampa y perder a más hermanos.\n")

THIRD_DIALOGUE_VAROK = ("Entonces Varok y sus soldados siguieron camino. Había caído la noche cuando cruzaron todo el\n"
                        "bosque encantado y debían acampar, por supuesto debían tomar la cautela necesaria para no\n"
                        "alertar a sus enemigos sobre su llegada.\n"
                        "Al otro día, decidieron seguir avanzando al alba. Varok no había dormido de todas maneras,\n"
                        "pues un comandante debe estar siempre atento ante todo peligro, pero no solo eso, el hecho\n"
                        "de haber encontrado el cadáver de ese camarada de la vanguardia, lo dejaba pensando,\n"
                        "no recibieron noticias, pues ya deberían haber llegado y haber armado asentamiento. Siendo\n"
                        "las tropas de reconocimiento, tendrían que haber advertido en caso de algún peligro próximo\n"
                        "al fuerte.\n"
                        "De todas maneras, con mas dudas que certezas, Varok simplemente dio la orden y emprendieron\n"
                        "viaje de nuevo.\n"
                        "Llegaron al llamado camino de las águilas, se veía todo muy tranquilo, y eso no pintaba\n"
                        "bien. Aquí es donde sembraba la duda en la cabeza de Varok, ¿Debo tomar el camino de las\n"
                        "águilas?\n"
                        "Quizá sea una trampa, y nos están preparando una emboscada al final del camino. Por otro\n"
                        "lado estaba el camino a través de las montañas, mas riesgoso pero ese probablemente\n"
                        "libre de peligro enemigo.\n"
                        "-“Lord comandante!”\n"
                        "-“Por dónde vamos?”\n")

THIRD_DIALOGUE_VAROK_EXTRA = ("En ese momento, el chico Ben esposado a un palo y acompañado de un troll, le dice:\n"
                              "-“Ser, puede que el camino de las águilas sea una trampa, he oído que el comandante\n"
                              "Victaryon esta defendiendo el fuerte, le gustan las emboscadas, es su estrategia\n"
                              "favorita.”\n"
                              "En ese momento el troll golpeo al chico.\n"
                              "-“Quien te has creído escoria?! Solo podrás hablar si se te lo permite.”\n"
                              "Lord Varok pregunto:\n"
                              "-“Chico, por que me dices esto? Debería creerte? Hasta donde sé, eres uno de ellos.”\n"
                              "-“Era uno de ellos, Ser.”\n"
                              "-“Y no estoy pretendiendo llevarlos a una trampa, ni tampoco salvarme mi propio\n"
                              "pellejo,simplemente considero que no me interesa lo que el reino de Harranhim tenga\n"
                              "que ofrecer.\n"
                              "Lord Varok pensó lo que aquel chico le estaba diciendo, y tomo una decisión.\n")

THIRD_DECISION_VAROK = ("+=======================================================================================+\n"
                        "| 1)	“Sigamos por el camino de las águilas. No debemos arriesgarnos en hacer         |\n"
                        "|     caminos riesgosos.“                                                               |\n"                                                          
                        "+---------------------------------------------------------------------------------------+\n"
                        "| 2)	“Mejor desviémonos por las Montañas de la Luna, así podremos tomar por          |\n"
                        "|      sorpresa a nuestros enemigos y evitaremos trampas por el camino.“                |\n"
                        "+=======================================================================================+")

FIRST_CHOICE_VAROK_3 = ("El ejercito decidió ir en dirección hacia al este por el camino de las águilas, hasta llegar\n"
                        "a fuerte terror. El camino se hacia cada vez mas silencioso, ni siquiera las águilas que\n"
                        "suelen frecuentar el campo se escuchaban. En ese momento, uno de los exploradores diviso\n"
                        "la bajada del camino donde se dividía en dos, ellos debían tomar el camino hacia la\n"
                        "izquierda, para llegar a la ofensiva contra el fuerte. Fue en ese momento cuando, el\n"
                        "explorador y la división de bisontes escucharon un ruido a su derecha. Un árbol inmenso\n"
                        "cayo sobre la unidad que iba al frente y luego una flecha atravesó al explorador que iba\n"
                        "adelante. En ese momento, supieron que los habían emboscado.\n" 
                        "Empezaron a salir soldados de Harranhim de la arboleda que tenían a su derecha. Y por la\n" 
                        "izquierda, en las enormes rocas que había, arqueros, disparando flechas.\n" 
                        "Los orcos y trolls desenvainaron hachas, garrotes y mandobles. Varok mismo bajo de su\n" 
                        "bisonte y desenvaino su gran hacha. Diviso a su primer enemigo, parecía un caballero\n" 
                        "común y corriente, pero en vez de una espada, llevaba un mandoble, algo no muy común entre\n" 
                        "los caballeros.\n" 
                        "En ese momento Varok había entrado en un duelo decisivo.\n")

SECOND_CHOICE_VAROK_3 = ("Avanzaron por la montaña, debían cruzar por un camino que se llama el Nido de Águilas, a\n"
                         "través de las dos montañas mas grandes. Ni bien llegaron al nido, Lord Varok recordó la\n" 
                         "leyenda de la tribu de la luna.\n"
                         "Una tribu que rinde culto a la diosa lunar. Si bien eran mas saqueadores que otra\n"
                         "cosa, nadie puede pisar las montañas de la luna sin pagar con sangre o rendirle tributo\n"
                         "a la diosa lunar, ese era como un dicho popular, se sabía en todo el continente.\n"
                         "Había un silencio medio inquieto, por un segundo el viento que aullaba a través de la\n"
                         "altura de las montañas no se sintió y fue en ese momento cuando la famosa tribu apareció,\n"
                         "nolos dejaron retroceder ni avanzar, los habían seguido y no se habían dado cuenta. Se les\n"
                         "acerco uno de ellos y exclamo:\n"
                         "\n\n"
                         "-“Ustedes, no pasar! Mostrad respetos a la diosa!”. Dijo el hombre.\n"
                         "La cosa quedaba bien clara, quería que diéramos una ofrenda, pero la cuestión es, cual\n"
                         "seria.\n"
                         "-“Que demanda su diosa?”. Pregunto Lord Varok.\n"
                         "-“Lo que quieren todos los hombres y dioses, Comida y Oro mi señor orco.” Dijo el hombre.\n"
                         "-“Nuestra diosa representa la naturaleza, la fertilidad y la codicia. Tres cosas que\n"
                         "van bien.”\n"
                         "Varok sabia que o daban sus pertenencias o correría la sangre, y tampoco tenia el lujo de\n"
                         "poder volver en el camino, solo había dos opciones, cual iba a tomar, era un\n"
                         "misterio para todos.\n")

FOURTH_DECISION_VAROK = ("+=======================================================================================+\n"
                         "| 1)	“Esta bien, tomad nuestro oro y algunas provisiones.“                            |\n"                                                          
                         "+---------------------------------------------------------------------------------------+\n"
                         "| 2)	“No pienso darte nada. Necesitamos nuestras provisiones.“                        |\n"
                         "+=======================================================================================+")

DIALOGUE_AFTER_4_DECISION = ("Les permiten pasar el nido de águilas y llegar hasta el fuerte. Terminan llegando al\n"
                             "lugar que tanto ansiaban, el fuerte negro, y tenían la ventaja para desencadenar un\n"
                             "ataque sorpresa inclusive. En ese momento logran emboscar a los guardias que\n"
                             "custodiaban el fuerte, pues, no se esperaban que atacaran por el norte. Los soldados\n"
                             "no estaban preparados y cedieron terreno fácilmente, lo que les hizo mas fácil a los\n"
                             "orcos tomar el fuerte y avanzar hasta el gran patio del fuerte, momento en el cual,\n"
                             "aparecieron una oleada de paladines, listos para defender la entrada al patio.\n"
                             "En ese momento se le ocurrió un plan a Varok para avanzar. La unidad de avanzada\n"
                             "emprendió una carga y dio paso a que el combate empezara. Varok desenvaino su hacha\n"
                             "una vez más y se abrió paso con la carga. Cuando la carga impacto, Varok agarro su\n"
                             "hacha con fuerza para impactar con el paladín que resistía en la entrada al patio\n"
                             "del fuerte. La victoria de ese combate dependería si había tomado o no\n"
                             "una buena decisión.\n")

DIALOGUE_AFTER_COMBAT_1 = ("Varok logro derrotar al caballero en combate singular, logro ayudar a las tropas de\n" 
                           "los trolls, sin embargo la unidad de avanzada conformada por sus hombres estaba en\n" 
                           "aprietos, fue en ese momento que se escucho un grito desde la arboleda del cazador al\n" 
                           "oeste. La vanguardia que había partido mucho antes que ellos, había hecho aparición,\n" 
                           "y venia en una carga en dirección hacia la batalla. En ese momento Varok, dio un grito\n" 
                           "de guerra y animo a las tropas a avanzar. A pesar de las vidas perdidas, los orcos y\n" 
                           "los trolls lograron contratacar y consiguieron la victoria.\n" 
                           "Siguieron avanzando hasta llegar a la gran puerta del Fuerte y ahí irrumpieron dentro,\n" 
                           "los soldados los estaban esperando. Ellos solo tenían un objetivo, derrotar al comandante\n" 
                           "Victaryon, ya sea que lo capturen o lo maten.\n" 
                           "Varok tenía planeado ir con la unidad de asesinos y arqueros hacia el frente y acabar\n" 
                           "con la vida del comandante en un abrir y cerrar de ojos, sin embargo, cruzar la\n" 
                           "vanguardia enemiga llena de paladines, no les dejaba.\n" 
                           "En ese momento solo se le ocurrió una cosa, aunque arriesgada, podría funcionar. "
                           "La unidad de avanzada emprendió una carga y dio paso a que el combate empezara. Varok "
                           "desenvaino su hacha una vez mas y se abrió paso con la carga. Cuando la carga impacto, "
                           "agarro su hacha con fuerza para impactar con el paladín que resistía en la entrada "
                           "al patio del fuerte. La victoria de ese combate dependería si había tomado o no\n"
                           "una buena decisión.\n")
DIALOGUE_AFTER_COMBAT_2 = ("Varok y sus hombres logran llegar al patio, los arqueros se instalan en las torres, la\n"
                           "batalla parecía ganada, pero, cayeron refuerzos. Varok ve como sus tropas van cayendo\n"
                           "uno a uno. A Lord Vol’jin lo habían alcanzado las flechas enemigas, sus guerreros siendo\n"
                           "pasados por lanza y espada. Parecía no haber esperanza pero, luego recordó el estruendo\n"
                           "mágico que podía hacer el garrote de Trundle, el destructor de icebergs y en ese momento\n"
                           "supo que había una última oportunidad.\n"
                           "-Soldado orco: “Lord comandante! Estamos rodeados, es nuestro fin.”\n"
                           "-Lord Varok: “No. No hemos llegado hasta aquí por nada. Perdimos a muchos de los\n"
                           "nuestros, ellos sacrificaron sus vidas por esta causa.”\n"
                           "-Lord Varok: “Tengo un ultimo plan.”\n"
                           "-Lord Varok: “Trundle! Necesitamos tu fuerza y tu arma”.\n"
                           "-Trundle: “De acuerdo.“\n"
                           "Varok explica su plan y confía en sus hombres plenamente para ejecutarlo, en ese\n"
                           "momento se preparan.\n"
                           "-Lord Varok: “ORCOS DE ORGRIMMAR, TROLLS DE DRAKKARI. UNIDOS! Esta será la ultima\n"
                           "carga de todas.”\n"
                           "Varok confiaba en que el estruendo del garrote impactara sobre el fuerte y lograran\n"
                           "poder dividir a las fuerzas enemigas. Confiaba en sus hombres para que completaran\n"
                           "la misión, mientras, él debía enfrentar al comandante Victaryon el mismo.\n"
                           "Se armo con su hacha y junto a sus hombres desencadeno la ultima batalla para recuperar\n"
                           "el fuerte negro.\n"
                           "Trundle golpeo con su garrote al piso del fuerte, la vanguardia cargo y en ese momento\n"
                           "el estruendo fue tan fuerte, que logro dividir a las tropas enemigas y causar\n"
                           "una distracción. Victaryon no se lo vio venir, y fue cuando Varok se lanzo hacia el\n"
                           "con su hacha, y comenzó realmente la batalla decisiva por el Fuerte negro.\n")

DIALOGUE_AFTER_COMBAT_3 = ("-“Hazlo, orco. Mátame. Demuestra tu naturaleza.”\n"
                           "-“No importa si muero. Mi patria saldrá victoriosa al final. No por mí, por Harranhim.”\n")

FINAL_DECISION_VAROK = ("+=======================================================================================+\n"
                        "| 1)	“Perdonarlo. Lo tomas prisionero.“                                              |\n"                                                          
                        "+---------------------------------------------------------------------------------------+\n"
                        "| 2)	“Acabar con él.“                                                                |\n"
                        "+=======================================================================================+")
FINAL_CHOICE_1 = ("El pueblo de Orgrimmar es justo, cuando debe serlo, y seras llevado como prisionero esta vez.\n"
                  "Varok lo golpea con el hacha y lo deja inconsciente.\n"
                  "-Lord Varok: “Llevenselo a la celda del fuerte. Me ocupare de esto mas tarde.\n"
                  "-Soldado orco: “Si, señor!“\n")
FINAL_CHOICE_2 = ("\n-Lord Varok: “Cualquier especie es capaz de razonar y entender cuando se debe perdonar a una "
                  "persona, y tu no mereces ser perdonado.“\n"
                  "-Lord Varok: “Lord comandante Victaryon, en el nombre del Orgrimmar y el norte, lo condeno a "
                  "muerte.\n"
                  "Varok levanto su hacha y aplico un corte limpio, termino con la vida del comandante humano. Si"
                  "bien es algo duro una sentencia, Varok siempre creia que el que dicta la sentencia debe "
                  "ejecutarla, sino no seria capaz de ser alguien justo y de honor. Algo que aprendio en Orgrimmar"
                  "desde muy joven.")

DIALOGUE_FINAL = ("En ese momento, vio como sus tropas lograron arrinconar a los enemigos. Aun se escuchaban\n"
                  "el sonido de las armas danzando, pero el resultado era claro, habían ganado.\n"
                  "-“¡Esta batalla termina ahora!”. Exclamo Lord Varok\n"
                  "-“Soldados, capturen a los restantes. Este asedio ha terminado. Hemos ganado.”\n"
                  "En el pasar de los días, las tropas enemigas restantes escaparon y el fuerte negro\n"
                  "empezó a ser fortificado, la próxima vez que vengan, estaremos preparados. Por lo pronto\n"
                  "tenían que quemar y rendir tributo a los grandes guerreros que dieron su vida por\n"
                  "ese fuerte. Varok ascendió a Trundle como General, y empezaría a entrenar a la horda de\n"
                  "trolls, para estar listos para la guerra. Varok por el momento se dedicaría a\n"
                  "descansar, el asedio lo había dejado malherido y cansado, pues no había dormido en días.\n"
                  "Necesitaba recuperar fuerzas para la defensa del fuerte que se estaba por disputar en\n"
                  "los tiempos venideros, pero por supuesto, eso forma parte de otra historia, que será\n"
                  "contada en otra ocasión…\n"
                  "FIN")

COMBAT_1 = True
COMBAT_2 = True
COMBAT_3 = True

QUIT = "¡Nos veremos en una proxima aventura viajero!"
ERROR_1 = "Eso no es una opcion valida..."
ERROR_2 = "Vuelva a ejecutar para intentar de nuevo..."
TAKE_DECISION = "Toma una decisión: "