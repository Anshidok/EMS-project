from flask import *
from src.dbconnection import *
from datetime import datetime
from flask import Flask, redirect, url_for, session
from flask_mail import *
import os
import smtplib

app = Flask(__name__)
app.secret_key = "anshid"

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "emsconvo@gmail.com"
app.config['MAIL_PASSWORD'] = 'blyanvwmjowqextk'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "emsconvo@gmail.com"

mail = Mail(app)


# ------------------------------------------------------------------------
# calling login page
@app.route("/", methods=['get', 'post'])
def main():
    #return '''<script>window.location="/l"</script>'''
     return '''<script>window.location="/userh"</script>'''
    # return render_template("venue_addvenue.html")


# ------------------------------------------------------------------------
@app.route("/l", methods=['get', 'post'])
def l():
    return render_template("login.html")


# ------------------------------------------------------------------------
# calling logout page
@app.route("/logout", methods=['get', 'post'])
def logout():
    session.pop('logged_in', None)
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
# calling change pass  page
@app.route("/changepassw", methods=['post', 'get'])
def changepassw():
    return render_template("changepass.html")



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
# calling user home page
@app.route("/userh", methods=['post', 'get'])
def userh():
    return render_template("user-index.html")
# ------------------------------------------------------------------------
# calling contact page
@app.route("/contact", methods=['post', 'get'])
def contact():
        return render_template("user-contact.html")

# ------------------------------------------------------------------------
# calling userdash  page
@app.route("/userdash", methods=['post', 'get'])
def userdash():
    return render_template("user-userdash.html")

# ------------------------------------------------------------------------
# calling veue add venue page in venueadmin page
@app.route("/venueadd", methods=['post', 'get'])
def venueadd():
    return render_template("venue_addvenue.html")
# ------------------------------------------------------------------------
# calling add payment page in venueadmin page
@app.route("/addpay", methods=['post', 'get'])
def addpay():
    return render_template("venue_addpayment.html")

# ------------------------------------------------------------------------
# calling veue add venue page in venueadmin page
@app.route("/allbookings", methods=['post', 'get'])
def allbookings():
    qry = "select * from bookings "
    res = selectall(qry,)
    return render_template("Admin-allbookings.html",val=res)


# ------------------------------------------------------------------------
# calling  update veue  page in venueadmin page
@app.route("/venueupdate", methods=['post', 'get'])
def venueupdate():
    id = session['lid']
    qry = "select * from halls where addid =%s"
    val1 = (id)
    res = selectone(qry, val1)
    return render_template("venue_update.html", val=res)

# ------------------------------------------------------------------------
# calling veue home  in venueadmin page
@app.route("/venueh", methods=['post', 'get'])
def venueh():
    id = session['lid']
    qry = "SELECT *  FROM `bookings` WHERE venueid=%s"
    val = (id)
    res = selectall2(qry,val)
    
    qry = "SELECT COUNT(*) as tt  FROM `bookings` WHERE venueid=%s"
    res1 = selectall2(qry,val)

    qry = "SELECT COUNT(*) as tp FROM `bookings` WHERE venueid=%s AND `status`='Pending'"
    res2 = selectall2(qry,val) 

    qry = "SELECT COUNT(*) as ts FROM `bookings` WHERE venueid=%s AND `status`='Aprove'"
    res3 = selectall2(qry,val)

    qry = "SELECT COUNT(*) as tr FROM `bookings` WHERE venueid=%s AND `status`='Pending'"
    res4 = selectall2(qry,val)
    
    
    return render_template("venue_index.html",val=res,val1=res1,val2=res2,val3=res3,val4=res2)


