from flask import Flask, render_template
from redis import Redis
import sys
import optparse
import time
import "SampleUserData.txt"


app = Flask(__name__)
redis = Redis(host='redis', port=5000)


start = int(round(time.time()))

@app.route('/content')
def content():
    redis.incr('content')
	text = open('SampleUserData.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('content.html', text=content) % redis.get('content')
 
 
#making sure that the page is reachable
if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python content.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
