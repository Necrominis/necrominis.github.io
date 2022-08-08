import os
from data import data


# ============================================================================ #
#                               HELPER FUNCTIONS                               #
# ============================================================================ #


def read_file(filepath: str) -> str:
	file = open(filepath, 'r')
	content = file.read()
	file.close()

	return content


def write_file(filepath: str, content: str) -> None:
	# Create the folders if they don't exist yet.
	parts = filepath.split('/')
	directory = ''
	for i in range(len(parts) - 1):
		directory += parts[i] + '/'
	if not os.path.exists(directory):
		os.mkdir(directory)
	# Create/write the file.
	file = open(filepath, 'w')
	file.write(content)
	file.close()


def pretty_html(html: str) -> str:
	# Remove tabs and newlines.
	flat_html = html.replace('\n', '').replace('\t', '')
	return flat_html


def page_id_to_url(page_id: str) -> str:
	page_type_id = data['pages'][page_id]['type']

	url = 'https://necrominis.github.io/'

	if page_type_id == 'post':
		# .../post/page_id/
		url += 'posts/' + page_id + '/'
	elif page_type_id == 'home':
		# .../
		pass
	else:
		# .../page_id/
		url += page_id + '/'

	return url


# ============================================================================ #
#                            SNIPPET HTML BUILDING                             #
# ============================================================================ #


# Build the HTML for a list of tags for a properties block.
def build_tags_html(tag_ids: 'list[str]', tag_type_id: str) -> str:
	# Start with the tag template HTML
	tags_html = ''

	# Get the HTML for each tag, and add it to the tags HTML.
	for tag_id in tag_ids:
		# Get the tag info.
		tag = data[tag_type_id][tag_id]

		# Create the tag HTML.
		tag_html = read_file('./.python/html/tag.html')
		tag_html = tag_html.replace('<!--TEXT-->', tag['text'])
		tag_html = tag_html.replace('<!--COLOR-->', tag['color'])

		# If the tag links to a page, link it and make it clickable.
		linked_page_id = tag['linked-page']
		if linked_page_id != "":
			tag_html = tag_html.replace('<!--URL-->', page_id_to_url(linked_page_id))
			tag_html = tag_html.replace('<!--UNCLICKABLE-->', '')
		# Otherwise, make the link unclickable.
		else:
			tag_html = tag_html.replace('<!--URL-->', '#')
			tag_html = tag_html.replace('<!--UNCLICKABLE-->', ' unclickable')

		# Add the tag HTML to the entire tags HTML.
		tags_html += tag_html
	
	# Finally, return the completed tag HTML snippet.
	return tags_html


# Build the HTML for a list of links for the models property of a post page.
def build_models_list_html(models: 'list[dict]') -> str:
	list_html = ''
	
	# Add each model to a comma-separated list.
	for model in models:
		text = model['text']
		url = model['url']

		# Use a link if the model has a URL, otherwise use plain text.
		link_html = ''
		if url != "":
			link_html = read_file('./.python/html/link.html')
			link_html = link_html.replace('<!--URL-->', url)
			link_html = link_html.replace('<!--TEXT-->', text)
		else:
			link_html = text
		
		# Add commas after each model.
		link_html += ', '
	
		# Combine the link HTML with the overall list HTML.
		list_html += link_html

	# Remove the trailing comma (', ') of the last model.
	list_html = list_html[:-2]

	# Finally, return the 
	return list_html


# Build an HTML block for a post's properties.
def build_post_properties_html(properties: dict) -> str:
	# Start with a post properties HTML template.
	properties_html = read_file('./.python/html/post-properties.html')

	# Set the created property.
	properties_html = properties_html.replace('<!--CREATED-->', properties['created'])

	# Set the tags property.
	tags_html = build_tags_html(properties['tags'], 'tags')
	properties_html = properties_html.replace('<!--TAGS-->', tags_html)

	# Set the manufacturer(s) property.
	tags_html = build_tags_html(properties['manufacturers'], 'manufacturers')
	properties_html = properties_html.replace('<!--MANUFACTURERS-->', tags_html)

	# Set the model(s) property.
	models_html = build_models_list_html(properties['models'])
	properties_html = properties_html.replace('<!--MODELS-->', models_html)

	# Finally, return the properties block HTML.
	return properties_html


# Build an HTML snippet single slideshow slide.
def build_slideshow_slide_html(image_source: str) -> str:
	slide_html = read_file('./.python/html/slideshow-slide.html')
	slide_html = slide_html.replace('<!--IMAGE_SOURCE-->', image_source)
	return slide_html


# Build a slideshow HTML block from a list of images.
def build_slideshow_html(image_sources: 'list[str]') -> str:
	# Start with a slideshow template.
	slideshow_html = read_file('./.python/html/slideshow.html')

	# Get the HTML for all slideshow slides.
	slides_html = ''
	for image_source in image_sources:
		slides_html += build_slideshow_slide_html(image_source)
	
	# Put the combined slides HTML into the slideshow HTML
	slideshow_html = slideshow_html.replace('<!--SLIDES-->', slides_html)

	# Finally, return the slideshow block HTML.
	return slideshow_html


