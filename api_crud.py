from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "done": False},
    {"id": 2, "title": "Task 2", "description": "Description 2", "done": False},
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# GET single task by id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404

# POST a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# PUT update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    data = request.json
    task.update({
        'title': data.get('title', task['title']),
        'description': data.get('description', task['description']),
        'done': data.get('done', task['done'])
    })
    return jsonify({'task': task})

# DELETE a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
