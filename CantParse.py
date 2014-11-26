from nltk.text import TextCollection

f = open("cant.txt","r");
cont = f.read()
emails = cont.split('GROUP')
words = [email.replace('\n', ' ').split() for email in emails]
f.close()

generator = TextCollection(words)
generator.generate(150)

