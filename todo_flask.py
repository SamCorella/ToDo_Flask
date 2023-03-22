from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect(url_for('todo'))

@app.route('/edit/<int:index>')
def edit(index):
    pass

if __name__ == "__main__":
    app.run(debug=True)
