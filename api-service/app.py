from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'


# @app.route('/gpt')
# def getResponse():
#     topic = request.args.get('topic')
#     total_slides = int(request.args.get('total_slides'))
#     return get_openai_response(topic, total_slides)

if __name__ == '__main__':
	app.run(debug=True)