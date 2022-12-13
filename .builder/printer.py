from colorama import Fore, Back, Style





# Initialize the printer.
# Call this before any print statements.
def init_printer() -> None:
	print(Fore.RED, end='')





# Deinitialize the printer.
# Call this before closing the program.
def deinit_printer() -> None:
	print(Style.RESET_ALL, end='')




	
# Deinitialize the printer.
# Call this instead of _reset()
def _reset() -> None:
	print(Style.RESET_ALL, end='')
	init_printer()





# Print normal message in white.
def print_normal(message: str = '') -> None:
	print(Fore.WHITE + str(message))
	_reset()





# Print good message in green.
def print_good(message: str = '') -> None:
	print(Fore.GREEN + str(message))
	_reset()




# Print warning message in yellow, with a WARNING prefix.
def print_warning(message: str, detail: str = '') -> None:
	styled_detail = Fore.YELLOW + Style.BRIGHT + detail
	print(Fore.YELLOW + Style.BRIGHT + 'WARNING: ', end='')
	_reset()
	print(Fore.YELLOW + str(message) + styled_detail)
	_reset()




# Print bad message in red.
def print_bad(message: str = '') -> None:
	print(Fore.RED + str(message))
	_reset()




# Print error message in red, with an ERROR prefix.
def print_error(message: str, detail: str = '') -> None:
	styled_detail = Fore.RED + Style.BRIGHT + detail
	print(Fore.RED + Style.BRIGHT + 'ERROR: ', end='')
	_reset()
	print(Fore.RED + str(message) + styled_detail)
	_reset()




# Print fault message in red, with an FAULT prefix.
def print_fault(message: str, detail: str = '') -> None:
	styled_detail = Fore.RED + Style.BRIGHT + detail
	print(Fore.RED + Style.BRIGHT + '/!\\ FAULT: ', end='')
	_reset()
	print(Fore.RED + str(message) + styled_detail)
	_reset()





# Print section-start message in blue.
def print_start(message: str = '') -> None:
	print(Fore.BLUE + Style.BRIGHT + str(message) + '...')
	_reset()





# Print section-end message in cyan.
def print_end(message: str = '') -> None:
	print(Fore.CYAN + Style.BRIGHT + '...' + str(message))
	_reset()





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')