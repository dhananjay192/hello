# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"
#print("hello")
import azure.functions as func

 

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Hello, Azure Functions!")
