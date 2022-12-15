from data import data
from common import *
from printer import *
from processor import *




# The following are assumed to exist and required for this to work:
# data['image-paths']['post-photos']
# data['no-image']
# data['no-paint']
# data['blank-paint']
# data['tags'][tag_id]['text']
# data['tags'][tag_id]['color']
# data['pages']['gallery']['pages']
# data['pages'][page_id]['properties']
# data['pages'][page_id]['properties']['tags'][tag_id]
# data['pages'][page_id]['properties']['tags'][tag_id]['text']
# data['pages'][page_id]['properties']['tags'][tag_id]['color']
# data['pages'][page_id]['properties']['tags'][tag_id]['linked-page']
# data['pages'][page_id]['images']
# data['pages'][page_id]['paragraphs']
# data['pages'][page_id]['paints-used']
# data['paint-brands'][brand_id]['text']
# data['paint-brands'][brand_id]['lines'][line_id]['text']
# data['paints'][paint_id]['text']
# data['paints'][paint_id]['brand']
# data['paints'][paint_id]['line']
# data['paints'][paint_id]['icon']
# data['paints'][paint_id]['icon-css']
# data['paints'][paint_id]['official-name']
# data['paints'][paint_id]['url']





	# ============================================================================ #
	#                                    COMMON                                    #
	# ============================================================================ #





# Build the list of paragraphs HTML for page.
# ======================================================================================= #
def build_paragraphs_html(page_id: str) -> str:
	paragraphs = data['pages'][page_id]['paragraphs']

	# Go through each paragraph line, build the HTML, and combine them.
	paragraphs_html = ''
	for paragraph in paragraphs:
		# Remove newlines and tabs from paragraph (so data can be multi-lined without breaking things).
		single_lined_paragraph = paragraph.replace('\n', '').replace('\t', '')

		# Process markdown in paragraph.
		single_lined_paragraph = process_paragraph(single_lined_paragraph)

		# Build and add the paragraph HTML.
		paragraph_html = read_html_file('paragraph.html')
		paragraph_html = paragraph_html.replace('<!--PARAGRAPH-->', single_lined_paragraph)
		paragraphs_html += paragraph_html

	return paragraphs_html





# Build the paragraphs section HTML for page.
# ======================================================================================= #
def build_paragraphs_section_html(page_id: str) -> str:
	# Get the starter paragraphs HTML.
	paragraphs_html = read_html_file('paragraphs.html')

	# Go through each paragraph line, build the HTML, and combine them.
	paragraph_lines_html = build_paragraphs_html(page_id)

	# Add the paragraph lines HTML into the final paragraphs HTML and return it.
	paragraphs_html = paragraphs_html.replace('<!--PARAGRAPHS-->', paragraph_lines_html)
	return paragraphs_html





	# ============================================================================ #
	#                                  PROPERTIES                                  #
	# ============================================================================ #





# Build the models property HTML for a post page.
# ======================================================================================= #
def build_models_property_html(page_id: str) -> str:
	models_list = data['pages'][page_id]['properties']['models']
	
	# Get the models property starter HTML.
	models_html = read_html_file('models-property.html')

	# Go through each manufacturer item, build the HTML, and combine them.
	model_items_html = ''
	for i in range(len(models_list)):
		model = models_list[i]
		model_text = model['text']
		model_url = model['url']

		model_html = read_html_file('models-property-item.html')
		model_html = model_html.replace('<!--MODEL-->', model_text)
		model_html = model_html.replace('<!--URL-->', model_url)
		
		model_items_html += model_html

		# Add a comma seperation to all but the last model.
		if i < len(models_list) - 1:
			model_items_html += ', '

	# Add the model items HTML into the final models HTML and return it.
	models_html = models_html.replace('<!--MODELS-->', model_items_html)
	return models_html





