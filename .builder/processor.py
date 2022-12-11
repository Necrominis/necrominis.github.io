import re as regex
from data import data
from common import *
from printer import *





# The following are assumed to exist and required for this to work:
# data['pages'][page_id]





# Process the first-paragraph using markdown-ish syntax.
# Example: :-paragraph
# Example: -:paragraph
# ======================================================================================= #
def _process_non_breaking_first_paragraph(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every non-breaking paragraph syntax and replace it with link HTML.
	first_paragraph_pattern = regex.compile(r'^-:(.*$)', regex.U)
	for match in first_paragraph_pattern.finditer(paragraph):
		whole_paragraph = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'-:{whole_paragraph}', f'<mark class="non-breaking-paragraph"><mark class="first-paragraph">{whole_paragraph}</mark></mark>', 1)
		return processed_paragraph

	# Find every non-breaking paragraph syntax and replace it with link HTML.
	first_paragraph_pattern = regex.compile(r'^:-(.*$)', regex.U)
	for match in first_paragraph_pattern.finditer(paragraph):
		whole_paragraph = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f':-{whole_paragraph}', f'<mark class="non-breaking-paragraph"><mark class="first-paragraph">{whole_paragraph}</mark></mark>', 1)
		return processed_paragraph

	return processed_paragraph





# Process the non-breaking paragraph using markdown-ish syntax.
# Must be done after non-breaking first-paragraph processing.
# Example: -paragraph
# ======================================================================================= #
def _process_non_breaking_paragraph(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every non-breaking paragraph syntax and replace it with link HTML.
	first_paragraph_pattern = regex.compile(r'^-(.*$)', regex.U)
	for match in first_paragraph_pattern.finditer(paragraph):
		whole_paragraph = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'-{whole_paragraph}', f'<mark class="non-breaking-paragraph">{whole_paragraph}</mark>', 1)
		break

	return processed_paragraph





# Process the first-paragraph using markdown-ish syntax.
# Must be done after non-breaking first-paragraph processing.
# Example: :paragraph
# ======================================================================================= #
def _process_first_paragraph(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find the first-paragraph syntax and replace it with HTML.
	first_paragraph_pattern = regex.compile(r'^:(.*$)', regex.U)
	for match in first_paragraph_pattern.finditer(paragraph):
		whole_paragraph = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f':{whole_paragraph}', f'<mark class="first-paragraph">{whole_paragraph}</mark>', 1)
		break

	return processed_paragraph





# Process the links using markdown syntax.
# Must be done after bold processing.
# Example: *text*
# Example: _text_
# ======================================================================================= #
def _process_italics(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every *italic* syntax and replace it with HTML.
	italic_pattern = regex.compile(r'\*(\S{1}|\S{1}.*?\S{1})\*', regex.U)
	for match in italic_pattern.finditer(paragraph):
		text = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'*{text}*', f'<i>{text}</i>', 1)

	# Find every _italic_ syntax and replace it with HTML.
	italic_pattern_2 = regex.compile(r'\_(\S{1}|\S{1}.*?\S{1})\_', regex.U)
	for match in italic_pattern_2.finditer(paragraph):
		text = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'_{text}_', f'<i>{text}</i>', 1)

	return processed_paragraph





# Process the links using markdown syntax.
# Example: **text**
# ======================================================================================= #
def _process_bolds(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every bold syntax and replace it with HTML.
	bold_pattern = regex.compile(r'\*\*(\S{1}|\S{1}.*?\S{1})\*\*', regex.U)
	for match in bold_pattern.finditer(paragraph):
		text = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'**{text}**', f'<b>{text}</b>', 1)

	return processed_paragraph





# Process the mini-names and highlights using markdown-ish syntax.
# Example: [[text]]
# ======================================================================================= #
def _process_highlights(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every highlight syntax and replace it with HTML.
	highlight_pattern = regex.compile(r'\[\[(\S{1}|\S{1}.*?\S{1})\]\]', regex.U)
	for match in highlight_pattern.finditer(paragraph):
		text = match.groups()[0]
		processed_paragraph = processed_paragraph.replace(f'[[{text}]]', f'<mark class="mini-name">{text}</mark>', 1)

	return processed_paragraph





# Process the tooltips using markdown syntax.
# Example: [text]T(tip)
# ======================================================================================= #
def _process_tooltips(paragraph: str) -> str:
	processed_paragraph = paragraph

	# Find every tooltip syntax and replace it with HTML.
	tooltip_pattern = regex.compile(r'\[([^][]+)?\]T\((.*?)\)', regex.U)
	for match in tooltip_pattern.finditer(paragraph):
		text, tip = match.groups()
		processed_paragraph = processed_paragraph.replace(f'[{text}]T({tip})', f'<mark class="tooltip">{text}<span class="tip">{tip}</span></mark>', 1)

	return processed_paragraph





# Process the links using markdown syntax.
# Must be done after highlight processing.
# Example: [text](url)
# Example: [text](page_id)
# ======================================================================================= #
def _process_links(paragraph: str) -> str:
	page_ids = data['pages'].keys()

	processed_paragraph = paragraph

	# Find every link syntax and replace it with HTML.
	link_pattern = regex.compile(r'\[([^][]+)?\]\((.*?)\)', regex.U)
	for match in link_pattern.finditer(paragraph):
		link_text, link_url = match.groups()
		# Link to a page ID, if it's not a normal URL.
		new_url = link_url
		if not 'https://' in link_url:
			# Check page ID link.
			if link_url in page_ids:
				new_url = page_id_to_url(link_url)
			else:
				new_url = f"{data['website']}404/{link_url}"
				print_error(f'Paragraph link is not a URL and not a page ID: {link_url}')
			
		processed_paragraph = processed_paragraph.replace(f'[{link_text}]({link_url})', f'<a href="{new_url}">{link_text}</a>', 1)

	return processed_paragraph





# Post-process the markdown syntax in paragraphs.
# ======================================================================================= #
def process_paragraph(paragraph: str) -> str:
	processed_paragraph = paragraph

	processed_paragraph = _process_non_breaking_first_paragraph(processed_paragraph)
	processed_paragraph = _process_non_breaking_paragraph(processed_paragraph)
	processed_paragraph = _process_first_paragraph(processed_paragraph)

	processed_paragraph = _process_bolds(processed_paragraph)
	processed_paragraph = _process_italics(processed_paragraph)

	processed_paragraph = _process_highlights(processed_paragraph)

	processed_paragraph = _process_links(processed_paragraph)
	processed_paragraph = _process_tooltips(processed_paragraph)
	
	return processed_paragraph