from printer import *





# Make sure to always use trailing commas!
# Paint orders are the same as category orders!
# Paint colors arw white to black and red to purple!





# ============================================================================ #
def _solid(color: str) -> str:
	return f"background-color: {color};"
def _right(comma_separated_colors: str) -> str:
	return f"background-image: linear-gradient(to right, {comma_separated_colors});"
def _down(comma_separated_colors: str) -> str:
	return f"background-image: linear-gradient(to bottom, {comma_separated_colors});"
def _diagonal(comma_separated_colors: str) -> str:
	return f"background-image: linear-gradient(to bottom right, {comma_separated_colors});"
def _radial(comma_separated_colors: str) -> str:
	return f"background-image: radial-gradient({comma_separated_colors});"





# ============================================================================ #
paint_categories = {
	"colors": {
		"text": "Color Paints",
	},
	"metallics": {
		"text": "Metallic Paints",
	},
	"washes": {
		"text": "Washes & Shades",
	},
	"contrasts": {
		"text": "Contrast Paints",
	},
	"inks": {
		"text": "Inks",
	},
	"technicals": {
		"text": "Texture & Technical Paints",
	},
	"varnishes": {
		"text": "Varnishes",
	},
	"additives": {
		"text": "Additives",
	},
	"primers": {
		"text": "Primers",
	},
}





# ============================================================================ #
paint_brands = {
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
			"diorama-effects": {
				"text": "Diorama Effects",
			},
			"auxiliaries": {
				"text": "Auxiliaries",
			},
			"surface-primer": {
				"text": "Surface Primer",
			},
		},
	},
	"citadel": {
		"text": "Citadel",
		"lines": {
			"base": {
				"text": "Base",
			},
			"layer": {
				"text": "Layer",
			},
			"dry": {
				"text": "Dry",
			},
			"shade": {
				"text": "Shade",
			},
			"contrast": {
				"text": "Contrast",
			},
			"technical": {
				"text": "Technical",
			},
			"texture": {
				"text": "Texture",
			},
			"sprays": {
				"text": "Sprays",
			},
			"air": {
				"text": "Air",
			},
		},
	},
	"army-painter": {
		"text": "Army Painter",
		"lines": {
			"warpaints": {
				"text": "Warpaints",
			},
		},
	},
	"liquitex": {
		"text": "Liquitex",
		"lines": {
			"acrylic-mediums": {
				"text": "Acrylic Mediums"
			},
		},
	},
	"tamiya": {
		"text": "Tamiya",
		"lines": {
			"surface-primer-l": {
				"text": "Surface Primer L"
			},
		},
	},
	"krylon": {
		"text": "Krylon",
		"lines": {
			"color-maxx": {
				"text": "Color Maxx"
			},
		},
	},
}





