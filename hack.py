import operator
from OC import OC

numArticles = 50
articles = OC.articles.list(numArticles)

titles = dict()

for id, a in articles.items():
  s = a['citation']
  idx = s.find("accessed on ", 0) + len("accessed on ")
  date = s[idx:]

  titles[a['title']] = (a['views'], date)

titles = sorted(titles.items(), key=operator.itemgetter(1), reverse=True) #sort by views

for t, data in titles:
  # data[0] = views, date[1] = date
  print t + ": " + str(data[0]) + "\t " + data[1]
