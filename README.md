# dse-203-project
dse 203 project 

This contains all the files for the dse-203 final project

1. Notebooks (Text Rank, dedupe)
2. Python scripts (Selenium webscraping)

Github wont let us upload the datasets due to size.


## Notebooks

- patent_topics_AI.ipynb
In this notebook, patents are processed and topics are extracted for AI patents. Companies who filed those patents are also identified.
Year 2017 to 2021 are processed as multithreaded process and csv file for each year was generated and then merged as one dataframe.

- org_vb_dedupe.ipynb
In this notebook, companies with their funded data scraped from Venture Beat are Entity Matched with companies who have AI patents filed.

- org_sb_patent.ipynb
In this notebook, companies and their funded data downloaded from SBIR (Small Business and Innovative Research) are Entity Matched with companies who have AI patents filed.

- venturebeat_Cleaning.ipynb
Data cleanup for data extracted from Venture Beat website. Dollar amounts were properly formatted among other cleaning.

- neo4j.ipynb
Not really a notebook persay but contains neo4j cypher command to upload data to build graph. Few sample cypher queries are also thrown in.

## Python Script. Web Scraping

- venturebeat_script.py
Script that was run to web scrape data from Venture Beat

## Neo4j Graph

- dse-203-project-2-neo4j.dmp
Its the neo4j dump which contains the final product of the project. Database password is password. Sorry, it wont allow as to have an empty password.


## Datasets
All the csv's are gzip which can be unzipped. There are 2 large files that couldnt be uploaded to Github due to size. 
These files are uploaded to Google Drive and shared. Download these files to dataset directory.
-	patent.tsv.gz
-	patent_assignee.tsv.gz