# ------------------------------------------------------------------------
# calling bookings page in venueadmin section
@app.route("/venuebookings", methods=['post', 'get'])
def venuebookings():

    id = session['lid']
    qry = "SELECT *  FROM `bookings` WHERE venueid=%s"
    val = (id)
    res = selectall2(qry,val)

    qry = "SELECT COUNT(*) as tt  FROM `bookings` WHERE venueid=%s"
    res1 = selectall2(qry,val)

    qry = "SELECT COUNT(*) as ts FROM `bookings` WHERE venueid=%s AND `status`='Aprove'"
    res2 = selectall2(qry,val)

    qry = "SELECT COUNT(*) as tp FROM `bookings` WHERE venueid=%s AND `status`='Pending'"
    res3 = selectall2(qry,val) 
    

    qry = "SELECT * FROM `halls` WHERE addid=%s"
    res4 = selectall2(qry,val)
    

    return render_template("venue_bookings.html",val=res,val1=res1,val2=res2,val3=res3,val4=res4)

# ------------------------------------------------------------------------
# calling reservation  page
@app.route("/more", methods=['post', 'get'])
def more():
    id = session['hid']

    qry = "SELECT * FROM halls WHERE hid=%s"
    val = (id)
    res = selectone(qry, val)
    # return render_template("user-moreinfo.html", vall=res)
    return render_template("reservation.html", vall=res)


# ------------------------------------------------------------------------
# calling admin-edit venue  page
@app.route("/editvenuepage", methods=['post', 'get'])
def editvenuepage():
    id = request.args.get('ID')
    qry = "SELECT * FROM `halls` WHERE hid=%s"
    val1 = (id)
    res = selectone(qry, val1)
    return render_template("Admin-editvenue.html", val=res)


# ------------------------------------------------------------------------
# calling viewVenue page and show all added venues
@app.route("/viewVenues", methods=['post', 'get'])
def viewVenues():
    qry = "SELECT * FROM halls"
    res = selectall(qry)
    print(res)
    return render_template("Admin-viewVenues.html", val=res)


# ------------------------------------------------------------------------
# calling admin-editevent  page
@app.route("/editeventpage", methods=['post', 'get'])
def editeventpage():
    id = request.args.get('ID')
    session['eventid'] = id
    qry = "SELECT * FROM `events` WHERE eventid=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("Admin-editevent.html", val1=res)


# ------------------------------------------------------------------------
# calling viewEvents page and show all added events
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
# calling contact list page and show all the enquiries users
@app.route("/payment", methods=['post', 'get'])
def payment():
    if session.get('hid') is not None:
        # id=session['lid']
        # qry = "select * FROM `bookings` WHERE lid=%s"
        # val1=(id)
        # res1 = selectone(qry,val1)
        # print(res1['venueid'])


        id=session['hid']
        qry = "SELECT * FROM paymentd where hid=%s"
        val=(id)
        res = selectone(qry,val)
        # print(res)
        return render_template("payment.html",val1=res)
    else:
        return '''<script>alert('You have not made a booking yet!');window.location="/userevetns"</script>'''



# ------------------------------------------------------------------------
# calling allhalls  page
@app.route("/allhalls", methods=['post', 'get'])
def allhalls():
    # if not session.get('logged_in'):
    #     return '''<script>alert('You Are Not Logged In Yet!');window.location="/l"</script>'''
    # else:
        qry = "SELECT * FROM halls"
        res = selectall(qry)
        return render_template("Venues.html", val=res)
        # return render_template("user-allcenters.html", val=res)


# ------------------------------------------------------------------------
# calling user-events  page
@app.route("/userevetns", methods=['post', 'get'])
def userevetns():
    # if not session.get('logged_in'):
    #     return '''<script>alert('You Are Not Logged In Yet!');window.location="/l"</script>'''
    # else:
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
# calling eventcustomize page
@app.route("/customize", methods=['post', 'get'])
def customize():
    if not session.get('logged_in'):
        return '''<script>alert('You Are Not Logged In Yet!');window.location="/l"</script>'''
    else:
        id = request.args.get('ID')
        session['eventid'] = id
        qry = "SELECT * FROM `events` WHERE eventid=%s"
        val = (id)
        res = selectone(qry, val)
        return render_template("user-eventcustomize.html", val=res)


