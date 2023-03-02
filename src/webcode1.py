from flask import *
from src.dbconnection import *
from datetime import datetime
from flask import Flask, redirect, url_for, session
from flask_mail import Mail, Message
from flask_mail import *
import os
import smtplib

app = Flask(__name__)
app.secret_key = "anshid"

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "anshid283@gmail.com"
app.config['MAIL_PASSWORD'] = 'quynvmodakuxoubr'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "anshid283@gmail.com"

mail = Mail(app)

# ------------------------------------------------------------------------
# calling login page
@app.route("/", methods=['get', 'post'])
def main():
    return render_template("admin-home.html")
# ------------------------------------------------------------------------
# calling logout page
@app.route("/logout", methods=['get', 'post'])
def logout():
    session.pop('email', None)
    return render_template("login.html")
# ------------------------------------------------------------------------
# calling signup page
@app.route("/reg", methods=['post', 'get'])
def reg():
    return render_template("register.html")

# ------------------------------------------------------------------------
# calling add center page
@app.route("/addcenter", methods=['post', 'get'])
def addcenter():
    return render_template("Admin-addcenter.html")
# ------------------------------------------------------------------------
# calling admin home page
@app.route("/adminh", methods=['post', 'get'])
def adminh():
    return render_template("Admin-home.html")
# ------------------------------------------------------------------------
# calling admin-events  page
@app.route("/addeventsp", methods=['post', 'get'])
def addeventsp():
    return render_template("Admin-addevent.html")








# ------------------------------------------------------------------------
# calling contact page
@app.route("/contact", methods=['post', 'get'])
def contact():
    return render_template("user-contact.html")
# ------------------------------------------------------------------------
# calling user home page
@app.route("/userh", methods=['post', 'get'])
def userh():
    return render_template("user-index.html")
# ------------------------------------------------------------------------
# calling userdash  page
@app.route("/userdash", methods=['post', 'get'])
def userdash():
    return render_template("user-userdash.html")


# ------------------------------------------------------------------------
# calling admin-editevent  page
@app.route("/editeventpage", methods=['post', 'get'])
def editeventpage():
    id=request.args.get('ID')
    session['eventid']=id
    qry = "SELECT * FROM `events` WHERE eventid=%s"
    val=(id)
    res=selectone(qry,val)
    return render_template("Admin-editevent.html",val1=res)

# ------------------------------------------------------------------------
# calling contact list page and show all the enquiries users
@app.route("/viewEvents", methods=['post', 'get'])
def viewEvents():
    qry = "SELECT * FROM events"
    res = selectall(qry)

    return render_template("Admin-viewEvents.html", val=res)

# ------------------------------------------------------------------------
# calling contact list page and show all the enquiries users
@app.route("/contactlist", methods=['post', 'get'])
def customerlist():
    qry = "SELECT * FROM contact"
    res = selectall(qry)

    return render_template("Admin-contactlist.html", val=res)

# ------------------------------------------------------------------------
# calling allhalls  page
@app.route("/allhalls", methods=['post', 'get'])
def allhalls():
    qry = "SELECT * FROM halls"
    res = selectall(qry)
    return render_template("user-allcenters.html", val=res)

# ------------------------------------------------------------------------
# calling user-events  page
@app.route("/userevetns", methods=['post', 'get'])
def userevetns():
    qry = "SELECT * FROM events"
    res = selectall(qry)
    return render_template("user-events.html", val=res)

# ------------------------------------------------------------------------
# calling customer lis page and show all the loged users
@app.route("/customerslist", methods=['post', 'get'])
def customerslist():
    qry = "SELECT * FROM login,signup where login.lid=signup.lid"
    res = selectall(qry)
    return render_template("Admin-customerslist.html", val=res)





# ------------------------------------------------------------------------
# calling login function
@app.route("/login", methods=['get', 'post'])
def login():
    username = request.form['textfield1']
    password = request.form['textfield2']

    session['username'] = username

    qry = "SELECT * FROM login WHERE `username`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)

    if res is None:
        return ''' <script> alert('Invalid username or password');window.location="/" </script> '''
    elif res['type'] == "admin":
        session['lid'] = res['lid']
        return '''<script> alert('Welcome admin');window.location="/adminh"</script>'''
    else:
        session['lid'] = res['lid']
        return '''<script>alert('login successfull');window.location="/userh"</script>'''

# ------------------------------------------------------------------------
# signup function
@app.route("/registration", methods=['get', 'post'])
def registration():
    username = request.form['textfield1']
    name = request.form['textfield2']
    phone = request.form['textfield3']
    email = request.form['textfield4']
    password = request.form['textfield5']
    confirmpassword = request.form['textfield6']
    if name == "" or username == "" or email == "" or phone == "" or password == "" or confirmpassword == "":
        return '''<script> alert('Fill The Empty Cells');window.location="/reg"</script>'''


    elif password == confirmpassword:
        qry = "INSERT INTO login VALUES(NULL,%s,%s,'user')"
        val = (username, password)
        res = iud(qry, val)
        qry1 = "INSERT INTO `signup` VALUES (NULL,%s,%s,%s,%s)"
        val1 = (str(res), name, phone, email)
        res1 = iud(qry1, val1)
        return '''<script> alert('Successfully Registerd');window.location="/"</script>'''
    else:
        return '''<script> alert('Password Does not Match');window.location="/reg"</script>'''


