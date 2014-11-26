from nltk.text import TextCollection

f = open("shakes.txt","r");
cont = f.read()
emails = cont.split('by William Shakespeare')
words = [email.replace('\n', ' ').split() for email in emails]
f.close()

generator = TextCollection(words)
#generator.generate(10)
#generator.generate(25)
generator.generate(80)

