from app import app

@app.route('/greeting', defaults={'name': None})
@app.route('/greeting/<name>')
def greeting(name):
    print(name)
    if name:
        return f'It is a pleasure to meet you, {name}!'
    return 'It is a pleasure to meet you, user!'