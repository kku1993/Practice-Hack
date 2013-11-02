import operator
import sys
from OC import OC

# sortByView - get a list of articles sorted in descending order by view
# REQUIRES: numArticles > 0
def sortByView(numArticles):
  # get articles from Open Curriculum serers 
  articles = OC.articles.list(numArticles)

  # dictionary to map titles to (views, date)
  titles = dict()

  for id, a in articles.items():
    # extract date information
    s = a['citation']
    idx = s.find("accessed on ", 0) + len("accessed on ")
    date = s[idx:]

    titles[a['title']] = (a['views'], date)

  # sort by views
  return sorted(titles.items(), key=operator.itemgetter(1), reverse=True) 


# get 50 articles
titles = sortByView(50)

# test sortedness
for i in xrange(len(titles) - 1):
  t1, data1 = titles[i]
  t2, data2 = titles[i+1]
  if data1[0] < data2[0]:
    print "test failed"
    sys.exit(1)

for t, data in titles:
  # data[0] = views, date[1] = date
  print t + ": " + str(data[0]) + "\t " + data[1]
