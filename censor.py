#!/usr/bin/python

def censor(text,word):
    text = str(text)
    word = str(word)
    asterix = ""
    text_split = text.split()
    if word in text_split:
	asterix = "*" * len(word)
    for n in text_split:
	if (n==word):		
		text_split[text_split.index(n)] = asterix
    return " ".join(text_split)   

print censor("this is hack wack hack","hack")
