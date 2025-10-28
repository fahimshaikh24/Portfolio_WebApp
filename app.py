#Portfolio Web Application Using Flask
#Author : Fahim Shaikh

from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "mysecretkey"  # Required for flash messages

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

#Contact us page 
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']
        flash(f"Thank you {fullname}, I will contact you soon! ✅")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
