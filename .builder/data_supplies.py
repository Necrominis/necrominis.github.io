# Make sure to always use trailing commas!





# ============================================================================ #
supplies_categories = {
	"brushes": {
		"text": "Brushes",
	},
}





# ============================================================================ #
supplies_brands = {
	"badger": {
		"text": "Badger",
	},
}





# ============================================================================ #
supplies = {
	"105-patriot-air-brush": {
		"text": "105 Patriot Air-Brush",
		"brand": "badger",
		"category": "brushes",
		"official-name": "Badger Air-Brush Co. Model 105 Patriot",
		"url": "https://www.amazon.com/Badger-Air-Brush-Co-Patriot-Airbrush/dp/B002W84GTO/ref=sr_1_1?crid=13TABVFPVOAAP&keywords=badger%2B105%2Bairbrush&qid=1647451154&sprefix=badger%2B105airbrush%2Caps%2C99&sr=8-1&th=1",
	},
}





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