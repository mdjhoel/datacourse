import os
import json
import webbrowser

# open data for reading and load into a variable, then close 
myfile = open("data.json")
mydata = json.load(myfile)
myfile.close()

# open a html file for writing
myhtml = open("test.html","w")

# loop over data and write it to a table, then close to finish write
myhtml.write("<table>")
for student in mydata["students"]:
    myhtml.write("<tr>")
    myhtml.write("<td>" + mydata["students"][student]["name"] + "</td>")
    myhtml.write("<td>" + str(mydata["students"][student]["year"]) + "</td>")
    myhtml.write("<tr>")
myhtml.write("</table>")
myhtml.close()

# open in a new browser tab
filename = 'file:///'+os.getcwd()+'/' + 'test.html'
webbrowser.open_new_tab(filename)

    

