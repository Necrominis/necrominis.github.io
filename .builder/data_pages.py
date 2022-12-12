from data_common import *
from printer import *
from data_pages_posts import *





# Make sure to always use trailing commas!
# Press Alt+Z to toggle word-wrap when typing paragraphs!





# ============================================================================ #
pages = {
	"404": {
		"title": "404: Page Not Found",
		"type": "404",
		"paragraphs": [
			f""":Uh-oh! This page doesn't seem to exist!""",
		],
	},
	"home": {
		"title": "Necrominis Mini-Painting Studio",
		"type": "home",
		"paragraphs": [
			f""":I'm [[Tucker]] from [[Necrominis]], and I'm a miniature painter hobbyist.""",
			
			f"""I first tried painting miniatures in 2015, for the [*Dungeons & Dragons*]({URL_DND}) tabletop roleplaying game. In 2019, I took on miniature painting as a serious hobby and have been improving my craft every since.""",
			
			f"""I still paint miniatures for tabletop games like *[D&D]({URL_DND})*, *[Warhammer]({URL_WARHAMMER})*, and *[Star Wars: Legion]({URL_STAR_WARS_LEGION})*, but now I also paint for the sole purpose of painting beautiful display miniatures, as well.""",
			
			f"""I've also purchased an *[Anycubic Photon S](anycubic-photon-s)*, in 2020, and have been [3D printing]T({TT_3D_PRINTING}) resin miniatures ever since. Most of the models I print are purchased from *[My Mini Factory]({URL_MY_MINI_FACTORY})* or from artists I support on *[Patreon]({URL_PATREON})*.""",
		],
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





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')