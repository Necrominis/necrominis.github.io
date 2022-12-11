from data import data
from common import *
from printer import *
from snippet_builder import *





# The following are assumed to exist and required for this to work:
# data["website"]
# data["image-paths"] == 'logos' or 'covers' or 'icons' or 'paint-photos' or 'paint-icons' or 'supplies-photos' or 'supplies-icons' or 'post-photos'
# data['pages'][page_id]['title']
# data['pages'][page_id]['type']
# data['pages'][page_id]['type'] == 'home' or 'gallery' or 'post' or 'my-paints' or 'paint' or 'my-supplies' or 'supplies'



def parse_filepaths(html: str) -> str:
	website = data["website"]
	image_paths = data['image-paths']

	parsed_html = html

	# Add website URL to any relative filepaths.
	parsed_html = parsed_html.replace('<!--WEBSITE-->', website)

	# Add image filepaths.
	parsed_html = parsed_html.replace('<!--WEBSITE-LOGO-->', website + image_paths['logos'])
	parsed_html = parsed_html.replace('<!--WEBSITE-COVER-->', website + image_paths['covers'])
	parsed_html = parsed_html.replace('<!--WEBSITE-ICON-->', website + image_paths['icons'])
	parsed_html = parsed_html.replace('<!--WEBSITE-PAINT-PHOTO-->', website + image_paths['paint-photos'])
	parsed_html = parsed_html.replace('<!--WEBSITE-PAINT-ICON-->', website + image_paths['paint-icons'])
	parsed_html = parsed_html.replace('<!--WEBSITE-SUPPLIES-PHOTO-->', website + image_paths['supplies-photos'])
	parsed_html = parsed_html.replace('<!--WEBSITE-SUPPLIES-ICON-->', website + image_paths['supplies-icons'])
	parsed_html = parsed_html.replace('<!--WEBSITE-POST-PHOTO-->', website + image_paths['post-photos'])

	return parsed_html





# Get the article section HTML for a page.
# ======================================================================================= #
def build_article_html(page_id: str) -> str:
	page = data['pages'][page_id]
	page_type_id = page['type']
	page_title = page['title']

	# Get the starter article HTML and set the title.
	article_html = read_html_file('article.html')
	article_html = article_html.replace('<!--TITLE-->', page_title)
	
	# Set article div to full-width or not, based on page type.
	if page_type_id in ['gallery', 'paints-home', 'supplies-home']:
		article_html = article_html.replace('<!--FULL-WIDTH-->', 'full-width')
	elif page_type_id in ['post']:
		article_html = article_html.replace('<!--FULL-WIDTH-->', 'double-width')
	article_html = article_html.replace('<!--FULL-WIDTH-->', '')

	# Build HTML based on page type (post, gallery, etc.).
	article_content_html = ''

	if page_type_id == 'post':
		article_content_html = build_post_article_content_html(page_id)
	elif page_type_id == 'my-paints':
		article_content_html = build_paints_article_content_html(page_id)
	elif page_type_id == 'paint':
		article_content_html = build_paint_article_content_html(page_id)
	elif page_type_id == 'my-supplies':
			article_content_html = build_supplies_article_content_html(page_id)
	elif page_type_id == 'supplies':
			article_content_html = build_supply_article_content_html(page_id)
	elif page_type_id == 'gallery':
		article_content_html = build_gallery_article_content_html(page_id)
	elif page_type_id == 'home':
		article_content_html = build_home_article_content_html(page_id)
	else:
		print_error(f'Page type ID \'{page_type_id}\' not implemented.')

	article_html = article_html.replace('<!--CONTENT-->', article_content_html)

	return article_html





# Get the entire HTML file text for a page.
# ======================================================================================= #
def build_page_html(page_id: str) -> str:
	page = data['pages'][page_id]
	page_title = page['title']
	website = data["website"]
	image_paths = data['image-paths']
	
	# Get the starter template HTML and set the title.
	page_html = read_html_file('template.html')
	page_html = page_html.replace('<!--TITLE-->', page_title)

	# Get and add the article inner HTML based on the page type.
	article_html = build_article_html(page_id)
	page_html = page_html.replace('<!--ARTICLE-->', article_html)

	# Replace filepath comments with actual filepaths.
	page_html = parse_filepaths(page_html)

	# Finally, return the page's completed HTML.
	return page_html





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')