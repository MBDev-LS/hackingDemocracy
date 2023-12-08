
# def fetch_info_if_missing_wrapper(*args, **kwargs):
	
# 	print(args, kwargs)

# fetch_info_if_missing_wrapper('hello')

import re

results = re.findall(r'^(https?:\/\/([a-zA-Z0-9]|\.)+)', 'https://game.com')

print(results)