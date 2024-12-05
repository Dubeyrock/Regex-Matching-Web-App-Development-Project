from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex', '')

    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error as e:
        matches = [f"Invalid regex pattern: {e}"]

    return render_template('index.html', test_string=test_string, regex=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email', '')
    # Basic email regex pattern
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = bool(re.match(email_regex, email))
    
    return render_template('index.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
