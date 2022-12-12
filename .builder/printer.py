from colorama import Fore, Back, Style





# Print good message in green.
def print_good(message: str) -> None:
	print(Fore.GREEN + message + Style.RESET_ALL)




# Print warning message in yellow, with a WARNING prefix.
def print_warning(message: str, detail: str = '') -> None:
	styled_detail = Fore.YELLOW + Style.BRIGHT + detail
	print(Fore.YELLOW + Style.BRIGHT + 'WARNING: ' + Style.RESET_ALL + Fore.YELLOW + message + styled_detail + Style.RESET_ALL)




# Print bad message in red.
def print_bad(message: str) -> None:
	print(Fore.RED + message + Style.RESET_ALL)




# Print error message in red, with an ERROR prefix.
def print_error(message: str, detail: str = '') -> None:
	styled_detail = Fore.RED + Style.BRIGHT + detail
	print(Fore.RED + Style.BRIGHT + 'ERROR: ' + Style.RESET_ALL + Fore.RED + message + styled_detail + Style.RESET_ALL)





# Print section-start message in blue.
def print_start(message: str) -> None:
	print(Fore.BLUE + Style.BRIGHT + message + '...' + Style.RESET_ALL)





# Print section-end message in cyan.
def print_end(message: str) -> None:
	print(Fore.CYAN + Style.BRIGHT + '...' + message + Style.RESET_ALL)





# Don't allow running this as the main file. Run main.py instead.
# ======================================================================================= #
if __name__ == '__main__':
	print_error('Run \'main.py\' instead.')