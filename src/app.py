from flask import Flask, jsonify, request 
app = Flask(__name__)

# Suppose you have your data in the variable named some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    if "label" in request_body and "done" in request_body:
        if isinstance(request_body["label"], str) and isinstance(request_body["done"],bool):
            todos.append(request_body)
            return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)
    return jsonify(todos)










