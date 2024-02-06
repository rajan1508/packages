from flask import Flask, render_template, request
import os,shutil

app = Flask(__name__)

# Sample list of items
items = []

def process_data():
    # This function can perform some processing on the data
    # For simplicity, let's just reverse the list of items

    files = os.walk(r"C:\Users\rajan\OneDrive\Desktop\Personal\Btech_Marksheet")
    des = r"C:\Users\rajan\Music"
    items.clear()

    copied = 0

    for r,s,f in files:
        for i in f:
            items.append(i)
            shutil.copy2(os.path.join(r,i),des)
    
    return len(items)

def another_function():
    return 'checking another_function'

@app.route('/Process', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'btn2' in request.form:
            # Call another function when the second button is clicked
            result = process_data()
        else:
            # Call the default function when the first button is clicked
            result = another_function()
        # Call the function when the button is clicked
        # result = process_data()

    return render_template('index.html', items=items, result=result)

if __name__ == '__main__':
    app.run(debug=True)
