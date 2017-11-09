#!/usr/bin/python
"""
It returns the days of where there were more than 1% errors detected.
"""
import psycopg2
import time
import datetime
conn = psycopg2.connect("dbname=news user=vagrant")

# Query 3:  THE DAY WHEN THERE WAS MORE THAN 1% ERRORS DETECTED.#
cur = conn.cursor()
# THE FOLLOWING QUERY TAKES THE dt_log column FROM THE vw_log TABLE
# SUMS UPTHE ERRORS ON A PARTICULAR DATE MAKES IT INTO A PERCENTAGE#
# AND CHECKS WHETHER THE ERROR PERCENTAGE IS MORE THAN 1% #
sql = """
SELECT dt_log, sum(error), count(*),
       ((sum(error) * 1.0 / count(*)) * 100.0)err_perc
FROM vw_log
GROUP BY dt_log
HAVING ((sum(error) * 1.0 / count(*)) * 100.0) > 1.0;
 """
cur.execute(sql)
recs = cur.fetchall()
# THIS SHOWS THE FORMATTED ANSWER OF THE QUERY#
print "====================================================="
print " DAY OF ERROR                 PERCENTAGE             "
print "====================================================="
for rec in recs:
    print "%8s                 |  %.2f" % (rec[0].isoformat(), rec[3]) + "%"

print "====================================================="
cur.close()
conn.close()
