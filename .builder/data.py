# Make sure to always use trailing commas!
# Dates are YYYY-MM-DD!
# Paint orders are:
# - Vallejo colors (white to black, red to purple).
# - Vallejo metallics.
# - Vallejo washes & inks.
# - Citadel colors.
# - Citadel metallics.
# - Citadel contrasts.
# - Citadel shades.
# - Citadel technicals and textures.
# - Primers, varnishes, and paint additives.




# First paragraph f"""{FP_}text{_FP}""".
FP_ = """<mark class="first-paragraph">"""
_FP = """</mark>"""

# Mini name f"""{MN_}text{_MN}"""..
MN_ = """<mark class="mini-name">"""
_MN = """</mark>"""

# Tooltip f"""{TT_}text{_TT_}description{_TT}""".
TT_ = """<mark class="tooltip">"""
_TT_ = """<span class="tip">"""
_TT = """</span></mark>"""

# Link f"""{A_}url{_A_}text{_A}""".
A_ = """<a href=\""""
_A_ = """\">"""
_A = """</a>"""

# Italic f"""{I_}text{_i}""".
I_ = """<i>"""
_I = """</i>"""

# Italic link f"""{IA_}url{_IA_}text{_IA}""".
IA_ = f"""{I_}{A_}"""
_IA_ = f"""{_A_}"""
_IA = f"""{_I}{_A}"""

# Bold f"""{B_}text{_B}""".
B_ = """<b>"""
_B = """</b>"""