# Build the manufacturers property HTML for a post page.
# ======================================================================================= #
def build_manufacturers_property_html(page_id: str) -> str:
	manufacturers_list = data['pages'][page_id]['properties']['manufacturers']
	
	# Get the manufacturers property starter HTML.
	manufacturers_html = read_html_file('manufacturers-property.html')

	# Go through each manufacturer item, build the HTML, and combine them.
	manufacturer_items_html = ''
	for manufacturer_id in manufacturers_list:
		manufacturer = data['manufacturers'][manufacturer_id]
		manufacturer_color = manufacturer['color']
		manufacturer_text = manufacturer['text']
		manufacturer_url = manufacturer['url']

		manufacturer_html = read_html_file('manufacturers-property-item.html')
		manufacturer_html = manufacturer_html.replace('<!--COLOR-->', manufacturer_color)
		manufacturer_html = manufacturer_html.replace('<!--MANUFACTURER-->', manufacturer_text)
		manufacturer_html = manufacturer_html.replace('<!--URL-->', manufacturer_url)

		manufacturer_items_html += manufacturer_html

	# Add the manufacturer items HTML into the final manufacturers HTML and return it.
	manufacturers_html = manufacturers_html.replace('<!--MANUFACTURERS-->', manufacturer_items_html)
	return manufacturers_html





# Build the created date property HTML for a post page.
# ======================================================================================= #
def build_created_property_html(page_id: str) -> str:
	created_date = data['pages'][page_id]['properties']['created']

	# Get the created property starter HTML and put the created date in.
	created_html = read_html_file('created-property.html')
	created_html = created_html.replace('<!--DATE-->', created_date)

	return created_html





# Build the tags property HTML for a post page.
# ======================================================================================= #
def build_tags_property_html(page_id: str) -> str:
	tags_list = data['pages'][page_id]['properties']['tags']

	# Get the tags property starter HTML.
	tags_html = read_html_file('tags-property.html')

	# Go through each tag item, build the HTML, and combine them.
	tag_items_html = ''
	for tag_id in tags_list:
		tag = data['tags'][tag_id]
		tag_color = tag['color']
		tag_text = tag['text']
		tag_url = page_id_to_url(tag['linked-page'])

		tag_html = read_html_file('tags-property-item.html')
		tag_html = tag_html.replace('<!--COLOR-->', tag_color)
		tag_html = tag_html.replace('<!--TAG-->', tag_text)
		tag_html = tag_html.replace('<!--URL-->', tag_url)

		tag_items_html += tag_html
	
	# Add the tag items HTML into the final tags HTML and return it.
	tags_html = tags_html.replace('<!--TAGS-->', tag_items_html)
	return tags_html





	# ============================================================================ #
	#                                     POST                                     #
	# ============================================================================ #





# Build the paint icon HTML for a paints or paints-used section.
# ======================================================================================= #
def build_paint_icon_html(paint_id: str) -> str:
	paint = data['paints'][paint_id]

	# Choose icon image based on paint data.
	icon_path = data['no-paint']
	style_css = ''
	# Specified icon file.
	if 'icon' in paint.keys():
		icon_path = paint['icon']
	# Specified icon CSS.
	elif 'icon-css' in paint.keys():
		icon_path = data['blank-paint']
		style_css = paint['icon-css']

	# Place the icon into the HTML.
	icon_html = read_html_file('paint-icon.html')
	icon_html = icon_html.replace('<!--PAINT-ICON-->', icon_path)
	icon_html = icon_html.replace('<!--ICON-STYLE-->', style_css)

	return icon_html





