from data_common import FP_, _FP, NBP_, _NBP, MN_, _MN, TT_, _TT_, _TT, I_, _I, B_, _B
from data_common import *
from data_pages_posts import *





# Make sure to always use trailing commas!
# Press Alt+Z to toggle word-wrap when typing paragraphs!





# ============================================================================ #
pages = {
	"home": {
		"title": "Necrominis Mini-Painting Studio",
		"type": "home",
		"paragraphs": [
			f"""{FP_}I'm {MN_}Tucker{_MN} from {MN_}Necrominis{_MN}, and I'm a miniature painter hobbyist.{_FP}""",
			
			f"""I first tried painting miniatures in 2015, for the {I_}[Dungeons & Dragons](https://dnd.wizards.com/what-is-dnd){_I} tabletop roleplaying game. In 2019, I took on miniature painting as a serious hobby and have been improving my craft every since.""",
			
			f"""I still paint miniatures for tabletop games like {I_}[D&D](https://dnd.wizards.com/what-is-dnd){_I}, {I_}[Warhemmer](https://www.warhammer-community.com/en-us){_I}, and {I_}[Star Wars: Legion](https://www.fantasyflightgames.com/en/products/star-wars-legion){_I}, but now I also paint for the sole purpose of painting beautiful display miniatures, as well.""",
			
			f"""I've also purchased an {I_}[AnyCubic Photon S](https://www.anycubic.com/products/anycubic-photon-s){_I}, in 2020, and have been {TT_}3D printing{_TT_}{THREE_D_PRINTING}{_TT} resin miniatures ever since. Most of the models I print are purchased from {I_}[My Mini Factory](https://www.myminifactory.com){_I} or from artists I support on {I_}[Patreon](https://www.patreon.com){_I}.""",
		]
	},
	# ============================================================================ #
	"my-paints": {
		"title": "My Paint Collection",
		"type": "my-paints",
		"lists": {
			
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
			# Added with code below.
		],
	},
}

pages.update(posts)





# Populate gallery pages list with all post-type pages.
# ============================================================================ #
for post_id in posts.keys():
	pages['gallery']['pages'].append(post_id)





# Populate my-paints paints list with all paints.
# ============================================================================ #
# TODO





# ============================================================================ #
_i = 0
for page_id in pages.keys():
	pages[page_id]['index'] = _i
	_i += 1