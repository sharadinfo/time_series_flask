#from flask import Flask, render_template
#from flask import Flask, jsonify, request
#import csv
#with open('abc.csv', 'r') as csvFile:
 #   reader = csv.reader(csvFile, dialect='myDialect')
  #  for row in reader:
   #	 return render_template('dashboard.html',row=row)

#csvFile.close()
from flask import Flask, reader_template
from flask import Flask, jsonify, request

import csv
with open('abc.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
	return render_template("dashboard.html" ,row = row)
csvFile.close()
