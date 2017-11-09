--- Data Analysis Project
--- 
--- By Sophie Reddimalla  30/10/2017
------------------------------------------------
-- Description :
-- Sanitize log data so that it can be joined with 
-- other tables and make it easy to query.
--    * remove leading '/article/' from path so that it can be joined 
--      with slug in articles.
--    * remove time component from timestamp
--    * create error flag based on status column
-- ----------------------------------------------
CREATE OR REPLACE VIEW vw_log
AS 
SELECT right(path, -9)   article,
       date(time)        dt_log,
       CASE status 
           WHEN '200 OK' THEN 0
           ELSE 1
       END                error
FROM log;
   
