import re
from common import *

string = """You can go to the *supplies* page [here](2022-06-10) or [HERE](gallery)."""

link_pattern = re.compile(r'\[([^][]+)?\]\((.*?)\)', re.U)

for match in link_pattern.finditer(string):
	text, page_id = match.groups()
	string = string.replace(f'[{text}]({page_id})', f'<a href="{page_id_to_url(page_id)}">{text}</a>', 1)
	print(string)

