from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <form action="/calculate" method="post">
            <input type="text" name="expression">
            <input type="submit" value="Calculate">
        </form>
    ''')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run()
