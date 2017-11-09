#!/usr/bin/python
"""
It returns the most famous authors based on the page veiws.

"""
import psycopg2
conn = psycopg2.connect("dbname=news user=vagrant")

# Query 2:  FAMOUS AUTHORS BASED ON THE NUMBER OF  PAGE VEIWS.#
cur = conn.cursor()
# THE FOLLOWING JOINS TWO TABLES: articles and vw_log , articles and authors #
sql = """
SELECT aut.name, COUNT(*) cnt
   FROM vw_log vwl
   JOIN articles art ON art.slug = vwl.article
   JOIN authors  aut ON aut.id   = art.author
  GROUP BY aut.name
  ORDER BY cnt DESC;
 """
cur.execute(sql)
recs = cur.fetchall()
# THIS SHOWS THE FORMATTED ANSWER OF THE QUERY#
print "====================================================="
print " AUTHOR                               PAGE VIEWS  "
print "====================================================="
for rec in recs:
    print rec[0].ljust(30," ")  + str(rec[1]).rjust(10," ") + " Page Views."

print "====================================================="
cur.close()
conn.close()
