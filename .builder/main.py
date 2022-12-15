import os
import sys
from data import data
from common import *
from printer import *
from page_builder import build_page_html





# data['website'] = data['website-local']





# The following are assumed to exist and required for this to work:
# data['website']
# data['pages'][page_id]





# Build the HTML for a page, then create its file(s).
# ======================================================================================= #
def make_page(page_id: str) -> None:
	page_html = build_page_html(page_id)
	page_html = linear_html(page_html)
	
	page_filepath = page_id_to_filepath(page_id, True)

	write_file(page_filepath, page_html)





# Loop through every page and make it.
# ======================================================================================= #
def make_pages(verbose: bool = False, silent: bool = False) -> None:
	print_start('CREATING PAGES')

	page_ids = data['pages'].keys()

	# Make all the pages.
	for page_id in page_ids:
		# If specified, print out when each page is made. 
		if not silent:
			print_normal(f'  ./{page_id_to_subpath(page_id)}')
			if verbose:
				print_normal(f'      {page_id_to_url(page_id)}')
				print_normal(f'      {page_id_to_filepath(page_id, True)}')

		# Build and create the page file(s).
		make_page(page_id)
	
	# Print out finished text.
	print_end('DONE CREATING PAGES')





# Main method.
# ======================================================================================= #
def main(clean: bool = False, verbose: bool = False, silent: bool = False) -> None:
	init_printer()

	# Print out starting text.
	if is_web_url(data['website']):
		print_good('GENERATING PRODUCTION WEBSITE:')
	else:
		print_warning('GENERATING LOCAL DEVELOPMENT WEBSITE:')
		
	print_normal()

	# If specified, delete all the old pages first.
	if clean:
		pass # TODO

	# Generate all the page files.
	make_pages(verbose, silent)

	deinit_printer()





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
				print_fault("Bailing because the directory may not be correct: ", args[0])
				exit()
		else:
			# If directory is specified, and no path is given, bail.
			print_fault("Bailing because the directory flag was specified, but no path was given.")
			exit()
	else:
		if os.path.exists(os.getcwd()) and os.getcwd().join('/.builder/main.py'):
			# If directory wasn't specified, and the current path is valid, proceed.
			pass
		else:
			# If directory wasn't specified, and the current path is invalid, bail.
			print_fault("Bailing because the directory may not be correct: ", f"{os.getcwd()}")
			exit()

	# After processing arguments, start the main method.
	main(clean, verbose, silent)

	# Print the amout of memory used by this process.
	import os, psutil
	process = psutil.Process(os.getpid())
	bytes = process.memory_info().rss
	power = 2**10 # 1024.
	labels = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
	memory_used = bytes
	factor = 0
	while memory_used > power:
		memory_used /= power
		factor += 1
	if factor < 3:
		print_good(f"Process completed and used {round(memory_used, 2)} {labels[factor]} of RAM.")
	else:
		print_bad(f"Process completed and used {round(memory_used, 2)} {labels[factor]} of RAM.")