# ------------------------------------------------------------------------
# calling booking details show page
@app.route("/bookingdetails", methods=['post', 'get'])
def bookindetails():
    if not session.get('logged_in'):
        return '''<script>alert('You Are Not Logged In Yet!');window.location="/l"</script>'''
    else:
        # if 'hid' not in session:

        #     return '''<script>alert('You have not made a booking yet!');window.location="/userevetns"</script>'''
        if session.get('hid') is not None: # check the hid in session or not 
            id = session['hid']
            qry = "SELECT * FROM `halls` WHERE hid=%s"
            val = (id)
            res = selectone(qry, val)
            

            id = session['lid']
            qry = "SELECT * FROM `bookings` WHERE lid=%s"
            val = (id)
            res1 = selectone(qry, val)
            

            return render_template("user-bookings.html", val1=res1, val2=res)
        else:

            id = session['lid']
            qry = "SELECT * FROM `bookings` WHERE lid=%s"
            val = (id)
            res1 = selectone(qry, val)
            # res2 = res1({['date']:None})
            # print (res2)
            return render_template("user-bookings.html", val1=res1, val2=None)


# ------------------------------------------------------------------------
# calling booking page
@app.route("/book", methods=['post', 'get'])
def book():

    if session.get('eventid') is not None: # check the eventid in session or not 
        id = session['hid']
        qry = "SELECT * FROM `halls` WHERE hid=%s"
        val = (id)
        res = selectone(qry, val)

        id1 = session['eventid']
        qry1 = "SELECT * FROM `events` WHERE eventid=%s"
        val1 = (id1)
        res1 = selectone(qry1, val1)

        # return render_template("user-book.html",val=res,val1=res1)
        return render_template("book.html", val=res, val1=res1)
    else:
        return '''<script>alert('You have not select a EVENT type yet!');window.location="/userevetns"</script>'''
        


# ------------------------------------------------------------------------
# calling login function
@app.route("/login", methods=['get', 'post'])
def login():
    username = request.form['textfield1']
    password = request.form['textfield2']

    qry = "SELECT * FROM login WHERE `username`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)

    if res is None:
        return ''' <script> alert('Invalid username or password');window.location="/" </script> '''
    elif res['type'] == "admin":
        session['lid'] = res['lid']
        session['logged_in'] = True
        return '''<script> alert('Welcome admin');window.location="/adminh"</script>'''
    elif res['type'] == "venue":
        session['lid'] = res['lid']
        session['logged_in'] = True
        return '''<script> alert('Welcome admin');window.location="/venueh"</script>'''
    else:
        session['lid'] = res['lid']
        session['logged_in'] = True
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
    decri = request.form['textfield7']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/venues/" + fn)

    qry = "INSERT INTO halls VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (session['lid'], location, name, bprice, phone, email, decri, fn)
    res = iud(qry, val)
    return '''<script> alert('Successfully Added');window.location="/adminh"</script>'''


# ------------------------------------------------------------------------
# calling the more info page
@app.route("/moreinfo", methods=['post', 'get'])
def moreinfo():
    if not session.get('logged_in'):
        return '''<script>alert('You Are Not Logged In Yet!');window.location="/l"</script>'''
    else:
        id = request.args.get('id')
        session['hid'] = id

        qry = "SELECT * FROM halls WHERE hid=%s"

        val = (id)
        res = selectone(qry, val)
        session['addid'] = res['addid']
        # return render_template("user-moreinfo.html", vall=res)
        return render_template("reservation.html", vall=res)


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
    return '''<script> alert('Your Message Sended Successfully');window.location="/contact"</script>'''
    # else:
    #     return '''<script> alert('error...! Check your internet connection');window.location="/contact"</script>'''



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
# add payment details to database by venue-admin
@app.route("/addpaydetials", methods=['post', 'get'])
def addpaydetials():
    upid = request.form['textfield1']
    qr = request.files['files']

    id=session['lid']
    qry1= "SELECT * FROM halls WHERE `addid`=%s"
    val=(id)
    res1=selectone(qry1,val)


    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    qr.save("static/images/payment/" + fn)
    
    qry = "INSERT INTO paymentd VALUES(%s,%s,%s,%s)"
    val = (id,res1['hid'],upid, fn)
    iud(qry, val)

    return '''<script> alert('Added ');window.location="/addpay"</script>'''


