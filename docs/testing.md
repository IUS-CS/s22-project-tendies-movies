# Testing
  
Date: 2022-03-29

Members present:

* Tyler Schickel
* Eli Nutter
* Clay Wright

## Current Testing

Currently in the code, we've created a testing.py file that uses unit test implemented with the plugin pytest. The biggest item we wanted to test was to 
ensure our current function is able to find the various genres of movies using the Cinemagoer plugin we have installed. Currently there are 18 unit tests 
to find the 18 different genres of movies that are present within the IMDB Top 250 lists. Each unit tests returns that the genres are found, but the unit 
test also show that our code needs a lot of optimization before it is ready as a product for a user. 

##Future Testing

Future testing will include testing our UI. Finding genres of movies is a good first step, but we want to test that the buttons within our website lead to the
correct pages and returns the correct information to the users(i.e., pressing a button on the website does what we want the button to do). We would also like 
to expand testing to UI. Currently, everything is showing the information we want, but we would like to implement testing into our code that proves
our UI is consistent.
