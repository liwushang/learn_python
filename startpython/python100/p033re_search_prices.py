import re

content = """
xiaoming went shopping on the street
maile1jinhuanggauhuale8yuan;
maile2jinputaohuale13.5yuan;
maile3jinbaicaihuale5.4yuan;
"""
for line in content.split("\n"):
    pattern = r"(\d)jin(.*)huale(\d+(\.\d+)?)yuan"
    match = re.search(pattern, line)
    if match is not None:
        print(match.groups()[:3])
    print(line)


