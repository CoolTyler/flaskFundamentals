from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def intro():
  # return "Hello World!", "Tyler Bergstrom"
  return render_template('hello3.html')

@app.route('/projects')
def howdy_intro():
  return render_template('h3_projects.html')

@app.route('/about')
def kittens_intro():
  return render_template('h3_about.html')
app.run(debug=True)
