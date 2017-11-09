#!/usr/bin/python
"""
It returns Top 3 most popular articles

"""
import psycopg2
conn = psycopg2.connect("dbname=news user=vagrant")

# Query 1:  TOP THREE ARTICLES BASED ON THE NUMBER OF VEIWS.#
cur = conn.cursor()
# THIS JOIN TWO TABLES : articles and vw_log on slug and article column#
# respectively#
sql = """
SELECT art.title, COUNT(*) cnt
  FROM articles art JOIN vw_log vwl
    ON art.slug = vwl.article
 GROUP BY art.title
 ORDER BY cnt DESC
 LIMIT 3;
 """
cur.execute(sql)
recs = cur.fetchall()
# THIS SHOWS THE FORMATTED ANSWER OF THE QUERY#
print "====================================================="
print " TITLE                             VIEWS        "
print "====================================================="
for rec in recs:
    print rec[0] + " | " + str(rec[1]) + " Views."

print "====================================================="
cur.close()
conn.close()
