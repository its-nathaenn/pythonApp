from flask import Flask, render_template, request

# flask functions as a state based application

app = Flask(__name__)

# Make a homepage
@app.route("/")
def homepage():
    #return "<h1> This is the homepage of my App! </h1>"
    return render_template('base.html')



@app.route("/hello/<name>")
def hello(name):
    #listOfNames = [name, "yoyo", "yennifer"]
    #return render_template('name.html', Sname = name, nameList = listOfNames)
    return render_template("base.html")



@app.route('/form', methods=['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)



# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]



# Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug = True) # debug allows you to see what is happening 

