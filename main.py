from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
     form= """
    <!DOCTYPE html>
    <html>
        <body>
            <form>
                <label for "rot">Rotate by:</label>
                <input  type="text" name="rot" />
                <input type="textarea" name="text" />
                <input type="submit" /
            </form>
        </body>
    
    
    </html>



      """
    </body>
</html>


@app.route("/")
def index():
    return "Hello World"