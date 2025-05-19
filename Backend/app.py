from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

TASK_FILE = 'tasks.json'

# Read all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    if not os.path.exists(TASK_FILE):
        return jsonify([])
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)
    return jsonify(tasks)

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    if not new_task:
        return jsonify({"error": "Invalid data"}), 400
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = json.load(file)
    tasks.append(new_task)
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)
    return jsonify(new_task), 201

# Delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)
    tasks = [task for task in tasks if task['id'] != task_id]
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)
    return jsonify({"message": "Task deleted"}), 200

# Update a task
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks[i] = updated_task
            break
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)
    return jsonify(updated_task), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
