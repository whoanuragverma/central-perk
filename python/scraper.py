from bs4 import BeautifulSoup
import pandas as pd
import os

main = []
titles = []

ep_no = 1
for folders in os.listdir('raw'):
    for files in os.listdir(os.path.join('raw', folders)):
        soup = BeautifulSoup(
            open(os.path.join('raw', folders, files), encoding='cp1252'), "html.parser")
        titles.append(soup.title.text)
        ctr = 0
        for tag in soup.find_all('p'):
            ctr += 1
            print("For episode: {} Number: {} Scanned Lines: {} Total Lines: {}".format(
                soup.title.text, ep_no, ctr, len(soup.find_all('p'))))
            if tag.find('b') is not None and tag.find('b').find('font') is None:
                main.append(tag.text.replace(
                    "\xa0", " ", 10).replace("\n", " ", 10).split(": ", 1))
        ep_no += 1
df1 = pd.DataFrame(titles, columns=['Title'])
df1.to_excel("titles.xlsx", index=False)
df = pd.DataFrame(main, columns=['Charcater', 'Dialouge'])
df.to_excel("dialouges.xlsx", index=False)
