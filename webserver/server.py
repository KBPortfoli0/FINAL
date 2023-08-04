from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<username>/')
def info(username=None):
    return render_template('index.html', name=username)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database2:
        email = data["email"]
        password = data["password"]
        passwordconfirm = data["passwordconfirm"]
        file = database2.write(f'\n{email},{password},{passwordconfirm}')
def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        password = data["password"]
        passwordconfirm = data["passwordconfirm"]
        csv_writer = database.write(database, delimiter=',', quotecharacter='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,password,passwordconfirm])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. try again.'