# ------------------------------------------------------------------------
# deleting user in admin panel
@app.route("/deleteUser", methods=['post', 'get'])
def deleteUser():
    id = request.args.get('ID')
    qry = "DELETE FROM `login` WHERE `lid`=%s"
    val = (id)
    iud(qry, val)
    qry = "DELETE FROM `signup` WHERE `lid`=%s"
    val = (id)
    iud(qry, val)

    return '''<script>alert("Deleted successfully.");window.location="/customerslist"</script>'''


# ------------------------------------------------------------------------
# date chech=king  foe venue in user side
@app.route("/venuecheck", methods=['post', 'get'])
def hallcheck():
    bdate = request.form['checkdate']
    qry = "SELECT date FROM bookings where date = %s"
    val = (bdate)
    res = selectone(qry, val)

    if res:
        return f'''<script> alert('This Date is NOT AVAILABLE');window.location.href="{request.referrer}"</script>'''
    else:
        return f'''<script> alert('In This Date is AVAILABLE');window.location.href="{request.referrer}"</script>'''


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

    message = Message("Mr/Ms: " + res['name'] + " This is the replay for your subject on: " + res[
        'subject'] + " REPLYAY :- " + replay, recipients=[res['email']])

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
# deleting venues in admin panel
@app.route("/deletevenue", methods=['post', 'get'])
def deletevenue():
    id = request.args.get('ID')
    qry = "DELETE FROM `halls` WHERE `hid`= %s"
    val = (id)
    iud(qry, val)
    return '''<script>alert("Deleted successfully.");window.location="/viewVenues"</script>'''


# ------------------------------------------------------------------------
# edit events in admin panel
# calling update function in admin panel
@app.route("/editevent", methods=['post', 'get'])  # edit button action in admin panel
def editevent():
    eventtype = request.form['text1']
    description = request.form['text2']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/event/" + fn)

    qry = "UPDATE `events` SET `eventtype`=%s,`description`=%s ,image=%s  where eventid=%s"
    val = (eventtype, description, fn, session['eventid'])
    res = iud(qry, val)
    return '''<script> alert('data Updated');window.location="/viewEvents"</script>'''

# ------------------------------------------------------------------------
# inserting event_customize details into databese 
@app.route("/insertcustomize", methods=['post', 'get'])
def insertcustomize():
    id = request.form['id']
    catering = request.form['catering']
    ac = request.form['ac']
    stage = request.form['stage']
    count = request.form['count']
    time = request.form['time']

    qry = "INSERT INTO customize VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val = (session['lid'], id, catering, ac, stage, count, time)
    res = iud(qry, val)
    return '''<script> alert('Successfully saved  Now! You Can Select Your Favorate Venue ');window.location="/allhalls"</script>'''


# ------------------------------------------------------------------------
# edit venues in admin panel
# calling update function in admin panel
@app.route("/editvenue", methods=['post', 'get'])  # edit button action in admin panel
def editvenue():
    location = request.form['textfield1']
    name = request.form['textfield2']
    bprice = request.form['textfield3']
    phone = request.form['textfield4']
    email = request.form['textfield5']
    decri = request.form['textfield7']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/venues/" + fn)

    qry = "UPDATE `halls` SET `location`=%s,`name`=%s ,bprice=%s ,phone=%s ,email=%s ,decri=%s ,image=%s   where hid=%s"
    val = (location, name, bprice, phone, fn, email, decri, session['hid'])
    iud(qry, val)
    return '''<script> alert('data Updated');window.location="/viewVenues"</script>'''


