from flask import Flask

app = Flask(__name__)
# print(app.__dict__)
@app.route('/')
def index():
	return "hello World!!!"

if __name__ == "__main__":
	app.run(debug=True)