# ============================================================================ #
_colors = {
	"vallejo-model-color-white": {
		"text": "White",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.951 White",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/white-70951/",
	},
	"vallejo-game-color-dead-white": {
		"text": "Dead White",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.001 Dead White",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/dead-white-72001/",
	},
	"vallejo-model-color-off-white": {
		"text": "Off-White",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.820 Off-White",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/off-white-70820/",
	},
	"vallejo-game-color-wolf-grey": {
		"text": "Wolf Grey",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"icon-css": _solid("#afc1cb"),
		"official-name": "Vallejo Game Color 72.047 Wolf Grey",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/wolf-grey-72047/",
	},
	"vallejo-model-color-medium-sea-grey": {
		"text": "Medium Sea Grey",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.870 Medium Sea Grey",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/medium-sea-grey-70870/",
	},
	"vallejo-model-color-neutral-grey": {
		"text": "Neutral Grey",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.992 Neutral Grey",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/neutral-grey-70992/",
	},
	"vallejo-game-color-sombre-grey": {
		"text": "Sombre Grey",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.048 Sombre Grey",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/sombre-grey-72048/",
	},
	"vallejo-model-color-intermediate-blue": {
		"text": "Intermediate Blue",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.903 Intermediate Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/intermediate-blue-70903/",
	},
	"vallejo-model-color-black": {
		"text": "Black",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.950 Black",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/black-70950/",
	},
	"vallejo-model-color-flat-red": {
		"text": "Flat Red",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.957 Flat Red",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-red-70957/",
	},
	"vallejo-game-color-gory-red": {
		"text": "Gory Red",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.011 Gory Red",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gory-red-72011/",
	},
	"vallejo-model-color-hull-red": {
		"text": "Hull Red",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.985 Hull Red",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/hull-red-70985/",
	},
	"vallejo-game-color-terracotta": {
		"text": "Terracotta",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.065 Terracotta",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/terracotta-72065/",
	},
	"vallejo-game-color-hot-orange": {
		"text": "Hot Orange",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.009 Hot Orange",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/hot-orange-72009/",
	},
	"vallejo-model-color-clear-orange": {
		"text": "Clear Orange",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.956 Clear Orange",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/clear-orange-70956/",
	},
	"vallejo-game-color-pale-flesh": {
		"text": "Pale Flesh",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.003 Pale Flesh",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/pale-flesh-72003/",
	},
	"vallejo-model-color-flat-flesh": {
		"text": "Flat Flesh",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.995 Flat Flesh",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-flesh-70955/",
	},
	"vallejo-game-color-charred-brown": {
		"text": "Charred Brown",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.045 Charred Brown",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/charred-brown-72045/",
	},
	"vallejo-model-color-flat-brown": {
		"text": "Flat Brown",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.984 Flat Brown",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-brown-70984/",
	},
	"vallejo-game-color-beasty-brown": {
		"text": "Beasty Brown",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.043 Beasty Brown",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/beasty-brown-72043/",
	},
	"vallejo-game-color-orange-fire": {
		"text": "Orange Fire",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.008 Orange Fire",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/orange-fire-72008/",
	},
	"vallejo-game-color-scrofulous-brown": {
		"text": "Scrofulous Brown",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.038 Scrofulous Brown",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/scrofulous-brown-72038/",
	},
	"vallejo-model-color-buff": {
		"text": "Buff",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.976 Buff",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/buff-70976/",
	},
	"vallejo-model-color-yellow-ochre": {
		"text": "Yellow Ochre",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.913 Yellow Ochre",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/yellow-ochre-70913/",
	},
	"vallejo-game-color-gold-yellow": {
		"text": "Gold Yellow",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.007 Gold Yellow",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gold-yellow-72007/",
	},
	"vallejo-model-color-lemon-yellow": {
		"text": "Lemon Yellow",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.952 Lemon Yellow",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/lemon-yellow-70952/",
	},
	"vallejo-model-color-lime-green": {
		"text": "Lime Green",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.827 Lime Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/lime-green-70827/",
	},
	"vallejo-model-color-refractive-green": {
		"text": "Refractive Green",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.890 Refractive Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/refractive-green-70890/",
	},
	"vallejo-model-color-flat-green": {
		"text": "Flat Green",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.968 Flat Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-green-70968/",
	},
	"vallejo-model-color-intermediate-green": {
		"text": "Intermediate Green",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.891 Intermediate Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/intermediate-green-70891/",
	},
	"vallejo-game-color-goblin-green": {
		"text": "Goblin Green",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.030 Goblin Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/goblin-green-72030/",
	},
	"vallejo-model-color-emerald": {
		"text": "Emerald",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.838 Emerald",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/emerald-70838/",
	},
	"vallejo-model-color-park-green-flat": {
		"text": "Park Green Flat",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.969 Park Green Flat",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/park-green-flat-70969/",
	},
	"vallejo-game-color-scurvy-green": {
		"text": "Scurvy Green",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.027 Scurvy Green",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/scurvy-green-72027/",
	},
	"vallejo-game-color-electric-blue": {
		"text": "Electric BLue",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.023 Electric Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/electric-blue-72023/",
	},
	"vallejo-model-color-deep-sky-blue": {
		"text": "Deep Sky Blue",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.844 Deep Sky Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/deep-sky-blue-70844/",
	},
	"vallejo-model-color-azure": {
		"text": "Azure",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.902 Azure",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/azure-70902/",
	},
	"vallejo-model-color-grey-blue": {
		"text": "Grey Blue",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.943 Grey Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/grey-blue-70943/",
	},
	"vallejo-model-color-flat-blue": {
		"text": "Flat Blue",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.962 Flat Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/flat-blue-70962/",
	},
	"vallejo-game-color-ultramarine-blue": {
		"text": "Ultramarine Blue",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.022 Ultramarine Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/ultramarine-blue-72022/",
	},
	"vallejo-game-color-imperial-blue": {
		"text": "Imperial Blue",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.020 Imperial Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/imperial-blue-72020/",
	},
	"vallejo-game-color-night-blue": {
		"text": "Night Blue",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.019 Night Blue",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/night-blue-72019/",
	},
	"vallejo-game-color-heavy-violet": {
		"text": "Heavy Violet",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.142 Heavy Violet",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/heavy-violet-72142/",
	},
	"vallejo-game-color-hexed-lichen": {
		"text": "Hexed Lichen",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.015 Hexed Lichen",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/hexed-lichen-72015/",
	},
	"vallejo-model-color-purple": {
		"text": "Purple",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 72.959 Purple",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/purple-70959/",
	},
	"vallejo-model-color-royal-purple": {
		"text": "Royal Purple",
		"brand": "vallejo",
		"line": "model-color",
		"category": "colors",
		"official-name": "Vallejo Model Color 70.810 Royal Purple",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/royal-purple-70810/",
	},
	"vallejo-game-color-warlord-purple": {
		"text": "Warlord Purple",
		"brand": "vallejo",
		"line": "game-color",
		"category": "colors",
		"official-name": "Vallejo Game Color 72.014 Warlord Purple",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/warlord-purple-72014/",
	},
	# TODO: Combine these Citadel paints into the above paint list.
	"citadel-layer-scar-white": {
		"text": "Scar White",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Scar White",
		"url": "https://www.games-workshop.com/en-US/Layer-White-Scar-2019",
	},
	"citadel-base-corax-white": {
		"text": "Corax White",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Corax White",
		"url": "https://www.games-workshop.com/en-US/Base-Corax-White-2019",
	},
	"citadel-layer-eshin-grey": {
		"text": "Eshin Grey",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Eshin Grey",
		"url": "https://www.games-workshop.com/en-US/Layer-Eshin-Grey-2019",
	},
	"citadel-base-abaddon-black": {
		"text": "Abaddon Black",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "",
		"url": "https://www.games-workshop.com/en-US/Base-Abaddon-Black-2019",
	},
	"citadel-layer-evil-sunz-scarlet": {
		"text": "Evil Sunz Scarlet",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Evil Sunz Scarlet",
		"url": "https://www.games-workshop.com/en-US/Layer-Evil-Sunz-Scarlet-2019",
	},
	"citadel-base-mephiston-red": {
		"text": "Mephiston Red",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Mephiston Red",
		"url": "https://www.games-workshop.com/en-US/Base-Mephiston-Red-2019",
	},
	"citadel-layer-wazdakka-red": {
		"text": "Wazdakka Red",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Wazdakka Red",
		"url": "https://www.games-workshop.com/en-US/Layer-Wazdakka-Red-2019",
	},
	"citadel-layer-cadian-fleshtone": {
		"text": "Cadian Fleshtone",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Cadian Fleshtone",
		"url": "https://www.games-workshop.com/en-US/Layer-Cadian-Fleshtone-2019",
	},
	"citadel-base-wraithbone": {
		"text": "Wraithbone",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Wraithbone",
		"url": "https://www.games-workshop.com/en-US/Base-Wraithbone-2019",
	},
	"citadel-layer-ushabti-bone": {
		"text": "Ushabti Bone",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Ushabti Bone",
		"url": "https://www.games-workshop.com/en-US/Layer-Ushabti-Bone-2019s",
	},
	"citadel-layer-temple-guard-blue": {
		"text": "Temple Guard Blue",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Temple Guard Blue",
		"url": "https://www.games-workshop.com/en-US/Layer-Temple-Guard-Blue-2019",
	},
	"citadel-layer-sotek-green": {
		"text": "Sotek Green",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Sotek Green",
		"url": "https://www.games-workshop.com/en-US/Layer-Sotek-Green-2019",
	},
	"citadel-layer-thunderhawk-blue": {
		"text": "Thunderhawk Blue",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Thunderhawk Blue",
		"url": "https://www.games-workshop.com/en-US/Layer-Thunderhawk-Blue-2019s",
	},
	"citadel-base-incubi-darkness": {
		"text": "Incubi Darkness",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Incubi Darkness",
		"url": "https://www.games-workshop.com/en-US/Layer-Thunderhawk-Blue-2019",
	},
	"citadel-layer-fenrisian-grey": {
		"text": "Fenrisian Grey",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Fenrisian Grey",
		"url": "https://www.games-workshop.com/en-US/Layer-Fenrisian-Grey-2019s",
	},
	"citadel-dry-stormfang": {
		"text": "Stormfang",
		"brand": "citadel",
		"line": "dry",
		"category": "colors",
		"official-name": "Citadel Dry Stormfang",
		"url": "https://www.games-workshop.com/en-US/Dry-Stormfang-2019",
	},
	"citadel-layer-russ-grey": {
		"text": "Russ Grey",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Russ Grey",
		"url": "https://www.games-workshop.com/en-US/Layer-Russ-Grey-2019",
	},
	"citadel-layer-hoeth-blue": {
		"text": "Hoeth Blue",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Hoeth Blue",
		"url": "https://www.games-workshop.com/en-US/Layer-Hoeth-Blue-2019",
	},
	"citadel-base-the-fang": {
		"text": "The Fang",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base The Fang",
		"url": "https://www.games-workshop.com/en-US/Base-The-Fang-2019s",
	},
	"citadel-base-macragge-blue": {
		"text": "Macragge Blue",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Macragge Blue",
		"url": "https://www.games-workshop.com/en-US/Base-Macragge-Blue-2019s",
	},
	"citadel-base-kantor-blue": {
		"text": "Kantor Blue",
		"brand": "citadel",
		"line": "base",
		"category": "colors",
		"official-name": "Citadel Base Kantor Blue",
		"url": "https://www.games-workshop.com/en-US/Base-Kantor-Blue-2019",
	},
	"citadel-layer-genestealer-purple": {
		"text": "Genestealer Purple",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Genestealer Purple",
		"url": "https://www.games-workshop.com/en-US/Layer-Genestealer-Purple-2019s",
	},
	"citadel-layer-xereus-purple": {
		"text": "Xereus Purple",
		"brand": "citadel",
		"line": "layer",
		"category": "colors",
		"official-name": "Citadel Layer Xereus Purple",
		"url": "https://www.games-workshop.com/en-US/Layer-Xereus-Purple-2019",
	},
}