# Combine an array of paragraph lines together, adding <p> tags.
def build_paragraphs_html(paragraph_strings: 'list[str]') -> str:
	# Start with a line break for spacing.
	paragraphs_html = '<br>'

	# Turn each line into a paragrpah and add them.
	for line in paragraph_strings:
		paragraphs_html += f'<p>{line}</p>'
	
	# End with a line break as well.
	paragraphs_html += '<br>'

	# If there's no strings, just return a single line-break instead.
	if len(paragraph_strings) == 0:
		paragraphs_html = '<br>'

	# Finally, return the combined paragraphs block.
	return paragraphs_html


def build_paints_used_html(paints_used: dict) -> str:
	# Start with the paints-used template HTML.
	paints_used_html = read_file('./.python/html/paints-used.html')

	# Combine all paints used into a list.
	paints_list_html = ''
	for paint_used in paints_used:
		# Get the paint IDs.
		brand_id = paint_used['brand']
		line_id = paint_used['line']
		color_id = paint_used['color']

		# Get the paint.
		brand = data['supplies']['paint-brands'][brand_id]
		line = brand['lines'][line_id]
		color = line['colors'][color_id]

		# Get the paint info.
		page_id = color['page']
		text = color['text']
		url = f"{data['website']}paints/{page_id}/"
		icon_source = url + 'icon.png'

		# Get a single paint-used HTML line.
		paint_html = read_file('./.python/html/paint-used.html')

		# Add the info.
		paint_html = paint_html.replace('<!--URL-->', url)
		paint_html = paint_html.replace('<!--ICON_SOURCE-->', icon_source)
		paint_html = paint_html.replace('<!--PAINT-->', text)

		# Finally, add the paint HTML to the paints list HTML.
		paints_list_html += paint_html

	# Add the paints list to the paints-used.
	paints_used_html = paints_used_html.replace('<!--PAINTS-->', paints_list_html)

	# Finally, return the completed paints-used HTML block.
	return paints_used_html


# ============================================================================ #
#                              PAGE HTML BUILDING                              #
# ============================================================================ #


# Build post-type page's article HTML.
def build_post_article_html(page_id) -> str:
	page = data['pages'][page_id]

	# Build each block of the post's article.
	properties_html = build_post_properties_html(page['properties'])
	slideshow_html = build_slideshow_html(page['images'])
	paragraphs_html = build_paragraphs_html(page['paragraphs'])
	paints_used_html = build_paints_used_html(page['paints-used'])

	article_html = properties_html + slideshow_html + paragraphs_html + paints_used_html
	return article_html

# Build the article content HTML, based on the page's type.
def build_article_html(page_id) -> str:
	article_html = ''

	# Get the article HTML based on the page's type.
	page_type_id = data['pages'][page_id]['type']

	if page_type_id == 'gallery':
		pass # build_gallery_article_html(page_id)
	elif page_type_id == 'post':
		article_html = build_post_article_html(page_id)

	# Finally, return the article content HTML.
	return article_html


# Build the page's entire HTML.
def build_page_html(page_id) -> str:
	page = data['pages'][page_id]
	page_type_id = page['type']

	# Get the template HTML and set the title.
	page_html = read_file('./.python/html/template.html')
	page_html = page_html.replace('<!--TITLE-->', page['title'])

	# Set to normal or full-width based on the page type.
	if page_type_id == 'gallery':
		page_html = page_html.replace('<!--FULL_WIDTH-->', ' full-width')
	else:
		page_html = page_html.replace('<!--FULL_WIDTH-->', '')

	# Get the article inner HTML based on the page's type.
	article_html = ''

	if page_type_id == 'gallery':
		pass #build_gallery_page_html(page_id)
	else:
		article_html = build_article_html(page_id)
	
	# Add the article HTML to the page HTML.
	page_html = page_html.replace('<!--ARTICLE-->', article_html)
	
	# Finally, return the page's completed HTML.
	return page_html


# ============================================================================ #
#                             PAGE FILE GENERATION                             #
# ============================================================================ #


# Build a page's HTML, format it, then write it to the proper filepath.
def make_page(page_id: str) -> None:
	page_html = build_page_html(page_id)
	page_html = pretty_html(page_html)
	
	# Write the page to different locations, pased on which folder it belongs to.
	page_type = data['pages'][page_id]['type']

	# Sub-folder page types.
	if page_type == 'post':
		write_file(f'./post/{page_id}/index.html', page_html)

	elif page_type == 'paint':
		write_file(f'./paints/{page_id}/index.html', page_html)

	elif page_type == 'supplies':
		write_file(f'./supplies/{page_id}/index.html', page_html)

	# Singleton page types.
	elif page_type == 'gallery':
		write_file(f'./gallery/index.html', page_html)

	elif page_type == 'paints':
		write_file(f'./paints/index.html', page_html)

	elif page_type == 'supplies':
		write_file(f'./supplies/index.html', page_html)

	elif page_type == 'home':
		write_file(f'./index.html', page_html)

	# Default case, make a new folder for it.
	else:
		write_file(f'./{page_id}/index.html', page_html)


# ============================================================================ #
#                                 MAIN METHOD                                  #
# ============================================================================ #


# Go through everything to make all the pages. This is the "main" method.
def main() -> None:
	# for page in data['pages']...
	make_page('june-10-2022')


if __name__ == '__main__':
	main()