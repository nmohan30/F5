from flask import Flask, render_template
from redis import Redis
import sys
import optparse
import time
import "SampleUserData.txt"


app = Flask(__name__)
redis = Redis(host='redis', port=5000)


start = int(round(time.time()))

@app.route('/search')
def search('SampleUserData.txt', listwords):
    redis.incr('search')
	try:
	text = open('SampleUserData.txt', 'r+')
	read = file.readlines()
	file.close()
	for word in listwords:
		lower = word.lower()
		count = 0
	for sentence in read:
		line = sentence.split
	for each in line:
		line2 = each.lower()
	if lower == line2:
		count += 1
	print(lower, ":", count)
	else 
	print("User does not exist")
	
 	except FileExistsError:
 		print("File Does not Exist")
	
	return render_template('search'.html', text=search) % redis.get('search')
 
 
#making sure that the page is reachable
if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python search.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
