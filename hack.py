import operator
from OC import OC
articles = OC.articles.list(50)

titles = dict()

for id, a in articles.items():
  s = a['citation']
  idx = s.find("accessed on ", 0) + 12
  date = s[idx:]

  titles[a['title']] = (a['views'], date)

titles = sorted(titles.items(), key=operator.itemgetter(1), reverse=True)

for t, data in titles:
  print t + ": " + str(data[0]) + "\t " + data[1]
