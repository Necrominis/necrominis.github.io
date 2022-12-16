from printer import *




# Make sure to always use trailing commas!
# Make sure to use ’ instead of ' in text!





# ============================================================================ #
manufacturers = {
	"unknown": {
		"text": "Unknown",
		"color": "grey",
		"url": "",
	},
	"games-workshop": {
		"text": "Games Workshop",
		"color": "yellow",
		"url": "https://www.games-workshop.com/en-US/Home",
	},
	"fantasy-flight-games": {
		"text": "Fantasy Flight Games",
		"color": "blue",
		"url": "https://www.fantasyflightgames.com/en/index/",
	},
	"wizkids": {
		"text": "WizKids",
		"color": "yellow",
		"url": "https://wizkids.com/",
	},
	"reaper": {
		"text": "Reaper",
		"color": "red",
		"url": "https://www.reapermini.com/",
	},
	"hero-forge": {
		"text": "Hero Forge",
		"color": "red",
		"url": "https://www.heroforge.com/",
	},
	"war-base-west": {
		"text": "War Base West",
		"color": "yellow",
		"url": "https://www.amazon.com/s?i=merchant-items&me=A2WZTBIXI003FY",
	},
	"3d-printed": {
		"text": "3D Printed Myself",
		"color": "grey",
		"url": "",
	},
	"misc-3d-file": {
		"text": "Misc. 3D files",
		"color": "blue",
		"url": "",
	},
	"one-page-rules": {
		"text": "OnePageRules (3D Files)",
		"color": "white",
		"url": "https://www.myminifactory.com/users/OnePageRules",
	},
	"epic-miniatures": {
		"text": "Epic Miniatures (3D Files)",
		"color": "orange",
		"url": "https://www.myminifactory.com/users/Epic-Miniatures",
	},
	"tytan-troll-miniatures": {
		"text": "Tytan Troll Miniatures (3D Files)",
		"color": "blue",
		"url": "https://www.myminifactory.com/users/TytanTrollMiniatures",
	},
	"rocket-pig-games": {
		"text": "Rocket Pig Games (3D Files)",
		"color": "pink",
		"url": "https://www.myminifactory.com/users/RocketPigGames",
	},
}





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')