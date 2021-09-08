import requests
import json
import random

def clear_screen():
	import os
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def get_quote():
	url = "https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en"

	try:
		response = requests.get(url).json()
		return (response["quoteText"], response.get("quoteAuthor", "Anonymous"))
	except:
		with open("quotes.json") as quotes:
			quotes_list = json.loads(quotes.read())["quotes"]

		random_quote = random.choice(quotes_list)
		return (random_quote["text"], random_quote["author"])

def prettified(quote, author):
	width = 50
	words = quote.split()
	lines = []
	line  = []
	length = 0
	for word in words:
		if (length + len(word)) < width:
			line.append(word)
			length += len(word) + 1
		else:
			lines.append(" ".join(line))
			line = [word]
			length = len(word) + 1

	if len(line) > 0:
		lines.append(" ".join(line))

	upper_border = f" ╭─{'─' * width}─╮"

	prettified_quote = [f" │ {line.ljust(width)} │" for line in lines]

	prettified_author = f" │ {('~ ' + author).rjust(width)} │"

	lower_border = f" ╰─{'─' * width}─╯"

	return "\n".join([upper_border, *prettified_quote, prettified_author, lower_border]) + "\n"

if __name__ == "__main__":

	quote, author = get_quote()

	clear_screen()

	print(prettified(quote, author))