# ============================================================================ #
_metallics = {
	"citadel-dry-necron-compound": {
		"text": "Necron Compound",
		"brand": "citadel",
		"line": "dry",
		"category": "metallics",
		"official-name": "Citadel Dry Necron Compound",
		"url": "https://www.games-workshop.com/en-US/Dry-Necron-Compound-2019",
	},
	"citadel-layer-stormhost-silver": {
		"text": "Stormhost Silver",
		"brand": "citadel",
		"line": "layer",
		"category": "metallics",
		"official-name": "Citadel Layer Stormhost Silver",
		"url": "https://www.games-workshop.com/en-US/Layer-Stormhost-Silver-2019",
	},
	"vallejo-metal-color-aluminium": {
		"text": "Aluminium",
		"brand": "vallejo",
		"line": "metal",
		"category": "metallics",
		"official-name": "Vallejo Metal Color 77.701 Aluminium",
		"url": "https://acrylicosvallejo.com/en/product/hobby/metal-color-en/aluminium-77701/",
	},
	"vallejo-model-color-silver": {
		"text": "Silver",
		"brand": "vallejo",
		"line": "model-color",
		"category": "metallics",
		"official-name": "Vallejo Model Color 70.997 Silver",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/silver-70997/",
	},
	"vallejo-game-color-silver": {
		"text": "Silver",
		"brand": "vallejo",
		"line": "game-color",
		"category": "metallics",
		"official-name": "Vallejo Game Color 72.052 Silver",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/silver-72052/",
	},
	"citadel-base-leadbelcher": {
		"text": "Leadbelcher",
		"brand": "citadel",
		"line": "base",
		"category": "metallics",
		"official-name": "Citadel Base Leadbelcher",
		"url": "https://www.games-workshop.com/en-US/Base-Leadbelcher-2019",
	},
	"vallejo-game-color-gunmetal": {
		"text": "Gunmetal",
		"brand": "vallejo",
		"line": "game-color",
		"category": "metallics",
		"official-name": "Vallejo Game Color 72.054 Gunmetal",
		"url": "https://acrylicosvallejo.com/en/product/hobby/game-color-en/gunmetal-72054/",
	},
	"citadel-layer-brass-scorpion": {
		"text": "Brass Scorpion",
		"brand": "citadel",
		"line": "layer",
		"category": "metallics",
		"official-name": "Citadel Layer Brass Scorpion",
		"url": "https://www.games-workshop.com/en-US/Layer-Brass-Scorpion-2019s",
	},
	"citadel-layer-auric-armour-gold": {
		"text": "Auric Armour Gold",
		"brand": "citadel",
		"line": "layer",
		"category": "metallics",
		"official-name": "Citadel Layer Auric Armour Gold",
		"url": "https://www.games-workshop.com/en-US/Layer-Auric-Armour-Gold-2019",
	},
	"vallejo-model-color-gold": {
		"text": "Gold",
		"brand": "vallejo",
		"line": "model-color",
		"category": "metallics",
		"official-name": "Vallejo Model Color 70.996 Gold",
		"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/gold-70996/",
	},
}





