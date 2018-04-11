from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def intro():
  return render_template('index.html')

@app.route('/ninjas')
def ninjas_intro():
  return render_template('ninjas.html')

@app.route('/dojos')
def dojos_intro():
  return render_template('dojos.html')

app.run(debug=True)
