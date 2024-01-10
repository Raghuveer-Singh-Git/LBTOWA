# Data Source
We mainly used weatherapi.com.
- The API gave us 1000 free API calls per hour, which allowed us to experiment with different chunk sizes
- The API gave us a lot of information, including location name which helped us with formatting
- The API information was accurate and real-time, as we compared Singapore’s weather using the API and Google Weather and find no discrepancies

# Formatting
### Cleaning before API Calls
- Continents were drafted by “boxing” them into rectangles, such that the whole continent is represented with dimensions measured in latitude and longitude
- Too many API calls were being wasted on inhabited regions like the oceans and Antarctica, so we decided only to include the continents
### Cleaning after API Calls
- Large bodies of water surrounding the continents as well as lots of uninhabited regions remained and were called
- Many locations had no name or marking, but some had a numerical value such as “Kilometre 52” which had no usable information, so they were removed before printing the results

# Data gathering
- All longitudes for a given latitude would loop through first with the latitude being amended by a certain amount, after which the longitude would be changed by the same amount and the latitude would loop through again
- The smaller the amount, the more precise the collection. A value of 10 would require 1620 API calls, so we used a value of 20 at most for our tests unless we were focusing on a certain continent
- Finally, location, precipitation and temperature data was extracted from the API call and printed

# Samples
<img src="https://raw.githubusercontent.com/Raghuveer-Singh-Git/LBTOWA/main/Weather_Data/AustraliaNew.png" style="width:600px">
<img src="https://raw.githubusercontent.com/Raghuveer-Singh-Git/LBTOWA/main/Weather_Data/weather-data-demo.png" style="width:600px">

