from data import data
from common import *





# The following are assumed to exist and required for this to work:
# data['pages'][page_id]['properties']
# data['pages'][page_id]['properties']['tags'][tag_id]
# data['pages'][page_id]['properties']['tags'][tag_id]['text']
# data['pages'][page_id]['properties']['tags'][tag_id]['color']
# data['pages'][page_id]['properties']['tags'][tag_id]['linked-page']
# data['pages'][page_id]['images']
# data['pages'][page_id]['paragraphs']





	# ============================================================================ #
	#                                    COMMON                                    #
	# ============================================================================ #





# Build the paragraphs HTML for page.
# ======================================================================================= #
def build_paragraphs_html(page_id: str) -> str:
	paragraphs = data['pages'][page_id]['paragraphs']

	# Get the starter paragraphs HTML.
	paragraphs_html = read_html_file('paragraphs.html')

	# Go through each paragraph line, build the HTML, and combine them.
	paragraph_lines_html = ''
	for paragraph in paragraphs:
		paragraph_html = read_html_file('paragraph.html')
		paragraph_html = paragraph_html.replace('<!--PARAGRAPH-->', paragraph)
		paragraph_lines_html += paragraph_html

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





# Build the paints-used HTML for a post page.
# ======================================================================================= #
def build_paints_used_html(page_id: str) -> str:
	# TODO
	return ''





# Build the slideshow HTML for a post page.
# ======================================================================================= #
def build_slideshow_html(page_id: str) -> str:
	image_files = data['pages'][page_id]['images']

	# Get the starter slideshow HTML.
	slideshow_html = read_html_file('slideshow.html')

	# Go through each image, build the slide HTML, and combine them.
	slides_html = ''
	for image_file in image_files:
		slide_html = read_html_file('slideshow-slide.html')
		slide_html = slide_html.replace('<!--SLIDE-IMAGE-->', image_file)
		slides_html += slide_html
	
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
	paragraphs_html = build_paragraphs_html(page_id)
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
	return ''





# Build the article content HTML for a paint item page.
# ======================================================================================= #
def build_paint_article_content_html(page_id: str) -> str:
	# TODO
	return ''





	# ============================================================================ #
	#                                   SUPPLIES                                   #
	# ============================================================================ #





# Build the article content HTML for the supplies home page.
# ======================================================================================= #
def build_supplies_article_content_html(page_id: str) -> str:
	# TODO
	return ''





# Build the article content HTML for a supplies item page.
# ======================================================================================= #
def build_supply_article_content_html(page_id: str) -> str:
	# TODO
	return ''





	# ============================================================================ #
	#                                    GALLERY                                   #
	# ============================================================================ #





# Build the article content HTML for the gallery page.
# ======================================================================================= #
def build_gallery_article_content_html(page_id: str) -> str:
	# TODO
	return ''





	# ============================================================================ #
	#                                     HOME                                     #
	# ============================================================================ #





# Build the article content HTML for the home page.
# ======================================================================================= #
def build_home_article_content_html(page_id: str) -> str:
	# TODO
	return ''





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print('ERROR: Run \'main.py\' instead.')