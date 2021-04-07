from art import *
from termcolor import colored
import subprocess
subprocess.call('', shell=True)
import os
import sys
from selenium import webdriver
import time


def clss():
	os.system('cls' if os.name=='nt' else 'clear')



def main():
	clss()
	print(colored(text2art("Rom  seacher"),'cyan'))
	print(colored('Nintendo version - Created by Cucus\n\n\n'.center(107),'red'))
	x = input("Que voulez vous ?\n1. Un émulateur\n2. Une rom\n3. Infos\n4. Quitter\n\nVeuillez entrer un nombre : ")
	if x =='1':
		emul()

	if x =='2':
		rom()

	if x == '3':
		info()

	if x =='4':
		clss()
		sys.exit(0)
	else:
		print("Veuillez entrer un nombre")
		sys.exit(0)



def info():
	clss()
	print("Ce script a été créé pour vous aider a trouver des roms et des émulateurs plus facilement.\n")
	print("Dans l'option 'Rom': choisisez une plateforme, un nom de jeu, \net vous serez automatiquement redirigé vers le site de romsforever.co")
	print("Dans l'option 'Emulateur': choisisez une plateforme et vous serez directement redirigé vers le site mega.nz\n")
	print("/!\\N'inclut que les jeux Nintendo/!\\")
	input("")
	main()



def emul():
	clss()
	m = input("Quel type d'émulateur cherchez vous ?\n1. Game Boy\n2. Game Boy Color\n3. Gamecube\n4. GBA\n5. NES\n6. SNES\n7. Nintendo 64\n8. DS\n9. 3DS\n10. Wii\n11. Wii U\n12. Switch\n13. Quitter\n\n\nVeuillez entrer un nombre : ")
	prossesEmul(m)




def rom():
	clss()
	n = input("Quel type de rom cherchez vous ?\n1. Game Boy\n2. Game Boy Color\n3. Gamecube\n4. GBA\n5. NES\n6. SNES\n7. Nintendo 64\n8. DS\n9. 3DS\n10. Wii\n11. Wii U\n12. Switch\n13. Quitter\n\n\nVeuillez entrer un nombre : ")
	if n == '13':
		clss()
		sys.exit(0)



	clss()
	name = input("Quel jeu voulez vous rechercher ?\n\n--> ")
	prossesRom(n, name)




def prossesRom(nbre, name): #On redirige le navigateur vers les différentes catégories
	if nbre == '1':
		site = "https://romsforever.co/roms/game-boy"
	if nbre == '2':
		site = "https://romsforever.co/roms/game-boy-color"
	if nbre == '3':
		site = "https://romsforever.co/roms/gamecube"
	if nbre == '4':
		site = "https://romsforever.co/roms/game-boy-advance"
	if nbre == '5':
		site = "https://romsforever.co/roms/nes"
	if nbre == '6':
		site = "https://romsforever.co/roms/super-nintendo"
	if nbre == '7':
		site = "https://romsforever.co/roms/nintendo-64"
	if nbre == '8':
		site = "https://romsforever.co/roms/nintendo-ds"
	if nbre == '9':
		site = "https://romsforever.co/roms/3ds"
	if nbre == '10':
		site = "https://romsforever.co/roms/nintendo-wii"
	if nbre == '11':
		site = "https://romsforever.co/roms/wii-u"
	if nbre == '12':
		site = "https://romsforever.co/roms/switch"
	if nbre == '13':
		sys.exit(0)
	"""else:
		print("Veuillez entrer un nombre valide")
		sys.exit(0)"""


	driver = webdriver.Chrome(executable_path="chromedriver.exe")
	driver.get(site)
	#On écrit dans la barre de recherche le texte que l'utilisateur a entré
	search_bar = driver.find_element_by_name("s")
	search_bar.send_keys(name)
	#On click sur le bouton pour rechercher
	button = driver.find_element_by_class_name("is-search-filter")
	button.click()
	print("\n\nVeuillez fermer l'invite de commande")
	while True:
		time.sleep(1)




def prossesEmul(nbre): #On redirige le navigateur vers les différentes émulateurs
	if nbre == '1':
		site = "https://mega.nz/file/fchBWIZS#XdBqS6W5yyXwqWqWNSduxP2-j_6GWoaf5thcZ--EhMc"
	if nbre == '2':
		site = "https://mega.nz/file/fchBWIZS#XdBqS6W5yyXwqWqWNSduxP2-j_6GWoaf5thcZ--EhMc"
	if nbre == '3':
		site = "https://mega.nz/file/zIg1TAJD#bMoQRth6gdb1_FvVrrnh8OS0gehAQLF8rruYjD1QMN8"
	if nbre == '4':
		site = "https://mega.nz/file/fchBWIZS#XdBqS6W5yyXwqWqWNSduxP2-j_6GWoaf5thcZ--EhMc"
	if nbre == '5':
		site = "https://mega.nz/file/qcwjAKQY#Ycyk8bEixMewF2SwpkgNj01B_M7x9MOpG5P5cqyl1ts"
	if nbre == '6':
		site = "https://mega.nz/file/SN4VFYxC#H-pcsIIR7JeoOMe_B2EoUj6tjdgdG5a_PxiAbLnwTIE"
	if nbre == '7':
		site = "https://mega.nz/file/rQh1xYwD#yuYgWsPyCxLUb2nlbuED10oxpQPoQGxheTyA0WAjjdU"
	if nbre == '8':
		site = "https://mega.nz/file/PZowFRYA#CvaT7T44sCZWvBh97uOxMcq5dtrfCG1tjxrqg-tUk2s"
	if nbre == '9':
		site = "https://mega.nz/file/vVww3JiR#G0_2FN6i3wcYKb4PB3zf5DENhWzGuXDMPl2Fmc9qocI"
	if nbre == '10':
		site = "https://mega.nz/file/zIg1TAJD#bMoQRth6gdb1_FvVrrnh8OS0gehAQLF8rruYjD1QMN8"
	if nbre == '11':
		site = "https://mega.nz/file/3Rg0VLIK#VtXq7aNCceQuvRxpEYUMZ9gY0Mh6cBnacRjcZCLlaHQ"
	if nbre == '12':
		site = "https://mega.nz/file/XR4A2D5T#oHK8U3WZLI_oLZQ32njE2_duR7I_GzdmqjFAvQmr_PQ"
	if nbre == '13':
		clss()
		sys.exit(0)
	"""else:
		print("Veuillez entrer un nombre valide")
		sys.exit(0)"""

	driver = webdriver.Chrome(executable_path="chromedriver.exe")
	driver.get(site)
	print("\n\nVeuillez fermer l'invite de commande")
	while True:
		time.sleep(1)




if __name__ == '__main__':
	main()