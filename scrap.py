import requests

class Fragment:
    def __init__(self, start, end, text):
        self.start = start
        self.end = end
        self.text = text
    def print(self):
        print(str(self.start) + " " + str(self.end) + " " + str(self.text))

class Offer:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def print(self):
        print("Tytuł: " + str(self.title.text) + " Cena: " + str(self.price.text))


def cutoff(string, stringStart, patternStart, paternEnd):
    stringExamined = string[stringStart:]
    idx1 = stringExamined.find(patternStart) + len(patternStart)
    idx2 = idx1 + stringExamined[idx1:].find(paternEnd) + stringStart
    idx1 = idx1 + stringStart
    return Fragment(idx1, idx2, string[idx1:idx2])

r = requests.get('https://www.olx.pl/nieruchomosci/mieszkania/warszawa/')
with open('website.html', 'w', encoding = "utf-8") as f:
    f.write(r.text)


txt = r.text
start = 0
for i in range(txt.count('alt=')):
    title = cutoff(txt, start, 'alt="', '"')
    price = cutoff(txt, title.end, '<p class="price">\n                            <strong>', '</strong>')
    offer = Offer(title, price)
    offer.print()
    start = price.end