# Build the paint item HTML for a paints or paints-used section.
# ======================================================================================= #
def build_paint_item_html(paint_id: str) -> str:
	paint = data['paints'][paint_id]

	# Get the brand data.
	brand_id = paint['brand']
	brand = data['paint-brands'][brand_id]
	brand_text = brand['text']
	# Get the paint line data.
	line_id = paint['line']
	line = brand['lines'][line_id]
	line_text = line['text']
	# Get the paint color data.
	color_text = paint['text']
	# Get the final paint data. (TODO: page and official-name)
	icon_html = build_paint_icon_html(paint_id)
	url = paint['url']
	paint_name = f'{brand_text}{separator}{line_text}{separator}{color_text}'

	# Get the paint item starter HTML.
	paint_item_html = read_html_file('paint-item.html')

	# Replace the HTML with the paint's data.
	paint_item_html = paint_item_html.replace('<!--PAINT-ICON-->', icon_html)
	paint_item_html = paint_item_html.replace('<!--URL-->', url)
	paint_item_html = paint_item_html.replace('<!--PAINT-->', paint_name)

	return paint_item_html





# Build the paints-used HTML for a post page.
# ======================================================================================= #
def build_paints_list_html(paint_ids: '[str]') -> str:
	# GO through each paint, build the list item HTML, and combine them.
	paint_items_html = ''
	for paint_id in sort_paints(paint_ids, True):
		# Place breaks between paints if a paint item is empty.
		if paint_id == '':
			paint_items_html += read_html_file('paints-used-separator.html')
			continue

		# Build the paint item HTML and add it to the list.
		paint_item_html = build_paint_item_html(paint_id)
		paint_items_html += paint_item_html
	
	return paint_items_html





# Build the paints-used HTML for a post page.
# ======================================================================================= #
def build_paints_used_html(page_id: str) -> str:
	paints_used_ids = data['pages'][page_id]['paints-used']

	# Get the paints-used starter HTML.
	paints_used_html = read_html_file('paints-used.html')

	# GO through each paint, build the list item HTML, and combine them.
	paint_items_html = build_paints_list_html(paints_used_ids)

	# Add the paint items HTML to the final paints-used HTML and return it.
	paints_used_html = paints_used_html.replace('<!--PAINTS-->', paint_items_html)
	return paints_used_html





# Build the slideshow HTML for a post page.
# ======================================================================================= #
def build_slideshow_html(page_id: str) -> str:
	image_files = data['pages'][page_id]['images']

	# Handle no images being specified by the post.
	if len(image_files) == 0:
		image_files = [data['no-image']]
		print_warning('Missing image reference for slideshow on page with ID: ', page_id)

	# Get the starter slideshow HTML.
	slideshow_html = read_html_file('slideshow.html')

	# Go through each image, build the slide HTML, and combine them.
	slides_html = ''
	for image_file in image_files:
		# Use missing image image if the image file can't be found.
		_image_file = image_file
		if not os.path.isfile(data['image-paths']['post-photos']):
			_image_file = data['no-image']
		# Add the image to the slide HTML.
		slide_html = read_html_file('slideshow-slide.html')
		slide_html = slide_html.replace('<!--SLIDE-IMAGE-->', _image_file)
		slides_html += slide_html
	
	# If there are multiple images, add the slideshow arrows and dots.
	if len(image_files) > 1:
		# Adds slideshow arrows.
		arrows_html = read_html_file('slideshow-arrows.html')
		slideshow_html = slideshow_html.replace('<!--ARROWS-->', arrows_html)
	
		# Add a dot for each slide.
		dots_html = ''
		for slide_index in range(len(image_files)):
			dot_html = read_html_file('slideshow-dot.html')
			dot_html = dot_html.replace('1', f'{slide_index + 1}') # Slide indices start at 1 not 0.
			dots_html += dot_html
		slideshow_html = slideshow_html.replace('<!--DOTS-->', dots_html)
	
	# Add the slides HTML into the final slideshow HTML and return it.
	slideshow_html = slideshow_html.replace('<!--SLIDES-->', slides_html)
	return slideshow_html





