from nltk.text import TextCollection

f = open("emails.txt","r");
cont = f.read()
emails = cont.split('@')
words = [email.replace('\n', ' ').split() for email in emails]
#print words
f.close()

generator = TextCollection(words)
#generator.generate(10)
#generator.generate(25)
generator.generate(80)

