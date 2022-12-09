# Make sure to always use trailing commas!
# Dates are DD-MM-YYYY!
# Put bold/italic outside of hyperlinks!
#
# First Paragraph:	<mark class="first-paragraph">{text}</mark>
# Mini Name:		<mark class="mini-name">{text}</mark>
# Tooltip:			<mark class="tooltip">{inline_text}<span class="tip">{tip_description}</span></mark>
# Link:				<a href="{url}">{text}</a>





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
			"color": "grey",
			"linked-page": "gallery",
		},
		"technique-testing": {
			"text": "Technique Testing",
			"color": "green",
			"linked-page": "gallery",
		},
		"wip": {
			"text": "Work in Progress",
			"color": "grey",
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

	"paints": {
		"separator": " / ",
		"brands": {
			"vallejo": {
				"text": "Vallejo",
				"lines": {
					"model-color": {
						"text": "Model Color",
						"colors": {
							"black": {
								"text": "Black",
								"icon": "vallejo-model-color-black.png",
								"page": "vallejo-model-color-black",
								"official-name": "Vallejo Model Color 70.950 Black",
								"url": "https://acrylicosvallejo.com/en/product/hobby/model-color-en/black-70950/",
							}
						},
					},
				},
			},
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
				"""<mark class="first-paragraph">I'm <mark class="mini-name">Tucker</mark> from <mark class="mini-name">Necrominis</mark>, and I'm a miniature painter hobbyist.</mark>""",
				"""I first tried painting miniatures in 2015, for the <i><a href="https://dnd.wizards.com/what-is-dnd">Dungeons & Dragons</a></i> tabletop roleplaying game. In 2019, I took on miniature painting as a serious hobby and have been improving my craft every since.""",
				"""I still paint miniatures for tabletop games like <i><a href="https://dnd.wizards.com/what-is-dnd">D&D</a></i>, <i><a href="https://www.warhammer-community.com/en-us">Warhammer</a></i>, and <i><a href="https://www.fantasyflightgames.com/en/products/star-wars-legion">Star Wars: Legion</a></i>, but now I also paint for the sole purpose of painting beautiful display miniatures, as well.""",
				"""I've also purchased an <i><a href="https://www.anycubic.com/products/anycubic-photon-s">AnyCubic Photon S</a></i>, in 2020, and have been <mark class="tooltip">3D printing<span class="tip">3D printing is the construction of physical objects from a digital 3D model file.</span></mark> resin miniatures ever since. Most of the models I print are purchased from <i><a href="https://www.myminifactory.com">My Mini Factory</a></i> or from artists I support on <i><a href="https://www.patreon.com">Patreon</a></i>.""",
			]
		},
		# ============================================================================ #
		"my-paints": {
			"title": "My Paints",
			"type": "my-paints",
		},
		# ============================================================================ #
		"my-supplies": {
			"title": "My Supplies",
			"type": "my-supplies",
		},
		# ============================================================================ #
		"gallery": {
			"title": "Gallery",
			"type": "gallery",
			"pages": [
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
				"10-06-2022",
			],
		},
		# ============================================================================ #
		"10-06-2022": {
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
						"url": "https://www.games-workshop.com/en-US/WHU-The-Crimson-Court-EN-2021"
					},
				],
			},
			"images": [
				"necrominis-10-06-2022-raw-1.jpeg",
				"necrominis-10-06-2022-raw-2.jpeg",
				"necrominis-10-06-2022-raw-3.jpeg",
				"necrominis-10-06-2022-raw-4.jpeg",
			],
			"paragraphs": [
				"""<mark class="first-paragraph">A <mark class="mini-name">Soulblight Gravelord Vampire</mark> painted with a necromancy magic scheme.</mark>""",
				"""The first thing I worked on for this miniature was actually the base. I primed it black and gave it a rough airbrushing of a dark purple. I then wanted to create a glowing effect coming out of the cracks between the stone, so I dry-brushed dark teal around the cracks, then a lighter teal closer to the cracks, and then filled in the cracks with a lime green.""",
				"""For the actual vampire model, I started with the skin first. I layered from a medium grey to a light grey, but with some purple mixed in, with more purple in the darker tones, and more grey in the lighter tones. I used a similar technique for the wing arms, except using dark teal instead of purple. As for the actual wings, I left them black, dry-brushed dark teal toward the ends, and added a spotty texture to them.""",
				"""Seeing the rest of the model still black made me realize a dark outfit would fit the best and contrast with the light skin. The armor pieces remained black, but were highlighted toward dark purple and edge highlighted with a similar purple-grey mix from the skin's base coat. The rest of the straps, the mace, and the hair were highlighted similarly with dark to medium greys, as I wanted to avoid using metallic paints for this mini.""",
				"""The last details were a few gems and a bottle on the vampire's waist. These were painted with the two teal colors and the lime green, to remain coherent with the base.""",
				"""Finally, I airbrushed the two teal colors onto the model from below, to give the effect that the green light from the base is lighting up the vampire from below. Then I gave it a clear coat of gloss, for protective purposes, and matte for the final finish.""",
				"""All-in-all, I think this might be my best miniature yet, in terms of the color coherency, the skin shading, and the glow effect. One of my <a href="https://necrominis.github.io/post/10-06-2022/">previous miniatures</a> had a better paint job for the skin, but that was with an airbrush; this miniature's skin was painted by hand, and this one has higher contrast. I do think the wings' spots could be redone, though. I wanted to highlight the horizontal folds in the wings, but they weren't defined enough to catch the edge of my brush, and were too small to highlight by hand. Overall, though, I think this miniature turned out beautifully.""",
			],
			"paints-used": [
				{
					"brand": "vallejo",
					"line": "model-color",
					"color": "black",
				},
				"break",
			],
		},
	},
}