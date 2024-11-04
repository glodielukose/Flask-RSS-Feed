from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "No news is good"

if __name__ == "__main__":
  app.run()