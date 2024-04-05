from flask import Flask, Response
import requests
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

url = "https://http-server:5000"
@app.route("/")
def rr_balance():
	response = requests.get(url,verify=False)
	return Response(response.content,content_type=response.headers["Content-Type"])
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,ssl_context="adhoc")
@app.after_request
def nocache(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
