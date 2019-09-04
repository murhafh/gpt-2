from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

from conditional_generation import load_generation_model

class GenerateText(Resource):

    def post(self):
        try:
            input_text = request.json['text']
            print(input_text)
            generated_text = load_generation_model(model_name="355M", raw_text=input_text)
            return {'generated_text': generated_text }

        except Exception as x:
            print(x)
            return {"error", "Internal error"}, 500

api.add_resource(GenerateText, '/generateText')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=3434, threaded=True)
