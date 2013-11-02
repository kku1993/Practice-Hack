import operator
from OC import OC
articles = OC.articles.list(50)

titles = dict()

for id, a in articles.items():
  titles[a['title']] = a['views']

print sorted(titles.items(), key=operator.itemgetter(1), reverse=True)
