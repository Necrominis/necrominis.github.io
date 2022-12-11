import re as regex
from data import data
from common import *
from printer import *





# The following are assumed to exist and required for this to work:
# data['pages'][page_id]





# Process the links using markdown syntax:
# Example: [text]T(tip)
# ======================================================================================= #
def _process_tooltips(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every tooltip syntax and replace it with link HTML.
	tooltip = regex.compile(r'\[([^][]+)?\]T\((.*?)\)', regex.U)
	for match in tooltip.finditer(paragraph):
		text, tip = match.groups()
		processed_paragraph = processed_paragraph.replace(f'[{text}]T({tip})', f'<mark class="tooltip">{text}<span class="tip">{tip}</span></mark>', 1)

	return processed_paragraph





# Process the links using markdown syntax:
# Example: [text](url)
# Example: [text](page_id)
# ======================================================================================= #
def _process_links(paragraph: str) -> str:
	page_ids = data['pages'].keys()

	processed_paragraph = paragraph

	# Find every link syntax and replace it with link HTML.
	link_pattern = regex.compile(r'\[([^][]+)?\]\((.*?)\)', regex.U)
	for match in link_pattern.finditer(paragraph):
		link_text, link_url = match.groups()
		# Link to a page ID, if it's not a normal URL.
		new_url = link_url
		if link_url in page_ids:
			new_url = page_id_to_url(link_url)
		elif not 'https://' in link_url:
			print_error(f'Paragraph link is not a URL and not a page ID: {link_url}')
			
		processed_paragraph = processed_paragraph.replace(f'[{link_text}]({link_url})', f'<a href="{new_url}">{link_text}</a>', 1)

	return processed_paragraph





# Post-process the markdown syntax in paragraphs.
# ======================================================================================= #
def process_paragraph(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Process links.
	processed_paragraph = _process_links(processed_paragraph)

	# Process tooltips.
	processed_paragraph = _process_tooltips(processed_paragraph)
	
	return processed_paragraph