# Build the article content HTML for a post page.
# ======================================================================================= #
def build_post_properties_html(page_id: str) -> str:
	# Get the starter post properties HTML.
	properties_html = read_html_file('properties.html')

	property_items_html = ''

	# Build and add the created property HTML.
	created_html = build_created_property_html(page_id)
	property_items_html += created_html

	# Build and add the tags property HTML.
	tags_html = build_tags_property_html(page_id)
	property_items_html += tags_html

	# Build and add the manufacturers property HTML.
	manufacturers_html = build_manufacturers_property_html(page_id)
	property_items_html += manufacturers_html

	# Build and add the models property HTML.
	models_html = build_models_property_html(page_id)
	property_items_html += models_html

	# Finally, place all the property items HTML into the properties HTML.
	properties_html = properties_html.replace('<!--PROPERTIES-->', property_items_html)
	return properties_html





# Build the article content HTML for a post page.
# ======================================================================================= #
def build_post_article_content_html(page_id: str) -> str:
	# Get the starter article content HTML.
	article_content = read_html_file('post-article-content.html')

	# Get the properties HTML and add it to the article content HTML.
	properties_html = build_post_properties_html(page_id)
	article_content = article_content.replace('<!--PROPERTIES-->', properties_html)

	# Get the slideshow HTML and add it to the article content HTML.
	slideshow_html = build_slideshow_html(page_id)
	article_content = article_content.replace('<!--SLIDESHOW-->', slideshow_html)

	# Get the paragraphs HTML and add it to the article content HTML.
	paragraphs_html = build_paragraphs_section_html(page_id)
	article_content = article_content.replace('<!--PARAGRAPHS-->', paragraphs_html)

	# Get the paints-used HTML and add it to the article content HTML.
	paints_used_html = build_paints_used_html(page_id)
	article_content = article_content.replace('<!--PAINTS-USED-->', paints_used_html)

	return article_content





	# ============================================================================ #
	#                                    PAINTS                                    #
	# ============================================================================ #





# Build the article content HTML for the paints home page.
# ======================================================================================= #
def build_paints_article_content_html(page_id: str) -> str:
	# TODO
	return UNFINISHED





# Build the article content HTML for a paint item page.
# ======================================================================================= #
def build_paint_article_content_html(page_id: str) -> str:
	# TODO
	return UNFINISHED





	# ============================================================================ #
	#                                   SUPPLIES                                   #
	# ============================================================================ #





# Build the article content HTML for the supplies home page.
# ======================================================================================= #
def build_supplies_article_content_html(page_id: str) -> str:
	# TODO
	return UNFINISHED





# Build the article content HTML for a supplies item page.
# ======================================================================================= #
def build_supply_article_content_html(page_id: str) -> str:
	# TODO
	return UNFINISHED





	# ============================================================================ #
	#                                    GALLERY                                   #
	# ============================================================================ #





# Build the filters HTML for a gallery.
# ======================================================================================= #
def build_gallery_filters_html(page_id: str) -> str:
	tags = data['tags']

	# Get gallery filters starter HTML.
	gallery_filters_html = read_html_file('gallery-filters.html')

	# Go through each filter and add it to a list of filters.
	filters_html = ''
	for tag_id in tags.keys():
		# Skip the WIP tag, since it's custom-made.
		if tag_id == 'wip':
			continue

		# Get the tag filter data.
		tag_text = tags[tag_id]['text']
		tag_color = tags[tag_id]['color']

		# Build the filter HTML.
		filter_html = read_html_file('gallery-filter.html')
		filter_html = filter_html.replace('<!--COLOR-->', tag_color)
		filter_html = filter_html.replace('<!--ID-->', tag_id)
		filter_html = filter_html.replace('<!--NAME-->', tag_text)

		# Add the filter HTML to the filters HTML.
		filters_html += filter_html
	
	# Add the filters HTML to the gallery filters HTML.
	gallery_filters_html = gallery_filters_html.replace('<!--FILTERS-->', filters_html)

	return gallery_filters_html





