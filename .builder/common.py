import os
from xml.dom import minidom
from data import data





# The following are assumed to exist and required for this to work:
# data['website']
# data['pages'][page_id]['type']
# data['pages'][page_id]['type'] == 'home' or 'gallery' or 'post' or 'my-paints' or 'paint' or 'my-supplies' or 'supplies'





UNFINISHED = "This website is still under construction, so this content is missing or unfinished."





# Read a file and return its content.
# ======================================================================================= #
def read_file(filepath: str) -> str:
	# Ensure the filepath exists before reading from it.
	if not os.path.exists(filepath):
		print(f'ERROR: Trying to read from nonexistant file: {filepath}')
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

	# .../post/index.html
	if page_type_id == 'post':
		page_subpath = f'post/{page_id}/'
	# .../paints/index.html
	elif page_type_id == 'my-paints':
		page_subpath = 'paints/'
	# .../paints/{page_id}/index.html
	elif page_type_id == 'paint':
		page_subpath = f'paints/{page_id}/'
	# .../supplies/index.html
	elif page_type_id == 'my-supplies':
		page_subpath = 'supplies/'
	# .../supplies/{page_id}/index.html
	elif page_type_id == 'supplies':
		page_subpath = f'supplies/{page_id}/'
	# .../gallery/index.html
	elif page_type_id == 'gallery':
		page_subpath = 'gallery/'
	# .../index.html
	elif page_type_id == 'home':
		page_subpath = ''
	else:
		print(f'ERROR: Page type ID \'{page_type_id}\' not implemented.')
	
	return page_subpath





# Get the folderpath for a page's `index.html`.
# Example: ./post/10-06-2022/
# Example (absolute): /home/user/dev/necrominis-github.io/post/10-06-2022/
# Ends in a `/`.
# ======================================================================================= #
def _page_id_to_folderpath(page_id: str, absolute: bool = False) -> str:
	page_subpath = page_id_to_subpath(page_id)

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

	filepath = f'{folderpath}index.html'
	return filepath





# Get the website URL for a page.
# Example: https://necrominis.github.io/post/10-06-2022/
# Ends in a `/`.
# ======================================================================================= #
def page_id_to_url(page_id: str) -> str:
	website = data['website']
	page_subpath = page_id_to_subpath(page_id)

	url = f'{website}{page_subpath}'

	return url





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print('ERROR: Run \'main.py\' instead.')