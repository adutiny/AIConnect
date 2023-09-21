
 # This is a flask blueprint that contains all the routes for the authentication pages

from http import server
import os
from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
import flask
from pyparsing import html_comment
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from .import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template, request, redirect, url_for, flash
import flask
from flask import render_template
from flask_mail import Message
import imap_tools
from flask import redirect, url_for
from flask_login import UserMixin,current_user
from flask import Flask
from flask import request
from flask import Flask, render_template, request
import sqlite3
import base64
import getpass
import smtplib
from email.mime.text import MIMEText

from website.chatbotAITRU import *

from Key2 import aiconnect_email
from Key2 import aiconnect_pass

 








auth = Blueprint('auth', __name__)

#from chatbotaitru import *


# Create a new route for the index page
@auth.route('/')
def index():
   return render_template('index.html')

'''
@auth.route('/shop_cart')
def shop_cart():
   return render_template('shop_cart.html',user=current_user)
 
'''

# create a route for the about page
@auth.route('/about')
def about():
   return render_template('about.html',user=current_user)


'''

@auth.route('/truformtinyhouse')
def truformtinyhouse():
   return render_template('truformtinyhouse.html',user=current_user)
'''

# Create a route for the prompt page
@auth.route('/prompt')
def prompt():
   return render_template('prompttraining.html',user=current_user)


# create a route for the form for the Prompt Page, creates variables for the inputs into the contact page

@auth.route('/submit_form1', methods=['POST'])
def submit_Form1():
    name = flask.request.form['name']
    email = flask.request.form['email']
    phone = flask.request.form['phone']
    website = flask.request.form['website']

    # Pairs questions and answers from the prompt training form

    Q1 = flask.request.form["Q1"]
    A1 = flask.request.form["A1"]
    Q2 = flask.request.form['Q2']
    A2 = flask.request.form['A2']
    Q3 = flask.request.form['Q3']
    A3 = flask.request.form['A3']
    Q4 = flask.request.form['Q4']
    A4 = flask.request.form['A4']
    Q5 = flask.request.form['Q5']
    A5 = flask.request.form['A5']
    Q6 = flask.request.form['Q6']
    A6 = flask.request.form['A6']


   
# creates and sends the email to the user and to the company. With the q's and A's from the prompt training form
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email: str = "answers@aiconnectsale.com"  # Enter your address
    passwords = aiconnect_pass
    



    import smtplib

    # set the server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # start the server connection
    server.starttls()

    # use the login method to login to your email account
    server.login(sender_email, passwords)

    



    message2 = f'Subject: AI Connect Sales!\n\nHello {name} ,\n\n Thank you very much for filling out the Prompt Training form\n\n The more accurate you answers the better training we can do.\n\n If your pricing changes or any of the answers you have given change over time. Just go back to the form and fill it out with the nw answer, then press submit.\n\n Your changes will automatically update. within seconds. \n\nThanks again for your time!\nBest regards,\n Woody\nwww.aiconnectsales.com'
    server.sendmail(sender_email, email, message2)

        # create the message
    message3 = f'Subject: AI Connect Contact form\n\n Name: {name},\n\n Email: {email},\n\n Phone:{phone},\n\n Q1:{Q1,A1}\n\n Q2:{Q2,A2}\n\n Q3: {Q3,A3}\n\n Q4:{Q4,A4}\n\n Q5:{Q5,A5}\n\n Q6:{Q6,A6},\n\n ,\n\n Website:{website}\n\n'
    server.sendmail(sender_email,"answers@aiconnectsale.com",message3)

    return flask.render_template('confirmation.html')

    server.quit() 




# Creates a route for the Feedback page

@auth.route('/feedback')
def showform():
      return render_template('aiconnectform.html')

# Creates a route for the form for the feedback page, creates variables for the inputs into the feedback page

@auth.route('/submit_form', methods=['POST'])
def submit_Form():
    name = flask.request.form['name']
    email = flask.request.form['email']
    tool = request.form["tool"]
    leads = flask.request.form['leads']
    concerns = flask.request.form['concerns']
    accurate_is_AI = flask.request.form['accurate_is_AI']
    message22 = flask.request.form['message22']

    # Creates and sends emails to the user and to the company with the inputs from the feedback form

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email: str = "answers@aiconnectsale.com" # Enter your address
    passwords = aiconnect_pass



    #import smtplib

    # set the server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # start the server connection
    server.starttls()

    # use the login method to login to your email account
    server.login(sender_email, passwords)

    



    message2 = f'Subject: AI Connect Sales!\n\nHello {name},\n\nThank you very much for taking the time to answer our questions!\n\nI wanted to let you know that our AI technology has an impressive accuracy rate of approximately 95%, compared to the average employee accuracy rate, which ranges from 60% to 90%. You can find more information about our pricing on our website at www.aiconnectsales.com. We are dedicated to helping you improve your closing rates and reduce costs associated with your sales process.\n\nIf you are interested, we would be happy to give you a demo. You can schedule one by clicking on this link: https://calendar.app.google/yqJSrswLZzeV87Yn6.\n\nThanks again for your time!\nBest regards,\nWoody\nwww.aiconnectsales.com'
    server.sendmail(sender_email, email, message2)

        # create the message
    message3 = f'Subject: AI Connect Contact form\n\n Name: {name},\n\n Email: {email},\n\n leads:{leads},\n\n {concerns},\n\n accurate:{accurate_is_AI},\n\n message:{message22}\n\n, pay_for:{tool}\n\n'
    server.sendmail(sender_email,"answers@aiconnectsale.com",message3)

    return flask.render_template('confirmation.html')

    server.quit() 