data = {
	"website": "https://necrominis.github.io/",
	#"website": "/home/tucker/dev/necrominis.github.io/",

	# ============================================================================ #
	#                                IMAGE FOLDERS                                 #
	# ============================================================================ #

	"image-paths": {
		"logos": "images/logos/",
		"covers": "images/covers/",
		"icons": "images/icons/",
		"paint-photos": "images/paint/",
		"paint-icons": "images/paint-icons/",
		"supplies-photos": "images/supplies",
		"supplies-icons": "images/supplies-icons/",
		"post-photos": "images/posts/",
	},

	# ============================================================================ #
	#                                     TAGS                                     #
	# ============================================================================ #

	"tags": {
		"dungeons-and-dragons": {
			"text": "Dungeons & Dragons",
			"color": "red",
			"linked-page": "gallery",
		},
		"warhammer-40k": {
			"text": "Warhammer: 40,000",
			"color": "blue",
			"linked-page": "gallery",
		},
		"warhammer-age-of-sigmar": {
			"text": "Warhammer: Age of Sigmar",
			"color": "yellow",
			"linked-page": "gallery",
		},
		"warhammer-underworlds": {
			"text": "Warhammer: Underworlds",
			"color": "red",
			"linked-page": "gallery",
		},
		"star-wars-legion": {
			"text": "Star Wars: Legion",
			"color": "blue",
			"linked-page": "gallery",
		},
		"star-wars": {
			"text": "Star Wars",
			"color": "yellow",
			"linked-page": "gallery",
		},
		"superhero": {
			"text": "Superhero",
			"color": "red",
			"linked-page": "gallery",
		},
		"fantasy": {
			"text": "Fantasy",
			"color": "green",
			"linked-page": "gallery",
		},
		"sci-fi": {
			"text": "Sci-Fi",
			"color": "purple",
			"linked-page": "gallery",
		},
		"display": {
			"text": "Display",
			"color": "pink",
			"linked-page": "gallery",
		},
		"bust": {
			"text": "Bust",
			"color": "orange",
			"linked-page": "gallery",
		},
		"tabletop": {
			"text": "Tabletop",
			"color": "brown",
			"linked-page": "gallery",
		},
		"kitbash": {
			"text": "Kitbash",
			"color": "white",
			"linked-page": "gallery",
		},
		"technique-testing": {
			"text": "Technique Testing",
			"color": "green",
			"linked-page": "gallery",
		},
		"wip": {
			"text": "Work in Progress",
			"color": "white",
			"linked-page": "gallery",
		},
	},

	# ============================================================================ #
	#                                MANUFACTURERS                                 #
	# ============================================================================ #

	"manufacturers": {
		"unknown": {
			"text": "Unknown",
			"color": "grey",
			"url": "#",
		},
		"games-workshop": {
			"text": "Games Workshop",
			"color": "yellow",
			"url": "#",
		},
		"fantasy-flight-games": {
			"text": "Fantasy Flight Games",
			"color": "blue",
			"url": "#",
		},
		"wizkids": {
			"text": "WizKids",
			"color": "yellow",
			"url": "#",
		},
		"reaper": {
			"text": "Reaper",
			"color": "red",
			"url": "#",
		},
		"3d-printed": {
			"text": "3D Printed",
			"color": "grey",
			"url": "#",
		},
		"hero-forge": {
			"text": "Hero Forge",
			"color": "red",
			"url": "#",
		},
		"hallmark": {
			"text": "Hallmark",
			"color": "purple",
			"url": "#",
		},
		"war-base-west": {
			"text": "War Base West",
			"color": "grey",
			"url": "#",
		},
	},

	# ============================================================================ #
	#                                   SUPPLIES                                   #
	# ============================================================================ #

	"supplies": {
		"separator": " / ",
		"categories": {
			"brushes": {
				"brands": {
					"badger": {
						"text": "Badger",
						"items": {
							"105-patriot-air-brush": {
								"text": "105 Patriot Air-Brush",
								"icon": "air-brush.png",
								"page": "105-patriot-air-brush",
								"official-name": "Badger Air-Brush Co. Model 105 Patriot",
								"url": "https://www.amazon.com/Badger-Air-Brush-Co-Patriot-Airbrush/dp/B002W84GTO/ref=sr_1_1?crid=13TABVFPVOAAP&keywords=badger%2B105%2Bairbrush&qid=1647451154&sprefix=badger%2B105airbrush%2Caps%2C99&sr=8-1&th=1",
							},
						},
					},
				},
			},
		},
	},

	# ============================================================================ #
	#                                    PAINTS                                    #
	# ============================================================================ #

	"paint-brands": {
		"vallejo": {
			"text": "Vallejo",
			"lines": {
				"model-color": {
					"text": "Model Color",
				},
				"game-color": {
					"text": "Game Color",
				},
				"metal-color": {
					"text": "Metal Color",
				},
			},
		},
	},

	# ============================================================================ #

	"paints": {
		# Vallejo colors ============================================================= #
		"vallejo-model-color-white": {
			"text": "White",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.951 White",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/white-70951/",
		},
		"vallejo-game-color-dead-white": {
			"text": "Dead White",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.001 Dead White",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/dead-white-72001/",
		},
		"vallejo-model-color-off-white": {
			"text": "Off-White",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.820 Off-White",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/off-white-70820/",
		},
		"vallejo-game-color-wolf-grey": {
			"text": "Wolf Grey",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.047 Wolf Grey",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/wolf-grey-72047/",
		},
		"vallejo-model-color-medium-sea-grey": {
			"text": "Medium Sea Grey",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.870 Medium Sea Grey",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/medium-sea-grey-70870/",
		},
		"vallejo-model-color-neutral-grey": {
			"text": "Neutral Grey",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.992 Neutral Grey",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/neutral-grey-70992/",
		},
		"vallejo-game-color-sombre-grey": {
			"text": "Sombre Grey",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.048 Sombre Grey",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/sombre-grey-72048/",
		},
		"vallejo-model-color-intermediate-blue": {
			"text": "Intermediate Blue",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.903 Intermediate Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/intermediate-blue-70903/",
		},
		"vallejo-model-color-black": {
			"text": "Black",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.950 Black",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/black-70950/",
		},
		"vallejo-model-color-flat-red": {
			"text": "Flat Red",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.957 Flat Red",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-red-70957/",
		},
		"vallejo-game-color-gory-red": {
			"text": "Gory Red",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.011 Gory Red",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gory-red-72011/",
		},
		"vallejo-model-color-hull-red": {
			"text": "Hull Red",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.985 Hull Red",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/hull-red-70985/",
		},
		"vallejo-game-color-terracotta": {
			"text": "Terracotta",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.065 Terracotta",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/terracotta-72065/",
		},
		"vallejo-game-color-hot-orange": {
			"text": "Hot Orange",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.009 Hot Orange",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/hot-orange-72009/",
		},
		"vallejo-model-color-clear-orange": {
			"text": "Clear Orange",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.956 Clear Orange",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/clear-orange-70956/",
		},
		"vallejo-game-color-pale-flesh": {
			"text": "Pale Flesh",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.003 Pale Flesh",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/pale-flesh-72003/",
		},
		"vallejo-model-color-flat-flesh": {
			"text": "Flat Flesh",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.995 Flat Flesh",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-flesh-70955/",
		},
		"vallejo-game-color-charred-brown": {
			"text": "Charred Brown",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.045 Charred Brown",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/charred-brown-72045/",
		},
		"vallejo-model-color-flat-brown": {
			"text": "Flat Brown",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.984 Flat Brown",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-brown-70984/",
		},
		"vallejo-game-color-beasty-brown": {
			"text": "Beasty Brown",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.043 Beasty Brown",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/beasty-brown-72043/",
		},
		"vallejo-game-color-orange-fire": {
			"text": "Orange Fire",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.008 Orange Fire",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/orange-fire-72008/",
		},
		"vallejo-game-color-scrofulous-brown": {
			"text": "Scrofulous Brown",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.038 Scrofulous Brown",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/scrofulous-brown-72038/",
		},
		"vallejo-model-color-buff": {
			"text": "Buff",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.976 Buff",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/buff-70976/",
		},
		"vallejo-model-color-yellow-ochre": {
			"text": "Yellow Ochre",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.913 Yellow Ochre",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/yellow-ochre-70913/",
		},
		"vallejo-game-color-gold-yellow": {
			"text": "Gold Yellow",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.007 Gold Yellow",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gold-yellow-72007/",
		},
		"vallejo-model-color-lemon-yellow": {
			"text": "Lemon Yellow",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.952 Lemon Yellow",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/lemon-yellow-70952/",
		},
		"vallejo-model-color-lime-green": {
			"text": "Lime Green",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.827 Lime Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/lime-green-70827/",
		},
		"vallejo-model-color-refractive-green": {
			"text": "Refractive Green",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.890 Refractive Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/refractive-green-70890/",
		},
		"vallejo-model-color-flat-green": {
			"text": "Flat Green",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.968 Flat Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-green-70968/",
		},
		"vallejo-model-color-intermediate-green": {
			"text": "Intermediate Green",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.891 Intermediate Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/intermediate-green-70891/",
		},
		"vallejo-game-color-goblin-green": {
			"text": "Goblin Green",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.030 Goblin Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/goblin-green-72030/",
		},
		"vallejo-model-color-emerald": {
			"text": "Emerald",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.838 Emerald",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/emerald-70838/",
		},
		"vallejo-model-color-park-green-flat": {
			"text": "Park Green Flat",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.969 Park Green Flat",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/park-green-flat-70969/",
		},
		"vallejo-game-color-scurvy-green": {
			"text": "Scurvy Green",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.027 Scurvy Green",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/scurvy-green-72027/",
		},
		"vallejo-game-color-electric-blue": {
			"text": "Electric BLue",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.023 Electric Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/electric-blue-72023/",
		},
		"vallejo-model-color-deep-sky-blue": {
			"text": "Deep Sky Blue",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.844 Deep Sky Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/deep-sky-blue-70844/",
		},
		"vallejo-model-color-azure": {
			"text": "Azure",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.902 Azure",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/azure-70902/",
		},
		"vallejo-model-color-grey-blue": {
			"text": "Grey Blue",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.943 Grey Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/grey-blue-70943/",
		},
		"vallejo-model-color-flat-blue": {
			"text": "Flat Blue",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.962 Flat Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-blue-70962/",
		},
		"vallejo-game-color-ultramarine-blue": {
			"text": "Ultramarine Blue",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.022 Ultramarine Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/ultramarine-blue-72022/",
		},
		"vallejo-game-color-imperial-blue": {
			"text": "Imperial Blue",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.020 Imperial Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/imperial-blue-72020/",
		},
		"vallejo-game-color-night-blue": {
			"text": "Night Blue",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.019 Night Blue",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/night-blue-72019/",
		},
		"vallejo-game-color-heavy-violet": {
			"text": "Heavy Violet",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.142 Heavy Violet",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/heavy-violet-72142/",
		},
		"vallejo-game-color-hexed-lichen": {
			"text": "Hexed Lichen",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.015 Hexed Lichen",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/hexed-lichen-72015/",
		},
		"vallejo-model-color-purple": {
			"text": "Purple",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 72.959 Purple",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/purple-70959/",
		},
		"vallejo-model-color-royal-purple": {
			"text": "Royal Purple",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.810 Royal Purple",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/royal-purple-70810/",
		},
		"vallejo-game-color-warlord-purple": {
			"text": "Warlord Purple",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.014 Warlord Purple",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/warlord-purple-72014/",
		},
		# Vallejo metallics ========================================================== #
		"vallejo-metal-color-aluminium": {
			"text": "Aluminium",
			"brand": "vallejo",
			"line": "metal",
			"official-name": "Vallejo Metal Color 77.701 Aluminium",
			"url": "https://acrylicosvallejo.com/en/product/hobby/metal-color-en/aluminium-77701/",
		},
		"vallejo-model-color-silver": {
			"text": "Silver",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.997 Silver",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/silver-70997/",
		},
		"vallejo-game-color-silver": {
			"text": "Silver",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.052 Silver",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/silver-72052/",
		},
		"vallejo-game-color-gunmetal": {
			"text": "Gunmetal",
			"brand": "vallejo",
			"line": "game-color",
			"official-name": "Vallejo Game Color 72.054 Gunmetal",
			"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gunmetal-72054/",
		},
		"vallejo-model-color-gold": {
			"text": "Gold",
			"brand": "vallejo",
			"line": "model-color",
			"official-name": "Vallejo Model Color 70.996 Gold",
			"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/gold-70996/",
		},
	},

	# ============================================================================ #
	#                                    PAGES                                     #
	# ============================================================================ #

	"pages": {
		"home": {
			"title": "Necrominis Mini-Painting Studio",
			"type": "home",
			"paragraphs": [
				f"""{FP_}I'm {MN_}Tucker{_MN} from {MN_}Necrominis{_MN}, and I'm a miniature painter hobbyist.{_FP}""",
				f"""I first tried painting miniatures in 2015, for the {IA_}https://dnd.wizards.com/what-is-dnd{_IA_}Dungeons & Dragons{_IA} tabletop roleplaying game. In 2019, I took on miniature painting as a serious hobby and have been improving my craft every since.""",
				f"""I still paint miniatures for tabletop games like {IA_}https://dnd.wizards.com/what-is-dnd{_IA_}D&D{_IA}, {IA_}https://www.warhammer-community.com/en-us{_IA_}Warhammer{_IA}, and {IA_}https://www.fantasyflightgames.com/en/products/star-wars-legion{_IA_}Star Wars: Legion{_IA}, but now I also paint for the sole purpose of painting beautiful display miniatures, as well.""",
				f"""I've also purchased an {IA_}https://www.anycubic.com/products/anycubic-photon-s{_IA_}AnyCubic Photon S{_IA}, in 2020, and have been {TT_}3D printing{_TT_}3D printing is the construction of physical objects from a digital 3D model file.{_TT} resin miniatures ever since. Most of the models I print are purchased from {IA_}https://www.myminifactory.com{_IA_}My Mini Factory{_IA} or from artists I support on {IA_}https://www.patreon.com{_IA_}Patreon{_IA}.""",
			]
		},
		# ============================================================================ #
		"my-paints": {
			"title": "My Paint Collection",
			"type": "my-paints",
			"lists": {
				"vallejo": {
					"text": "Vallejo Paints",
					"paints": [
						"vallejo-model-color-black",
					],
				},
			},
		},
		# ============================================================================ #
		"my-supplies": {
			"title": "My Hobby Supplies",
			"type": "my-supplies",
			"lists": {

			},
		},
		# ============================================================================ #
		"gallery": {
			"title": "Gallery",
			"type": "gallery",
			"pages": [
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
				"2022-06-10",
			],
		},
		# ============================================================================ #
		"2022-06-10": {
			"title": "Vampire Necromancer",
			"type": "post",
			"properties": {
				"created": "June 10, 2022",
				"tags": [
					"warhammer-underworlds", "fantasy", "tabletop",
				],
				"manufacturers": [
					"games-workshop",
				],
				"models": [
					{
						"text": "Soulblight Gravelord",
						"url": "https://www.games-workshop.com/en-US/solblight-gravelords-the-crimson-court-2022"
					},
				],
			},
			"images": [
				"necrominis-2022-06-10-raw-1.jpeg",
				"necrominis-2022-06-10-raw-2.jpeg",
				"necrominis-2022-06-10-raw-3.jpeg",
				"necrominis-2022-06-10-raw-4.jpeg",
			],
			"paragraphs": [
				f"""{FP_}A {MN_}Soulblight Gravelord Vampire{_MN} painted with a necromancy magic scheme.{_FP}""",
				f"""The first thing I worked on for this miniature was actually the base. I primed it black and gave it a rough airbrushing of a dark purple. I then wanted to create a glowing effect coming out of the cracks between the stone, so I dry-brushed dark teal around the cracks, then a lighter teal closer to the cracks, and then filled in the cracks with a lime green.""",
				f"""For the actual vampire model, I started with the skin first. I layered from a medium grey to a light grey, but with some purple mixed in, with more purple in the darker tones, and more grey in the lighter tones. I used a similar technique for the wing arms, except using dark teal instead of purple. As for the actual wings, I left them black, dry-brushed dark teal toward the ends, and added a spotty texture to them.""",
				f"""Seeing the rest of the model still black made me realize a dark outfit would fit the best and contrast with the light skin. The armor pieces remained black, but were highlighted toward dark purple and edge highlighted with a similar purple-grey mix from the skin's base coat. The rest of the straps, the mace, and the hair were highlighted similarly with dark to medium greys, as I wanted to avoid using metallic paints for this mini.""",
				f"""The last details were a few gems and a bottle on the vampire's waist. These were painted with the two teal colors and the lime green, to remain coherent with the base.""",
				f"""Finally, I airbrushed the two teal colors onto the model from below, to give the effect that the green light from the base is lighting up the vampire from below. Then I gave it a clear coat of gloss, for protective purposes, and matte for the final finish.""",
				f"""All-in-all, I think this might be my best miniature yet, in terms of the color coherency, the skin shading, and the glow effect. One of my {A_}https://necrominis.github.io/post/2022-03-15/{_A_}previous miniatures{_A} had a better paint job for the skin, but that was with an airbrush; this miniature's skin was painted by hand, and this one has higher contrast. I do think the wings' spots could be redone, though. I wanted to highlight the horizontal folds in the wings, but they weren't defined enough to catch the edge of my brush, and were too small to highlight by hand. Overall, though, I think this miniature turned out beautifully.""",
			],
			"paints-used": [
				"vallejo-game-color-wolf-grey",
				"vallejo-model-color-medium-sea-grey",
				"vallejo-game-color-sombre-grey",
				"vallejo-model-color-black",
				"vallejo-model-color-lime-green",
				"vallejo-model-color-park-green-flat",
				"vallejo-game-color-scurvy-green",
				"vallejo-game-color-heavy-violet",
				"",
				# "vallejo-surface-primer-black",
				# "krylon-spray-matte-finish",
				# "vallejo-auxiliary-gloss-acrylic-varnish",
				# "liquitex-acrylic-medium-flow-aid",
			],
		},
	},
}