# Build the items HTML for a gallery.
# ======================================================================================= #
def build_gallery_items_html(page_id: str) -> str:
	gallery_page = data['pages'][page_id]
	page_ids = sort_pages(gallery_page['pages'])

	# Get gallery starter HTML.
	gallery_items_html = read_html_file('gallery-items.html')

	# Get the gallery items starter HTML.
	gallery_items_html = read_html_file('gallery-items.html')

	# Go through each item and add a list of items.
	items_html = ''
	for item_page_id in page_ids:
		# Get the page (gallery item) data.
		page = data['pages'][item_page_id]
		page_url = page_id_to_url(item_page_id)
		page_tag_ids = page['properties']['tags']

		# Pick either the first page image, or the default no-image.
		page_image = data['no-image']
		if 'images' in page.keys() and len(page['images']) > 0:
			page_image = page['images'][0]
		else:
			print_warning('Missing image reference for slideshow on page with ID: ', page_id)

		# Build the starter gallery item HTML, and add the image and URL.
		item_html = read_html_file('gallery-item.html')
		item_html = item_html.replace('<!--URL-->', page_url)
		item_html = item_html.replace('<!--IMAGE-->', page_image)

		# Get the filter tags CSS for the item's page.
		tags_css = 'all '
		for tag_id in page_tag_ids:
			tags_css += f'{tag_id} '
		tags_css = tags_css[:len(tags_css)-1] # Remove trailing space.
		# Include WIP alone, and don't show it in any other filters.
		if 'wip' in page_tag_ids:
			tags_css = 'wip'
		
		# Add the filter tags CSS to the HTML.
		item_html = item_html.replace('<!--FILTERS-->', tags_css)

		# Add the item HTML to the items list HTML.
		items_html += item_html

	# Add the items HTML to the gallery items HTML.
	gallery_items_html = gallery_items_html.replace('<!--ITEMS-->', items_html)

	return gallery_items_html





# Build a gallery HTML.
# ======================================================================================= #
def build_gallery_html(page_id: str) -> str:
	# Get gallery starter HTML.
	gallery_html = read_html_file('gallery.html')

	# Build and add the filters HTML to the gallery HTML.
	gallery_filters_html = build_gallery_filters_html(page_id)
	gallery_html = gallery_html.replace('<!--FILTERS-->', gallery_filters_html)

	# Build and add the items HTML to the gallery HTML.
	gallery_items_html = build_gallery_items_html(page_id)
	gallery_html = gallery_html.replace('<!--ITEMS-->', gallery_items_html)

	return gallery_html





# Build the article content HTML for the gallery page.
# ======================================================================================= #
def build_gallery_article_content_html(page_id: str) -> str:
	# Get gallery starter HTML.
	gallery_article_content_html = read_html_file('gallery-article-content.html')

	# Build the gallery HTML and place it into the article content HTML
	gallery_html = build_gallery_html(page_id)
	gallery_article_content_html = gallery_article_content_html.replace('<!--GALLERY-->', gallery_html)

	return gallery_article_content_html





	# ============================================================================ #
	#                                     HOME                                     #
	# ============================================================================ #





# Build the article content HTML for the home page.
# ======================================================================================= #
def build_home_article_content_html(page_id: str) -> str:
	# Get the starter home article content HTML.
	home_html = read_html_file('home-article-content.html')

	# Build and add the paragraphs HTML.
	paragraphs_html = build_paragraphs_html(page_id)
	home_html = home_html.replace('<!--PARAGRAPHS-->', paragraphs_html)

	# Build and add the gallery HTML.
	gallery_html = build_gallery_html('gallery')
	home_html = home_html.replace('<!--GALLERY-->', gallery_html)

	return home_html





	# ============================================================================ #
	#                                     404                                      #
	# ============================================================================ #





# Build the article content HTML for the home page.
# ======================================================================================= #
def build_404_article_content_html(page_id: str) -> str:
	# Get the starter 404 article content HTML.
	error_404_html = read_html_file('404-article-content.html')

	# Build and add the paragraphs HTML.
	paragraphs_html = build_paragraphs_html(page_id)
	error_404_html = error_404_html.replace('<!--PARAGRAPHS-->', paragraphs_html)

	return error_404_html





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')