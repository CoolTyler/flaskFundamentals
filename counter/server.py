from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "ShhDontTell"

@app.route('/')
def keep_track():
  count = 0
  session['count'] += 1
  return render_template('index.html', count = session['count'])

@app.route('/add', methods=['POST'])
def add_two():
  session['count'] += 1
  return redirect('/')

app.run(debug=True)