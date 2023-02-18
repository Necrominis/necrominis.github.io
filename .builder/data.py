from printer import *
from data_image_paths import *
from data_tags import *
from data_manufacturers import *
from data_supplies import *
from data_paints import *
from data_pages import *





# Make sure to always use trailing commas!





data = {
	"website": "https://necrominis.github.io/",
	"website-local": "/home/tucker/dev/necrominis.github.io/",

	"image-paths": image_paths,
	"no-image": "necrominis-missing-image.jpg", # In the ./images/posts/ directory
	"no-image-thumbnail": "necrominis-missing-image.jpg", # In the ./images/posts/ directory
	"no-paint": "necrominis-paint-icon-full-grey.png", # In the ./images/paint-icons/ directory
	"blank-paint": "necrominis-blank-paint-icon.png", # In the ./images/paint-icons/ directory

	"tags": tags,
	"manufacturers": manufacturers,

	"supplies-categories": supplies_categories,
	"supplies-brands": supplies_brands,
	"supplies": supplies,

	"paint-categories": paint_categories,
	"paint-brands": paint_brands,
	"paints": paints,
	
	"pages": pages,
}





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')