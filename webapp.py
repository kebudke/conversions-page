from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/ftc")
def render_ftc():
    return render_template('fahrenheittocelsius.html')

@app.route("/itf")
def render_itf():
    return render_template('inchestofeet.html')

@app.route("/fti")
def render_fti():
    return render_template('feettoinches.html')

@app.route("/ftcresponse")
def render_ftcresponse():
    fahrenheit = float(request.args['fahrenheit'])
    celcius = (fahrenheit - 32)*(5/9)
    return render_template('ftcresponse.html', celsius = celsius)






if __name__=="__main__":
    app.run(debug=False, port=54321)