# Creates a route for the contact page
 
@auth.route('/contact')
def showForm():
      return render_template('contact.html') 
 

 
#app = Flask(__name__)

# Create a route for the form for the contact page, creates variables for the inputs into the contact page

@auth.route('/submitForm', methods=['POST'])
def submitForm():
    name = flask.request.form['name']
    email = flask.request.form['email']
    phone = flask.request.form['phone']
    message1 = flask.request.form['message']


     # Create a file called contactresponse.txt
    with open('contactresponse.txt', 'w') as f:
        f.write(message1)


   
    

    

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email: str = "answers@aiconnectsale.com"  # Enter your address
    passwords = aiconnect_pass



    import smtplib

        # set the server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)

        # start the server connection
    server.starttls()

        # use the login method to login to your email account
    server.login(sender_email, passwords)





    message2 = f'Subject: AI Connect Sales!\n\n Hello {name},\n\n Just wanted to let you know that our AI Connect Sales is available to assist you 24/7, every single day.\n\n Not only is it significantly more cost-effective than hiring employees, but it also offers better accuracy.\n\n And if you would like to schedule a demo, simply visit https://calendar.app.google/ya5UzYYs567M49WW6.\n\n We are here to help anytime you need! '
    server.sendmail(sender_email, email, message2)

        # create the message
    message3 = f'Subject: AI Connect Contact form\n\n Name: {name},\n\n Email: {email},\n\n Phone: {phone},\n\n Message: {message1}\n\n'
    server.sendmail(sender_email,"answers@aiconnectsale.com",message3)

    return flask.render_template('confirmation.html')

    server.quit()


'''
@auth.before_request
def start_web_contact_ai():
    import subprocess
    subprocess.call('Web_contact_AI.py', shell=True)
'''    

        
# Create a new route for the addons page
@auth.route('/AIaddons')
def aiaddons():
    return render_template('AddOns.html') 


# Create a new route for the chatbot page
@auth.route('/response')
def chatbot(method = ["POST"]):
   prompt_list: list[str] = ['You are a AI software company called AI Connect Sales. You are a company that offers AI Email for $49.99 a month, AI Chatbots for $49.99 a month, and AI Text Automations for $59.99. You are located in Astoria Oregon. your website is www.aiconnectsales.com your email is answers@aiconnectsale.com  Your phone is 503-555-5555. according to www.aiconnectsales.com, you have been in business since 2023'
                              ]
   
   # Call the necessary functions from the chatbot file
   user_input = request.args['res']
   response = get_bot_response(user_input, prompt_list)
   print(response)
   # Render the response into the HTML page
   return render_template('index.html', response=response, user_input=user_input)
   #return render_template('index.html', response='', user_input='', background_color="#323232", text_color="whitesmoke")



#Login route
 

from flask import Flask, render_template, request, Response
import sqlite3
import base64
import getpass

app = Flask(__name__)

# Create riute for login page
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    # Encrypt the password
    encoded_password = base64.b64encode(password.encode())

    # Create a connection to the database
    connection = sqlite3.connect("user22222.db")

    # Create a cursor object
    cursor = connection.cursor()

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    # If the username does not exist, print an error message
    if user is None:
        print("Username does not exist.")
        return render_template("login.html", error="Username does not exist.")

    # Check if the password matches the password in the database
    if user[1] != encoded_password:
        print("Incorrect password.")
        return render_template("login.html", error="Incorrect password.")

    # Close the connection to the database
    connection.close()

    # Check if the AI Email folder exists for the user
    if not os.path.exists(os.path.join('AI Email', username)):

        # The folder does not exist, print an error message
        print("Folder does not exist.")
        return

    # The folder exists, open it
    os.startfile(os.path.join('AI Email', username))
    #os.open(os.path.join('AI Email', username), os.O_RDONLY)


    # Redirect the browser to the file
    #return redirect(os.path.join('AI Email', username))

    # Return a successful response
    return jsonify({"success": True})

     

if __name__ == "__main__":
    app.run(debug=True)

      

#signup route

from flask import Flask, render_template, request
import sqlite3
import base64
import getpass

app = Flask(__name__)

@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
        if request.method == "GET":
            return render_template("sign_up.html")

    #else:
        # Get the username and password from the user
        username = request.form["username"]
        password = request.form["password"]

        # Encrypt the password
        encoded_password = base64.b64encode(password.encode())

        # Create a connection to the database
        connection = sqlite3.connect("user22222.db")

        # Create a cursor object
        cursor = connection.cursor()

        # Create the users table if it doesn't already exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        # Check if the username already exists in the database
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        # If the username already exists, print an error message
        if user is not None:
            print("Username already exists.")
            return render_template("signup.html", error="Username already exists.")

        # Insert the username and password into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encoded_password))
        connection.commit()
        connection.close()

        # Create the folder in the AI Email folder
         # Create a folder with the same name as the username inside the AI Email folder
        os.mkdir(os.path.join('AI Email' , username))

    # Open the folder
    #os.startfile(os.path.join('AI Email', username))

    

        # Print a success message
        print("Successfully signed up!")
        return render_template("Thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)



 