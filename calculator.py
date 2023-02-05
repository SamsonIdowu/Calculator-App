from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return '''
        <style>
            body {
                background-color: black;
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            form {
                width: 500px;
                padding: 20px;
                background-color: white;
                color: black;
                border-radius: 10px;
            }
        </style>
        <form action="/" method="post">
            <input type="text" name="expression" style="width: 100%; padding: 10px; font-size: 20px;">
            <input type="submit" value="Calculate" style="width: 100%; padding: 10px; font-size: 20px;">
        </form>
    '''

@app.route('/', methods=['POST'])
def evaluate_expression():
    expression = request.form['expression']
    try:
        result = eval(expression)
        return 'Result: {}'.format(result)
    except:
        return 'Invalid expression'

if __name__ == '__main__':
    app.run()
