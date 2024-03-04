from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)
    
    return render_template('results.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return 'Valid email address!'
    else:
        return 'Invalid email address!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

