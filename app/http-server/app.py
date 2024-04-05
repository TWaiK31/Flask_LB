from flask import Flask
from flask import request
import os
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
@app.route("/")
def server():
	return f"<p> Flask web server on {request.environ.get('HTTP_X_REAL_IP', request.remote_addr)}. Hello world!</p>"
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,ssl_context="adhoc")
@app.after_request
def no_cache(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate,public, max-age=0"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	return r
