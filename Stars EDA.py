##JUNIOR DE ASSESSMENT

import duckdb

#Reading Data Into Python
conn = duckdb.connect('stars.duckdb')


#Renaming g-rp to g_rp to avoid glitches in execution
conn.sql("""
         
ALTER TABLE star RENAME 'g-rp' TO g_rp
         
""")


##Count number of stars in each spectral class, Q2
conn.sql("""
         
SELECT
spectral_type AS Spectral_Class,
COUNT(spectral_type) AS Number_of_Stars

FROM 'star'
GROUP BY spectral_type 
ORDER BY 1    
         
         
""")


##Average distance byy spectral class, Q3
conn.sql("""

SELECT
spectral_type AS Spectral_Class,
AVG(distance) AS Average_Distance

FROM 'star'

GROUP BY spectral_type
         
""")

##Top 10 stars with highest Gmag values, Q4
conn.sql("""

SELECT
spectral_type,
gmag

FROM 'star'

ORDER BY gmag DESC LIMIT 10

""")    

## Dynamic GRP threshold, Q5

#prep statement
conn.sql("""

PREPARE grp_lowerlimit AS
SELECT*
FROM 'star'

WHERE star.g_rp > ? 
         
         
""")

#execution statement
conn.sql("""

EXECUTE grp_lowerlimit(0.2)         
""") 

#END 