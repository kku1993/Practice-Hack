# Copyright 2013 Kevin Ku, Trisha Black, Wenni Zhou
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Version 1.0

import operator
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

# test function 
def test(num):
  # get 50 articles
  titles = sortByView(num)

  # test sortedness
  for i in xrange(len(titles) - 1):
    t1, data1 = titles[i]
    t2, data2 = titles[i+1]
    assert(data1[0] >= data2[0])

  for t, data in titles:
    # data[0] = views, date[1] = date
    print t + ": " + str(data[0]) + "\t " + data[1]
