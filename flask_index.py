from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index")
def first_web():
    name= 'Flask'
    #pasar la variable en la html
    return render_template('index.html', indez_variable=name)

app.run(debug=True )