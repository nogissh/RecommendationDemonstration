import json
import numpy as np
from sklearn.cluster import KMeans

import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
base_sql = '''
select
  name, q1, q2, q3, q4, q5
from
  makeprofile_userprofile
where
  code = {}
'''

# query
cur.execute(base_sql.format('1111'))

# set array
namelist = []
qlist = []
for p in cur.fetchall():
  namelist.append(p[0])
  qlist.append(list(p[1:]))
qlist_np = np.array(qlist)

# clustering
pred = KMeans(n_clusters=4).fit_predict(qlist_np)

# replace to name
result = [[] for i in range(4)]
for i, r in enumerate(pred):
  result[r].append(namelist[i])

# out to file
with open('result.json', 'w') as f:
  json.dump(result, f, indent=2)