# ============================================================================ #
_washes = {
	
}





# ============================================================================ #
_contrasts = {

}





# ============================================================================ #
_inks = {

}





# ============================================================================ #
_technicals = {

}





# ============================================================================ #
_varnishes = {

}





# ============================================================================ #
_additives = {

}





# ============================================================================ #
_primers = {
	"vallejo-surface-primer-white": {
		"text": "White",
		"brand": "vallejo",
		"line": "surface-primer",
		"category": "primers",
		"official-name": "Vallejo Surface Primer 73.600 White",
		"url": "https://acrylicosvallejo.com/en/product/hobby/surface-primer-en/white-70600/s",
	},
	"tamiya-surface-primer-l-grey": {
		"text": "Grey",
		"brand": "tamiya",
		"line": "surface-primer-l",
		"category": "primers",
		"official-name": "Tamiya Surface Primer L Grey #87042",
		"url": "https://www.tamiyausa.com/shop/finishing/surface-primer-l-gray/",
	},
	"vallejo-surface-primer-usn-light-ghost-grey": {
		"text": "USN Light Ghost Grey",
		"brand": "vallejo",
		"line": "surface-primer",
		"category": "primers",
		"official-name": "Vallejo Surface Primer 73.615 USN Light Ghost Grey",
		"url": "https://acrylicosvallejo.com/en/product/hobby/surface-primer-en/usn-light-ghost-grey-70615/",
	},
	"army-painter-warpaints-brush-on-primer": {
		"text": "Brush-On Primer",
		"brand": "army-painter",
		"line": "warpaints",
		"category": "primers",
		"official-name": "The Army Painter Warpaints Brush-On Primer",
		"url": "https://shop.thearmypainter.com/products.php?ProductGroupId=22#Brush-On%20Primers",
	},
	"vallejo-surface-primer-black": {
		"text": "Black",
		"brand": "vallejo",
		"line": "surface-primer",
		"category": "primers",
		"official-name": "Vallejo Surface Primer 73.602 Black",
		"url": "https://acrylicosvallejo.com/en/product/hobby/surface-primer-en/black-70602/",
	},
	"citadel-sprays-chaos-black-primer": {
		"text": "Chaos Black Primer",
		"brand": "citadel",
		"line": "sprays",
		"category": "primers",
		"official-name": "Citadel Sprays Chaos Black (Primer)",
		"url": "https://www.games-workshop.com/en-US/Chaos-Black-Spray-US-2020s",
	},
}





# ============================================================================ #
paints = {}
paints.update(_colors)
paints.update(_metallics)
paints.update(_washes)
paints.update(_contrasts)
paints.update(_inks)
paints.update(_technicals)
paints.update(_varnishes)
paints.update(_additives)
paints.update(_primers)





# ============================================================================ #
_i = 0
for category_id in paint_categories.keys():
	paint_categories[category_id]['index'] = _i
	_i += 1

_i = 0
for brand_id in paint_brands.keys():
	paint_brands[brand_id]['index'] = _i
	_i = 0

_i = 0
for paint_id in paints.keys():
	paints[paint_id]['index'] = _i
	_i += 1





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')