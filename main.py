from flask import Flask, render_template
from string import printable
import random

app = Flask(__name__)

@app.route("/")
def index():
	chars = printable.strip()
	password = ""
	for i in range(20):
		password += random.choice(chars)
	return render_template("index.html", password = password)

def main():
	app.run(host = "0.0.0.0", port = 443)

if __name__ == "__main__":
	main()
