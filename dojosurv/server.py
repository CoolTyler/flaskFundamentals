from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def intro():
  return render_template('index.html')

@app.route('/success')
def success():
  # name = request.form['name']
  # email = request.form['email']
  # gender = request.form['gender']
  return render_template('success.html')

@app.route('/process', methods=['POST'])
def process():
  data = {
    "name": request.form['name'],
    "email": request.form['email'],
    "gender": request.form['gender']
  }
  return render_template('success.html', form_data = data)

app.run(debug=True)