# ------------------------------------------------------------------------
# add centre to database
@app.route("/insert", methods=['post', 'get'])
def insert():
    location = request.form['textfield1']
    name = request.form['textfield2']
    bprice = request.form['textfield3']
    phone = request.form['textfield4']
    email = request.form['textfield5']
    capacity = request.form['textfield6']
    decri = request.form['textfield7']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/" + fn)

    qry = "INSERT INTO halls VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (location, name, bprice, phone, email, capacity, decri, fn)
    res = iud(qry, val)
    return '''<script> alert('Successfully Added');window.location="/adminh"</script>'''

# ------------------------------------------------------------------------
# calling the more info page
@app.route("/moreinfo", methods=['post', 'get'])
def moreinfo():
    id = request.args.get('id')
    session['hid'] = id

    qry = "SELECT * FROM halls WHERE hid=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("user-moreinfo.html", vall=res)

# ------------------------------------------------------------------------
# calling mail  function
@app.route("/smail", methods=['post', 'get'])
def smail():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
    msg = Message("Hai" + name + " Thank you for contacting us.", recipients=[email])
    msg.body = message
    mail.send(msg)

    qry = "INSERT INTO contact VALUES(NULL,%s,%s,%s,%s,%s)"
    val = (session['lid'], name, email, subject, message)
    res = iud(qry, val)
    print(res)
    return '''<script> alert('Your Message Sended Successfully');window.location="/contact"</script>'''


# ------------------------------------------------------------------------
# add events to database by admin
@app.route("/addevents", methods=['post', 'get'])
def addevents():
    eventtype = request.form['text1']
    description = request.form['text2']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/event/" + fn)

    qry = "INSERT INTO events VALUES(NULL,%s,%s,%s)"
    val = (eventtype, description, fn)
    res = iud(qry, val)

    return '''<script> alert('Event Added Successfully');window.location="/addeventsp"</script>'''


# ------------------------------------------------------------------------
# deleting user in admin panel
@app.route("/deleteUser", methods=['post', 'get'])
def deleteUser():
    id = request.args.get('ID')
    qry = "DELETE FROM `login` WHERE `lid`=%s"
    val = (id)
    res = iud(qry, val)
    qry = "DELETE FROM `signup` WHERE `lid`=%s"
    val = (id)
    res = iud(qry, val)

    return '''<script>alert("Deleted successfully.");window.location="/customerslist"</script>'''


# ------------------------------------------------------------------------
@app.route("/hallcheck", methods=['post', 'get'])
def hallcheck():
    date1 = request.form['checkdate']
    print(date1)
    return '''<script> alert('Your Message Sended Successfully');window.location="/userh"</script>'''


# ------------------------------------------------------------------------
# Replaying to contacted users from admin panel
@app.route("/replay", methods=['get', 'post'])
def replay():
    id = request.args.get('ID')
    session['cid'] = id
    replay = request.form['re']
    qry = "SELECT `name`,`email`,`subject` FROM `contact` WHERE `cid` = %s"
    val = (id)
    res = selectone(qry, val)

    message = Message("Mr/Ms: " + res['name'] + " This is the replay for your subject on: " + res['subject'] + " REPLYAY :- " + replay,recipients=[res['email']])

    mail.send(message)

    return '''<script>alert("replay sended successfully.");window.location="/contactlist"</script>'''
# ------------------------------------------------------------------------
# deleting message in admin panel
@app.route("/deletemess", methods=['post', 'get'])
def deletemess():
    id = request.args.get('ID')
    qry = "DELETE FROM `contact` WHERE `cid`= %s"
    val = (id)
    iud(qry, val)
    return '''<script>alert("Deleted successfully.");window.location="/contactlist"</script>'''
# ------------------------------------------------------------------------
# deleting events in admin panel
@app.route("/deleteevent", methods=['post', 'get'])
def deleteevent():
    id = request.args.get('ID')
    qry = "DELETE FROM `events` WHERE `eventid`= %s"
    val = (id)
    iud(qry, val)
    return '''<script>alert("Deleted successfully.");window.location="/viewEvents"</script>'''

# ------------------------------------------------------------------------
# edit events in admin panel
# calling update function in admin panel
@app.route("/editevent",methods=['post','get']) # edit button action in admin panel
def editevent():
    eventtype = request.form['text1']
    description = request.form['text2']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/event/" + fn)



    qry="UPDATE `events` SET `eventtype`=%s,`description`=%s ,image=%s  where eventid=%s"
    val=(eventtype,description,fn,session['eventid'])
    res=iud(qry, val)
    return '''<script> alert('data Updated');window.location="/viewEvents"</script>'''


if __name__ == "__main__":
    app.run(debug=True)
