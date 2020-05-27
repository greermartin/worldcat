# worldcat
Scripts to count number of libraries holding a title for a given OCLC number using the WorldCat Search API. 

Lookup by OCLC number URL request documentation here: https://www.oclc.org/developer/develop/web-services/worldcat-search-api/library-locations.en.html

## What does it do?
Each script takes am inout csv with OCLC numbers, finds library holdings for each OCLC number up to 100 libraries, counts the number of libraries, and outputs a new csv with an appended column containig the library count. FRBR Grouping is on or off, according to the filename (count_us_libraries_frbrOn.py = FRBR Grouping set to "on");

Scripts count holdings in US, IL, with FRBR Grouping set to ON or OFF. Ex. `count_us_libraries_frbrOn.py` = library holdings for US, FRBR Grouping set to "on".

## What are the requirements?
* Requires WorldCat institution authentication key
* Store key in file named worldcat_auth.txt
* Inclue filenames for input and output csv in script
* One OCLC number per row in input csv
* OCLC number must be in column labeled "OCLC Number" (no quotes)
* Python file, input csv and worldcat_auth.txt must be in same directory

## Recommendations
Run in batches of 1,000 OCLC numbers or possibly fewer for US counts, or else service will time out.
