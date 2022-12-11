# Make sure to always use trailing commas!
# Make sure to sort supplies alphabetically!





# ============================================================================ #
supplies_categories = {
	"tools": {
		"text": "Tools",
	},
	"brushes": {
		"text": "Brushes",
	},
	"equipment": {
		"text": "Equipment",
	},
	"materials": {
		"text": "Materials",
	},
	"bases": {
		"text": "Bases",
	},
	"other": {
		"text": "Other Supplies",
	},
}





# ============================================================================ #
supplies_brands = {
	"badger": {
		"text": "Badger",
	},
	"anycubic": {
		"text": "Anycubic",
	},
}





# ============================================================================ #
_tools = {
	"army-painter-sculpting-tools": {
		"text": "Sculpting Tools",
		"brand": "Army Painter",
		"category": "tools",
		"official-name": "The Army Painter Sculpting Tools",
		"url": "https://www.amazon.com/Army-Painter-Sculpting-Tools-Double-Sided/dp/B07PVBRQS1",
	},
}





# ============================================================================ #
_brushes = {
	"105-patriot-air-brush": {
		"text": "105 Patriot Air-Brush",
		"brand": "badger",
		"category": "brushes",
		"official-name": "Badger Air-Brush Co. Model 105 Patriot",
		"url": "https://www.amazon.com/Badger-Air-Brush-Co-Patriot-Airbrush/dp/B002W84GTO/ref=sr_1_1?crid=13TABVFPVOAAP&keywords=badger%2B105%2Bairbrush&qid=1647451154&sprefix=badger%2B105airbrush%2Caps%2C99&sr=8-1&th=1",
	},
}





# ============================================================================ #
_equipment = {
	"anycubic-photon-s": {
		"text": "Photon S",
		"brand": "anycubic",
		"category": "equipment",
		"official-name": "Anycubic Photon S",
		"url": "https://www.anycubic.com/products/anycubic-photon-s",
	},
}





# ============================================================================ #
_materials = {

}





# ============================================================================ #
_bases = {

}





# ============================================================================ #
_other = {

}






# ============================================================================ #
supplies = {}
supplies.update(_tools)
supplies.update(_brushes)
supplies.update(_equipment)
supplies.update(_materials)
supplies.update(_bases)
supplies.update(_other)





# ============================================================================ #
_i = 0
for category_id in supplies_categories.keys():
	supplies_categories[category_id]['index'] = _i
	_i += 1

_i = 0
for brand_id in supplies_brands.keys():
	supplies_brands[brand_id]['index'] = _i
	_i = 0

_i = 0
for supplies_id in supplies.keys():
	supplies[supplies_id]['index'] = _i
	_i += 1