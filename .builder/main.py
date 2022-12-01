import os
import sys
from data import data
from common import *
from page_builder import build_page_html





# The following are assumed to exist and required for this to work:
# data['pages'][page_id]





# Build the HTML for a page, then create its file(s).
# ======================================================================================= #
def make_page(page_id: str) -> None:
	page_html = build_page_html(page_id)
	page_html = pretty_html(page_html)
	
	page_filepath = page_id_to_filepath(page_id, True)

	write_file(page_filepath, page_html)





# Main method. Loop through every page and make it.
# ======================================================================================= #
def main(clean: bool = False, verbose: bool = False, silent: bool = False) -> None:
	print('CREATING PAGES')

	page_ids = data['pages'].keys()

	# If specified, delete all the old pages first.
	if clean:
		pass # TODO

	# Make all the pages.
	for page_id in page_ids:
		# If specified, print out when each page is made. 
		if not silent:
			print(f'./{page_id_to_subpath(page_id)}')
			if verbose:
				print(f'    {page_id_to_url(page_id)}')
				print(f'    {page_id_to_filepath(page_id, True)}')

		# Build and create the page file(s).
		make_page(page_id)
	
	print('DONE')





# If this is the main file, process arguments and run the main method.
# ======================================================================================= #
if __name__ == '__main__':
	# Arguments.
	clean = False
	verbose = False
	silent = False
	directory = False

	# Check for arguments.
	args = sys.argv[1:]
	for arg in args:
		# Check if the clean argument was specified.
		if arg == '-c' or arg == '-clean' or arg == '--clean':
			args.remove(arg)
			clean = True
		# Check if the verbose argument was specified.
		elif arg == '-v' or arg == '-verbose' or arg == '--verbose':
			args.remove(arg)
			verbose = True
		# Check if the silent argument was specified.
		elif arg == '-s' or arg == '-silent' or arg == '--silent':
			args.remove(arg)
			silent = True
		# Check if the directory argument was specified.
		elif arg == '-d' or arg == '-dir' or arg == '-directory' or arg == '--dir' or arg == '--directory':
			args.remove(arg)
			directory = True
	
	# Ensure the cwd is good, otherwise bail.
	if directory:
		if len(args) > 0:
			if os.path.exists(args[0]) and os.path.exists(args[0] + '/.builder/main.py'):
				# If directory is specified and a valid path is given, proceed.
				os.chdir(args[0])
			else:
				# If directory is specified and an invalid path is given, bail.
				print("ERROR: Bailing because the directory may not be correct: " + args[0])
				exit()
		else:
			# If directory is specified, and no path is given, bail.
			print("ERROR: Bailing because the directory flag was specified, but no path was given.")
			exit()
	else:
		if os.path.exists(os.getcwd()) and os.getcwd().join('/.builder/main.py'):
			# If directory wasn't specified, and the current path is valid, proceed.
			pass
		else:
			# If directory wasn't specified, and the current path is invalid, bail.
			print("ERROR: Bailing because the directory may not be correct: " + os.getcwd())
			exit()

	# After processing arguments, start the main method.
	main(clean, verbose, silent)