from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return '''
        <style>
            body {
                background-color: black;
                color: white;
            }
        </style>
        <form action="/" method="post">
            <input type="text" name="expression">
            <input type="submit" value="Calculate">
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
