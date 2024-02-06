from flask import Flask, render_template, request
from config import BOOTSTRAP_CSS_PATH, JQUERY_PATH, POPPER_PATH, BOOTSTRAP_JS_PATH

app = Flask(__name__)

# Sample list of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

def process_data():
    # This function can perform some processing on the data
    # For simplicity, let's just reverse the list of items
    return reversed(items)

def another_function_1():
    # This function can perform a different processing on the data
    # For simplicity, let's just return the list of items as is
    return items

def another_function_2():
    # Another example function
    # For simplicity, let's just return the list of items in uppercase
    return [item.upper() for item in items]

def another_function_3():
    # Another example function
    # For simplicity, let's just return the list of items in lowercase
    return [item.lower() for item in items]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'btn1' in request.form:
            result = process_data()
        elif 'btn2' in request.form:
            result = another_function_1()
        elif 'btn3' in request.form:
            result = another_function_2()
        elif 'btn4' in request.form:
            result = another_function_3()

    return render_template('index.html', items=items, result=result,
                           bootstrap_css_path=BOOTSTRAP_CSS_PATH,
                           jquery_path=JQUERY_PATH,
                           popper_path=POPPER_PATH,
                           bootstrap_js_path=BOOTSTRAP_JS_PATH)

if __name__ == '__main__':
    app.run(debug=True)
