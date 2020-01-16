from flask import Flask,request,render_template
from processing import do_addition
from processing import do_subtraction

#Load Flask framework
app = Flask(__name__)
app.config["DEBUG"] = True


#Create a Flask application
@app.route("/",methods=["GET","POST"])
def compute():
    errors = ""
    if request.method == "POST":

        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])

        #If number entered is valid
        if number1 is not None and number2 is not None :
            #--> addition
            if "add" in request.form:
                result1 = do_addition(number1, number2)
                result2 = do_subtraction(number1, number2)
                return '''
                    <html>
                        <body>
                            <p>The additive amount is {result1}</p>
                            <p>The additive amount is {result2}</p>
                            <p><a href="/">Click here to calculate again</a>
                        </body>
                    </html>
                '''.format(result1=result1,result2=result2)

    return '''<html lang="en">

            <head>

                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
                <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

            </head>
            <body class="text-center">
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action="." >
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" name="add" value="Calculate" /></p>

                </form>
            </body>
        
        </html>'''.format(errors=errors)

if __name__=="__main__":
    app.run()