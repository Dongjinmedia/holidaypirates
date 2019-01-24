from flask import Flask

app = Flask(__name__)



@app.route('/')

def hello():

	return 'Hello Raihan and holidaypirates!!!'




if __name__ == '__main__':

	app.run()
