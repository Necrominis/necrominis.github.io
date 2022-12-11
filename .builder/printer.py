from colorama import Fore, Back, Style





def print_good(message: str) -> None:
	print(Fore.GREEN + message + Style.RESET_ALL)




def print_warning(message: str) -> None:
	print(Fore.YELLOW + Style.BRIGHT + 'WARNING: ' + Style.RESET_ALL + Fore.YELLOW + message + Style.RESET_ALL)




def print_bad(message: str) -> None:
	print(Fore.RED + message + Style.RESET_ALL)




def print_error(message: str) -> None:
	print(Fore.RED + Style.BRIGHT + 'ERROR: ' + Style.RESET_ALL + Fore.RED + message + Style.RESET_ALL)





def print_start(message: str) -> None:
	print(Fore.BLUE + Style.BRIGHT + message + '...' + Style.RESET_ALL)





def print_end(message: str) -> None:
	print(Fore.CYAN + Style.BRIGHT + '...' + message + Style.RESET_ALL)