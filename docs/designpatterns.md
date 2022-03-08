# Design Patterns
  
Date: 2022-03-08

Members present:

* Tyler Schickel
* Eli Nutter
* Clay Wright
  
## Design Pattern Being Used

Our program is currently working toward the Object Pool design pattern. The overall goal is to establish a movie class object, which pulls a lot of information into one class compared to re-establish it with each call of each webpage. This is to save the amount of resources establishing the movie object used currently. We plan to have each webpage/client(yes, no, genre) to reuse the same movie object by calling function to access information stored within the object to save resources and increase run time of the webpage compared to making a new object for each run page.

##Patterns that may fit well into our program

Adapter Pattern-Several of our components are currently static components. We hope to expand on functionality of static components into dynamic components that change without have to reload the page. We hope to use this to limit the subpages we need for our website currently without having to change the existing classes.

## Future Design Patterns

Iterator Pattern-The goal is to create a list class that we can access and traverse to find the information we need at a given time. Currently, we're looking at traversing the moving class by genre to send back a specific movie that matches the given movie to the client.

