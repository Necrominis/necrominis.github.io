import os
from xml.dom import minidom
from data import data
from printer import *





# The following are assumed to exist and required for this to work:
# data['website']
# data['pages'][page_id]['index']
# data['pages'][page_id]['type']
# data['pages'][page_id]['type'] == 'home' or 'gallery' or 'post' or 'my-paints' or 'paint' or 'my-supplies' or 'supplies' or '404'
# data['paints'] is sorted
# data['paints'][paint_id]['index']
# data['paints'][paint_id]['category']
# data['supplies'] is sorted
# data['supplies'][supplies_id]['index']
# data['supplies'][supplies_id]['category']





UNFINISHED = "<p>This website is still under construction, so this content is missing or unfinished.<p>"
separator = ' - '





# Read a file and return its content.
# ======================================================================================= #
def read_file(filepath: str) -> str:
	# Ensure the filepath exists before reading from it.
	if not os.path.exists(filepath):
		print_error(f'Trying to read from nonexistant file: {filepath}')
		return ''

	# Read the file and return its content.
	file = open(filepath, 'r')
	content = file.read()
	file.close()
	return content





# Read an HTML file and return its content.
# ======================================================================================= #
def read_html_file(filename: str) -> str:
	# Add the HTML extension to the filename if it doesn't have it already.
	filepath = f'./.builder/html/{filename}'
	if not filepath.endswith('.html'):
		filepath += '.html'
	
	return read_file(filepath)





# Write to a file, creating it if it doesn't already exist.
# ======================================================================================= #
def write_file(filepath: str, content: str, print_out: bool = False) -> None:
	# Create the folders if they don't exist yet.
	path_parts = filepath.split('/')
	directory = ''
	for i in range(len(path_parts) - 1):
		directory += path_parts[i] + '/'
	if not os.path.exists(directory):
		os.makedirs(directory)

	# Create/write the file.
	file = open(filepath, 'w')
	file.write(content)
	file.close()

	if print_out:
		print(f'Wrote to file: {filepath}')





# Return HTML all on one line.
# ======================================================================================= #
def linear_html(html: str) -> str:
	linear = html.replace('\n', '').replace('\t', '')
	return linear





# Return HTML with every node in individual lines, but with no indentation.
# ======================================================================================= #
def flat_html(html: str) -> str:
	linear = linear_html(html)
	flat = linear.replace('><', '>\n<')
	flat = flat.replace('-->\n<', '--><').replace('>\n<!--', '><!--')
	return flat





# Return properly styled and indented HTML.
# ======================================================================================= #
def pretty_html(html: str) -> str:
	#parser = minidom.parseString(html)
	#pretty = '\n'.join(parser.toprettyxml().splitlines()[1:])
	pretty = flat_html(html)
	return pretty





# Get the page subpath.
# Example: post/10-06-2022/
# Ends in a `/`, unless it's the home page.
# ======================================================================================= #
def page_id_to_subpath(page_id: str) -> str:
	page_type_id = data['pages'][page_id]['type']

	# Get the page subpath.
	page_subpath = ''

	# ./post/index.html
	if page_type_id == 'post':
		page_subpath = f'post/{page_id}/'
	# ./paints/index.html
	elif page_type_id == 'my-paints':
		page_subpath = 'paints/'
	# ./paints/{page_id}/index.html
	elif page_type_id == 'paint':
		page_subpath = f'paints/{page_id}/'
	# ./supplies/index.html
	elif page_type_id == 'my-supplies':
		page_subpath = 'supplies/'
	# ./supplies/{page_id}/index.html
	elif page_type_id == 'supplies':
		page_subpath = f'supplies/{page_id}/'
	# ./gallery/index.html
	elif page_type_id == 'gallery':
		page_subpath = 'gallery/'
	# ./index.html
	elif page_type_id == 'home':
		page_subpath = ''
	# ./404.html
	elif page_type_id == '404':
		page_subpath = ''
	else:
		print_error(f'Page type ID \'{page_type_id}\' not implemented.')
	
	return page_subpath





