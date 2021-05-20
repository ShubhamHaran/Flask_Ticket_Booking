import requests
from twilio.rest import Client
from flask import Flask,render_template,request
account_sid="AC71eb58f97103ff4c4897284a08ec45c5"
auth_token="6a4cc8468b36d1f4bbf352fc83129ca0"
client=Client(account_sid,auth_token)
app=Flask(__name__)
@app.route('/')
def registration_form():
    return render_template('test_page.html')
@app.route('/login_page',methods=['POST','GET'])
def login_registration_dtls():
    fname=request.form['fname']
    lname=request.form['lname']
    email=request.form['email']
    source_st=request.form['source_st']
    source_dt=request.form['source_dt']
    destination_st=request.form['destination_st']
    destination_dt=request.form['destination_dt']
    phno=request.form['phno']
    id_proof=request.form['id_proof']
    date=request.form['date']
    full_name=fname+" "+lname
    r=requests.get('https://api.covid19india.org/v4/data.json')
    json_data=r.json()
    cnt=json_data[destination_st]['districts'][destination_dt]['total']['confirmed']
    pop=json_data[destination_st]['districts'][destination_dt]['meta']['population']
    travel_pass=((cnt/pop)*100)
    if(travel_pass<30 and request.method=='POST'):
        status='CONFIRMED'
        greeting='Thank you!'
    else:
        status='NOT CONFIRMED'
        greeting='Try again later! Stay Safe!'
    bdy='HELLO! '+full_name+" your travel booking from "+source_dt+" to "+destination_dt+" has been "+status+" "+greeting
    client.messages.create(to="whatsapp:+918500221155",
                           from_="whatsapp:+14155238886",
                           body=bdy)
    return render_template('user_registration_details.html',var1=full_name,var2=email,var3=phno,var4=source_st,var5=id_proof,var6=date,var7=destination_st,var8=source_dt,var9=destination_dt,var10=status)
if __name__=="__main__":
    app.run(port=8801,debug=True)


