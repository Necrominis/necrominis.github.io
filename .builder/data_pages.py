from data_common import FP_, _FP, MN_, _MN, TT_, _TT_, _TT, A_, _A_, _A, I_, _I, IA_, _IA_, _IA, B_, _B
from data_pages_posts import *





# Make sure to always use trailing commas!





# ============================================================================ #
pages = {
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
			"colors": {
				"text": "Color Paints",
				"paints": [
				],
			},
			"metallics": {
				"text": "Metallic Paints",
				"paints": [
				],
			},
			"washes": {
				"text": "Washes",
				"paints": [
				],
			},
			"shades": {
				"text": "Shades",
				"paints": [
				],
			},
			"contrasts": {
				"text": "Contrasts",
				"paints": [
				],
			},
			"inks": {
				"text": "Inks",
				"paints": [
				],
			},
			"technicals": {
				"text": "Technicals",
				"paints": [
				],
			},
			"textures": {
				"text": "Textures",
				"paints": [
				],
			},
			"varnishes": {
				"text": "Varnishes",
				"paints": [
				],
			},
			"additives": {
				"text": "Additives",
				"paints": [
				],
			},
			"primers": {
				"text": "Primers",
				"paints": [
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
}

pages.update(posts)