# Get the folderpath for a page's `index.html`.
# Example: ./post/10-06-2022/
# Example (absolute): /home/user/dev/necrominis-github.io/post/10-06-2022/
# Ends in a `/`.
# ======================================================================================= #
def _page_id_to_folderpath(page_id: str, absolute: bool = False) -> str:
	page_subpath = page_id_to_subpath(page_id)

	# Get the page's folderpath.
	folderpath = f'./{page_subpath}'
	if absolute:
		folderpath = f'{os.getcwd()}/{page_subpath}'

	return folderpath





# Get the filepath to a page's `index.html` file.
# Example: ./post/10-06-2022/index.html
# Example (absolute): /home/user/dev/necrominis-github.io/post/10-06-2022/index.html
# ======================================================================================= #
def page_id_to_filepath(page_id: str, absolute: bool = False) -> str:
	folderpath = _page_id_to_folderpath(page_id, absolute)

	# Get the page's filepath.
	filepath = f'{folderpath}index.html'

	# Handle special 404 page.
	if data['pages'][page_id]['type'] == '404':
		filepath = f'{folderpath}404.html'

	return filepath





# Get the website URL for a page.
# Example: https://necrominis.github.io/post/10-06-2022/
# Ends in a `/`.
# ======================================================================================= #
def page_id_to_url(page_id: str) -> str:
	website = data['website']
	page_subpath = page_id_to_subpath(page_id)

	# Get the page's URL.
	url = f'{website}{page_subpath}'

	# Handle special 404 page.
	if data['pages'][page_id]['type'] == '404':
		url = f'{website}{page_subpath}404.html'

	return url





# Take a list of IDs and return the list sorted.
# ======================================================================================= #
def _sort_list(ids: '[str]', data_dictionary: dict) -> '[str]':
	all_ids = data_dictionary.keys()

	# Check for ID in ids that's not in all_ids.
	for id in ids:
		if not id in all_ids:
			print_warning('ID not found in list of IDs while sorting: ', id)

	# Create a list of tuples with index and ID.
	sorted_tuples = []
	for id in all_ids:
		# Skip empty items and items not in the original list.
		if id == '' or not id in ids:
			continue

		index = data_dictionary[id]['index']
		sorted_tuples.append((index, id))
	
	# Sort the list of tuples.
	sorted_tuples.sort()

	# Replace the sorted lists's tuples with just the IDs.
	sorted_ids = []
	for _index, id in sorted_tuples:
		sorted_ids.append(id)

	return sorted_ids





# Take a list of IDs and return the list sorted, with separators between the categories.
# ======================================================================================= #
def _sort_by_category(ids: '[str]', data_dictionary: dict, separators: bool = True) -> '[str]':
	sorted_ids = _sort_list(ids, data_dictionary)

	# Return without separators if desired, or if list is too short to need separators.
	if not separators or len(ids) < 2:
		return sorted_ids

	# Get a list of the paints.
	items = []
	for item_id in sorted_ids:
		items.append(data_dictionary[item_id])

	# Add separators between categories.
	organized_ids = [ids[0]]
	previous_item = data_dictionary[ids[0]]
	for i in len(items) - 1:
		item = items[i+1]
		item_id = ids[i+1]

		if item['category'] != previous_item['category']:
			organized_ids.append('')

		previous_item = item
		organized_ids.append(item_id)

	return organized_ids





# Take a list of paint IDs and return the list sorted.
# ======================================================================================= #
def sort_paints(paint_ids: '[str]', separators: bool = False) -> '[str]':
	sorted_paint_ids = _sort_by_category(paint_ids, data['paints'], separators)
	return sorted_paint_ids





# Take a list of supplies IDs and return the list sorted.
# ======================================================================================= #
def sort_supplies(supplies_ids: '[str]', separators: bool = False) -> '[str]':
	sorted_supplies_ids = _sort_by_category(supplies_ids, data['supplies'], separators)
	return sorted_supplies_ids





# Take a list of page IDs and return the list sorted.
# ======================================================================================= #
def sort_pages(page_ids: '[str]', descending: bool = False) -> '[str]':
	sorted_page_ids = _sort_list(page_ids, data['pages'])

	if descending:
		sorted_page_ids = list(reversed(sorted_page_ids))

	return sorted_page_ids





# Take a list of page IDs and return the list sorted.
# ======================================================================================= #
def is_web_url(url: str) -> bool:
	for check in ['http', 'www.', '.com', '.net', '.io', 'org']:
		if check in url:
			return True
	return False





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')