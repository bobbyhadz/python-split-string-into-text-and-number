# Split a string into text and number in Python

import re

my_str = 'hello123'

my_list = re.split(r'(\d+)', my_str)

# 👇️ ['hello', '123', '']
print(my_list)