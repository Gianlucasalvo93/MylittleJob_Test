# MylittleJob_Test

Dependecies: Flask,requests,json,urllib2
Python version: 2.7.12

File descriptions:

Index.html: is the initial and main page. Here the user can choose the category about his searching and can view the results

Index_w_b.html: is a simple html page, Without the Button filter, where the user can type the searching name about the category chosen previously on Index.html

stylesheets: css of the page Index.html

stylesheets_w_b: css of the page Index_w_b.html.

Main.py: is the main python back-end file, developed with the Flask framework (view the comments of the source code)

         Its operations are:
            - calls properly the Spotify API, setting the flag "types"
            - render the html pages
