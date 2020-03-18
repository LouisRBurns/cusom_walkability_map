# Custom Walkability Map
### Executive Summary
If you have ever used WalkScore, you've seen it is basically a kernal density map (aka heat map) showing the concentration of 10 different types of amenities. What if you're not interested in all 10? What if you don't care about shopping or schools? This script takes in user pereferences and generates a custom walkability map. This was a class project for GISc Programming in 2014. 
### Data
I extracted the 25,000+ amenities from ESRI Business Analyst through a search for the relevant NAICS codes. The basemap is for 
### Methodology
This program asks the user to rank (1-10) twelve different amenities. Then it prints the ranking to confirm with the user that they are happy with their choices. If not, it allows the user to go back and rerank the choices. It then updates the amenities map layer with the rankings and then executes an inverse distance weight operation with a range of 0.25 miles.
### Results
Here we see two maps: one with a focus on coffee shops and bars, and one with a focus on parks and water features.
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Coffee and Bars")
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Parks and Water")
### Discussion
This program was written in Python 2 and needs to be refactored and updated to run properly. It also relys on the proprietary ESRI arcpy package and if I were doing this again, I would use geopandas or possibly R. I found Business Analyst to typically be inaccurate enough that I would be wary of using it for production mapping. A better choice would probably be Google's mapping API. 

For the mapping, this script was a proof of concept. The scale is much too large to be practical in walking though if you were looking for a new place to live in DFW you might use it as a starting point. 

Finally, the looping structure I wrote at the time is awkward. Now, I would loop through a list rather than write a long set of if/then statements. It was my second formal programming class and the emphasis was on using the arcpy package. 