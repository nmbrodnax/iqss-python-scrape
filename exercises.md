## Introduction to Web Scraping with Python
[NaLette Brodnax](http://www.nalettebrodnax.com)<br>


## Workshop Exercises 

### Part 1: Introduction

 1. Complete the one-minute poll at [bit.ly/dsspoll](http://bit.ly/dsspoll).

### Part 2: Getting the Tools

 1. Create a new script called *review.py*.

### Part 3: Python Review

 1. Create a list called `datasets` with the following names as contents: airport, baseball, calcium, electricbill, and freethrows.  Use print statements and references to display the following:
    
    * the first item in the list
    * the third and fourth items in the list
    * the second-to-last item in the list

    Create a dictionary called `data_info` for the *airport* dataset.  The dataset's title is *US Airport Statistics* and it has 135 observations.  Use a print statement and reference to display the title of dataset.

 2. Write a loop that will display each name in `datasets` with the extension *.txt* on the end.

 3. Create a function called `add_extensions()` that accepts a list of strings, adds '.txt' to each string in the list, and returns a list of the new strings.  Try calling `add_extensions()` with `datasets` as an argument.

 4. Add a statement to import functions from the `requests` Python library.  Use the `.get()` method to request the contents of the following webpage: http://ww2.amstat.org/publications/jse/jse_data_archive.htm. Use a print statement to display the HTTP response code for the request.


[Click here](https://github.com/nmbrodnax/iqss-python-scrape/blob/master/files/intro_web_scraping.zip) to download the code for all exercises.