# ------------------------------------------------------------------------
# edit venues in admin panel
# calling update function in admin panel
@app.route("/updatevenue", methods=['post', 'get'])  # edit button action in admin panel
def updatevenue():
    location = request.form['textfield1']
    name = request.form['textfield2']
    bprice = request.form['textfield3']
    phone = request.form['textfield4']
    email = request.form['textfield5']
    # upi = request.form['textfield6']
    descri = request.form['textfield7']
    image = request.files['files']

    fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    image.save("static/images/venues/" + fn)

    qry = "UPDATE `halls` SET `location`=%s,`name`=%s ,bprice=%s ,phone=%s ,email=%s ,descri=%s ,image=%s   where lid=%s"
    val = (location, name, bprice, phone, email, descri, fn, session['lid'])
    iud(qry, val)
    return '''<script> alert('data Updated');window.location="/venueupdate"</script>'''


# ------------------------------------------------------------------------
# booking function
@app.route("/booking", methods=['post', 'get'])
def booking():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['mobile']
        email = request.form['email']
        add = request.form['add']
        place = request.form['place']
        date = request.form['date']

    # bdate = request.form['checkdate']
    qry = "SELECT date FROM bookings where date = %s"
    val = (date)
    res = selectone(qry, val)
    print(res)
    if res:
        return '''<script> alert('Alredy Booked By Someone !.\nchoose another date');window.location.href="/bookingdetails"</script>'''
    else:
        qry = "INSERT INTO bookings VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,'Pending',CURDATE())"
        val = (session['lid'],session['addid'],session['hid'],name,phone,add,email,place,date)
        iud(qry,val)
        return '''<script> alert('Succesfully booked');window.location="/bookingdetails"</script>'''
   
    # message="Thank you for booking our greate venue."
    # msg = Message("Hai" + name , recipients=[email])
    # msg.body = message
    # mail.send(msg)
# ------------------------------------------------------------------------
# calling thIS function to aprove booking in venue admin section
@app.route("/aprove", methods=['post', 'get'])
def aprove():
    id = request.args.get('ID')
    qry = "update bookings  set `status`='Aprove' where bkid=%s"
    val = (id)
    res=iud(qry,val)

    qry1 = "SELECT * FROM bookings WHERE bkid=%s"
    res1=selectone(qry1,val)



    #print(res1['cemail'])
    if res is None:
         return '''<script> alert('not APROVED');window.location="/venuebookings"</script>'''
    else:
        message=f"Your booking has been aproved. Thank you for everything  \n\nbooking id : { res1['bkid']}\nDate : { res1['date']}\n"
        msg = Message("Hai..."+res1['cname'] , recipients=[res1['cemail']])
        msg.body = message
        mail.send(msg)
        return '''<script> alert('APROVED');window.location="/venuebookings"</script>'''

# ------------------------------------------------------------------------
# calling thIS function to reject booking in venue admin section
@app.route("/reject", methods=['post', 'get'])
def reject():
    id = request.args.get('ID')

    qry = "update bookings  set `status`='Reject' where bkid=%s"
    val = (id)
    res=iud(qry,val)
    qry1 = "SELECT * FROM bookings WHERE bkid=%s"
    res1=selectone(qry1,val)


    if res is None:
     return '''<script> alert('not REJECTED');window.location="/venuebookings"</script>'''
    else:
     message=f"Your booking has been Rejected...!.\n\n If any enquery please contact this us......Thank you for everything"
     msg = Message("Hai..."+res1['cname'] , recipients=[res1['cemail']])
     msg.body = message
     mail.send(msg)
     return '''<script> alert('REJECTED');window.location="/venuebookings"</script>'''
# ------------------------------------------------------------------------
# show all the venue account in admin page
@app.route("/addvenueuser", methods=['post', 'get'])
def addvenueuser():
    
    qry = "select * FROM `login` WHERE `type`='venue'"
    res=selectall(qry)
    print(res)
    return render_template("Admin-adduser.html",val=res)

