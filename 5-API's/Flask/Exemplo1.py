from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Armazenar tarefas em memória
tasks = []

# Endpoint para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Endpoint para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'id' not in request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

# Endpoint para obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify(task)

# Endpoint para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404)
    
    if not request.json:
        abort(400)

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['completed'] = request.json.get('completed', task['completed'])
    
    return jsonify(task)

# Endpoint para excluir uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404)
    
    tasks.remove(task)
    return jsonify({'result': True})

# Instruções para rodar o servidor
# Use o seguinte comando no terminal:
# python app.py

if __name__ == '__main__':
    app.run(debug=True)
