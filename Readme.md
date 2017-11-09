# Data Analysis Project
# Project Title

Udacity Project 03 - Log Analysis

## Getting Started
### Initial setup
  1. Unzip data-analysis.zip into a folder .\data-analysis . Make sure that the folder is accesible from the Virtual Machine
  2. Connect to Virtual Machine.
  3. Create "news" database : Run the following command.
            psql -d news -f newsdata.sql
  4. Create Required views for the project : Run the following command.
            psql -d news -f create-views.sql
    
### Prerequisites
A linux Virtual Machine with following software 
    - postgres RDMS database
    - python 2.7 

 
### Getting Started
1. change the folder to .\data_analysis
2. Execute following scripts to view data analysis reports.
    a) To view top 3 popular articles, run ./famous_articles.py
    b) To view famous authors, run ./famous_authors.py
    c) To view dates on which more than 1% hits resulted in errors, run ./max_error_days.py


## Project Design
1. Created a view vw_log that Sanitize log data so that it can be joined with other tables and make it easy to query.
   (see create_views.sql for the query)
   View acheives the following objectives --
  * Removed leading '/article/' from path so that it can be joined with column 'slug' in table articles.
  * Removed time component from timestamp
  * Created column error based on status column (error=0 for no error ; error=1 for error)
2. All Queries are now fired against vw_log to return the desired results.

## Author 
Sophie Reddimalla.

## Acknowledgments
SAMSON REDDIMALLA