# ------------------------------------------------------------------------
# add venue user account and details in admin page
@app.route("/addvenueuseracc", methods=['post', 'get'])
def addvenueuseracc():
    if request.method == "POST":
        user = request.form['textfield1']
        passw = request.form['textfield2']
        type = request.form['textfield3']

    # message="Thank you for booking our greate venue."
    # msg = Message("Hai" + name , recipients=[email])
    # msg.body = message
    # mail.send(msg)

    qry = "INSERT INTO login VALUES(NULL,%s,%s,%s)"
    val = (user,passw,type)
    res = iud(qry,val)
    if res:
        return '''<script> alert('Added');window.location="/addvenueuser"</script>'''
    else:
        return '''<script> alert('Not Added!');window.location="/addvenueuser"</script>'''
# ------------------------------------------------------------------------
# edit venue account  in admin panel
# calling update function in admin panel
@app.route("/Edit", methods=['post', 'get'])  # edit button action in admin panel
def Edit():
    id = request.args.get('ID')
    user = request.form['textfield1']
    passw = request.form['textfield2']
    type = request.form['textfield3']

    qry = "UPDATE `login` SET `username`=%s,`password`=%s where lid=%s"
    val = (user,passw,id)
    res = iud(qry,val)
    if res:
        return '''<script> alert('data Updated');window.location="/addvenueuser"</script>'''
    else:
        return '''<script> alert('No data Updated!');window.location="/addvenueuser"</script>'''
 # ------------------------------------------------------------------------
# deleting venue account in admin panel
@app.route("/Delete", methods=['post', 'get'])
def Delete():
    id = request.args.get('ID')
    qry = "DELETE FROM `login` WHERE `lid`=%s"
    val = (id)
    iud(qry,val)
    

    return '''<script>alert("Deleted successfully.");window.location="/addvenueuser"</script>'''


# ------------------------------------------------------------------------
#action to change password
@app.route("/changepass", methods=['post', 'get'])
def changepass():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    id=session['lid']
    print(id)

    qry = "UPDATE login SET password=%s where `lid`=%s"
    val = (password,session['lid'])
    res=iud(qry, val)

    qry = "UPDATE `signup` SET `email`=%s where lid=%s"
    val = (email,session['lid'])
    iud(qry, val)
    # if res:
    return '''<script> alert('data Updated');window.location="/changepassw"</script>'''
    # else:
    #     return '''<script> alert('error');window.location="/changepassw"</script>'''
# ------------------------------------------------------------------------
# calling payment page in venue admin section
@app.route("/venuepayment", methods=['post', 'get'])
def venuepayment():
    qry = ""
    val = ()
    iud(qry,val)

    return render_template("venue_payments.html")
# ------------------------------------------------------------------------
@app.route("/show", methods=['post', 'get'])
def show():
    return render_template("Admin-update.html")

# ------------------------------------------------------------------------
# inserting UPI ref details into databese 
@app.route("/payconfirm", methods=['post', 'get'])
def payconfirm():
    
    id=session['lid']
    qry = "select * FROM `bookings` WHERE lid=%s"
    val1=(id)
    res1 = selectone(qry,val1)
    print(res1['venueid'])

    upi = request.form['upi']
    qry = "INSERT INTO payconfirm VALUES(%s,%s,%s,%s)"
    val = (res1['bkid'],session['lid'],res1['venueid'],upi)
    iud(qry, val)
    return '''<script> alert('Successfully Placed Your Order');window.location="/payment"</script>'''
# ------------------------------------------------------------------------
# show all the payments upi ref in venue-admin page
@app.route("/venueconfirm", methods=['post', 'get'])
def venueconfirm():
    
    id=session['lid']
    qry = "select * FROM `bookings` WHERE venueid=%s"
    res1 = selectall2(qry,id)
    qry = "select * FROM `payconfirm` WHERE addid=%s"
    res = selectall2(qry,id)

    return render_template("venue_confirm.html",val=res,val1=res1)










if __name__ == "__main__":
    app.run(debug=True)
