#Die Welt ist von Zombies überrannt, und das einzige,
#was sie mehr tun als Gehirn zu essen, ist über das Essen von Gehirn zu lesen. Ihre Mission ist es, Literatur für die Zombies zu erstellen,
#um sie abzulenken und Ihr Leben zu retten.

#impotieren von requests und choice aus random
import re
from random import choice
import requests


#text = open("gutenberg.txt")
#text_out = open("Zombie.txt","w")
#text.close()

#text_out.close()
url = "gutenberg.txt"
r = open(url, encoding="utf8").read()

text = r



plural_nouns = ['ladies' , 'gentlemen', 'men', 'children', 'boys','girls']
singular_nouns = ['son', 'daughter', 'child', 'wife','woman', 'mrs', 'miss', 'husband', 'man', 'mr', 'sir', 'lady']
plural_nouns_title = [word.title() for word in plural_nouns]
singular_nouns_title = [word.title() for word in singular_nouns]
speaking = ['said', 'replied', 'spoke', 'shouted', 'cried', 'whispered']
zombie_sounds = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']    
for word in plural_nouns:
    text = re.sub(r'\b{0}\b'.format(word), 'zombies',text)
for word in singular_nouns:
    text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
for word in plural_nouns_title:
    text = re.sub(r'\b{0}\b'.format(word), 'zombies',text)
for word in singular_nouns_title:
    text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
for word in speaking:
    text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)
with open('Zombie.txt', 'w', encoding="utf-8") as f:
    f.write(text)