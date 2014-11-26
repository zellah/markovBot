from nltk.text import TextCollection

f = open("cuil.txt","r");
cont = f.read()
emails = cont.split('Cuils')
words = [email.replace('\n', ' ').split() for email in emails]
f.close()

generator = TextCollection(words)
generator.generate(80)

