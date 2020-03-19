# worldcat
Scripts to count number of libraries holding a title for a given OCLC number using the WorldCat Search API. 

Lookup by OCLC number URL request documentation here: https://www.oclc.org/developer/develop/web-services/worldcat-search-api/library-locations.en.html

## What does it do?
Each script takes a csv with OCLC numbers, finds library holdings for each OCLC number up to 100 libraries, counts the number of libraries, and outputs a new csv with an appended column containig the library count. 

One script counts holdings in US, another script counts holdings in IL. 

## What are the requirements?
* Requires WorldCat institution authentication key
* Store key in file named worldcat_auth.txt
* Input csv must be named batch.csv
* Python file, batch.csv, and worldcat_auth.txt must be in same directory
* One OCLC number per row
* OCLC number must be in column labeled "OCLC Number" (no quotes)
