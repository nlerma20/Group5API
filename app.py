##Project 3
##REST API
## app.py

from flask import Flask
import hashlib
app = Flask(__name__)

@app.route("/")
def howdy():
    return "<h1>Hello World</h1>"

@app.route("/md5/<string>")
def md5(string):
	hash_object = hashlib.md5(string.encode())
	md5_hash = hash_object.hexdigest()
	return(md5_hash)
    
@app.route("/factorial/<num>")
def fact(num):
	intnum = int(num)
	factorial = 1
	if intnum == 0:
		return 'Factorial of 0 is 1'
	if intnum < 0:
		return 'Error, please enter a positive integer'
	else:
		for i in range(1,intnum + 1):
			factorial = factorial*i
		return(str(factorial))
    

@app.route("/fibonacci/<int>")
def fib():
    return

@app.route("/is-prime/<int>")
def prime():
	return

@app.route("/slack-alert/<string>")
def slackAlert():
	return

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')