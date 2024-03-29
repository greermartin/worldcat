# worldcat
Scripts to count number of libraries holding a title for a given OCLC number using the WorldCat Search API. 

Lookup by OCLC number. API documentation here: https://developer.api.oclc.org/wcv1

## What does it do?
Each script takes am input csv with OCLC numbers (omit (OCoLC)ocn, (OCoLC)ocm, and (OCoLC) prefixes), finds library holdings for each OCLC number up to 100 libraries, counts the number of libraries, and outputs a new csv with an appended column containing the library count. Default value for the FRBR Grouping parameter is on, the scripts with "frbrOff" in filename have FRBR Grouping set to off (ex. count_il_libraries_frbrOff.py).

## What are the requirements?
* Requires WorldCat institution authentication key
* Store key in file named worldcat_auth.txt
* Inclue filenames for input and output csv in script
* One OCLC number per row in input csv
* OCLC number must be in column labeled "OCLC Number" (no quotes)
* Python file, input csv and worldcat_auth.txt must be in same directory
* Leading zeroes in OCLC numbers should be removed for FRBR Grouping Off counts (otherwise will not retrieve holdings). Counts for FRBR Grouping On will not be affected if leading zeroes are removed.

## Recommendations
Run in batches of 1,000 OCLC numbers or possibly fewer for US counts, or else service will time out.
