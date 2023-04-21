from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)

@app.route("/<username>/<int:post_id>")
def any_function(username=None, post_id=None):
    return render_template('index2.html', name = username,post_id=post_id)

def write_to_file(data):
    filename="F:/Complete_Python_Developer/Udemy_Python_Lectures_with_programs/web_server/database.txt"

    with open(filename,'a') as file:

        email=data['email']
        sub=data['subject']
        msg=data['message']
        file.write(f"\n{email},{sub},{msg}")

def write_to_csv(data):

    filename="F:/Complete_Python_Developer/Udemy_Python_Lectures_with_programs/web_server/data.csv"

    with open(filename,'a',newline='') as file2:
        fieldnames = ['email', 'subject', 'message']
       
        csv_writer = csv.DictWriter(file2, fieldnames=fieldnames)
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def login(): 
    if request.method=="POST":

        try:
            data=request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('./thankyou.html')

        except:
            return "It did not save in a database" 

    else :
        return "Something went wrong"