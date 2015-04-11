#This script gives customkeys for books.html so that sorttable.js keeps sorting method
import re
import os

print os.path.dirname(__file__)
filename = os.path.dirname(__file__) + "\\books.html"
file = open(filename, 'r+')

i = 1
regex = re.compile(r".*</td><td>.*")
pattern = "</td><td>"
n = 2;

oname = os.path.dirname(__file__) + "\\books1.html"
outfile = open(oname, 'w+')

if file:
	for line in file.readlines():
		if regex.match(line):
			parts = re.split(pattern, line)
			first = parts[:n]
			last = parts[n:]
			j1 = pattern.join(first)
			j1 += "</td><td sorttable_customkey=\"" + str(i) + ("\">")
			j2 = pattern.join(last)
			new = ''.join([j1, j2])
			i += 1
			outfile.write(new)
		else:
			outfile.write(line)

#<tr class="tableizer-firstrow"><th>&nbsp;&nbsp;Book</th><th>&nbsp;&nbsp;Author</th><th>&nbsp;&nbsp;Dates Read</th><th>Rating* <br>(1-5)</th><th>&nbsp;&nbsp;Comments</th></tr>
#<tr><td>The Memoirs of Sherlock Holmes</td><td>Arthur Conan Doyle</td><td>Feb 2014 - April 2015</td><td>4.5</td><td>&nbsp;</td></tr>

file.close()