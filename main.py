from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import sqlite3
from get_mail import get_topN_mails
from gpt_api import gpt_api

app = Flask(__name__)

print("Applications table created successfully")

@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    
    conn = sqlite3.connect('./db.sqlite3')
    print("Opened database successfully")
    data = request.get_json()
    email = data['email']
    name = data['name']
    password = data['password']
    
    try:
        conn.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, name, password))
        conn.commit()
        response = jsonify({'message': 'Registration successful.','email':email,'name':name}), 201
        return response
    except sqlite3.IntegrityError as e:
         response = jsonify({'error': 'User with this email already exists.'}), 400
         return response

@app.route('/login', methods=['POST'])
@cross_origin()
def login(): 
    conn = sqlite3.connect('./db.sqlite3')
    print("Opened database successfully")
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    cursor = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    print(user)
    
    if user:
        response = jsonify({'message': 'Login successful.','email':email,'name':user[2]}), 200
        return response
    else:
        response = jsonify({'error': 'Invalid email or password.'}), 401
        return response
    
@app.route('/get_applications', methods=['POST'])
@cross_origin()
def get_applications():
    processed_email=gpt_api()
    email = request.json['email']
    conn = sqlite3.connect('./db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT userid FROM users WHERE email=?', (email,))
    result = c.fetchone()
    
    if not result:
        response = jsonify({'error': 'User not found'}), 404
        return response
    
    userid = result[0]
    c.execute("SELECT * FROM applications WHERE company_name=? AND position_name=?", (processed_email["Company"].split(":")[-1][1:], processed_email["Job Position"].split(":")[-1][1:]))
    current_data = c.fetchone()
    print("current_data",current_data)



    if not current_data:
        print("no data foud")
        c.execute('SELECT company_name, position_name, status, content FROM applications WHERE userid=?', (userid,))
        length=len(c.fetchall())
        print( (processed_email["Company"].split(":")[-1][1:],processed_email["Job Position"].split(":")[-1][1:],processed_email["Status"].split(":")[-1],userid,""))
        c.execute("INSERT INTO applications (email_code,company_name, position_name, status,userid,content) VALUES (?,?,?,?,?,?)",(str(length+11),processed_email["Company"].split(":")[-1][1:],processed_email["Job Position"].split(":")[-1],processed_email["Status"].split(":")[-1],userid,""))
        conn.commit()
    
        c.execute('SELECT company_name, position_name, status, content FROM applications WHERE userid=?', (userid,))
    applications = c.fetchall()
    data_list=[
{
    "title": "Applied",
    "data": [],
  },
  {
    "title": "Online Assessment",
    "data": [],
  },
  {
    "title": "Interview",
    "data": [],
  },
  {
    "title": "Rejected",
    "data": [],
  },
]
    for a in applications:
        if a[2]=="Applied" or a[2]=="Accepted" or a[2]==" Accepted":
            data_list[0]['data'].append(a)
        elif a[2]=="Interview" or a[2]==" Interview call":
            data_list[2]["data"].append(a)
        elif a[2]=="Online Assesment":
            data_list[1]["data"].append(a)
        elif a[2]=="Rejected" or  a[2]==" Rejected":
            data_list[3]["data"].append(a)

    conn.close()
    
    response = jsonify({'applications': data_list   })
    return response

# UpLead API endpoint
API_URL = 'https://api.uplead.com/v2/company-name-to-domain'

# UpLead API access key
API_ACCESS_KEY = 'bce217ccda0935d80b96a3368a31c9e5'

@app.route('/logo', methods=['POST'])
@cross_origin()
def get_logo():
    # Get the company name from the POST request
    company_name = request.json['company_name']

    # Make a request to the UpLead API to get company data
    response = requests.post(API_URL, json={
        'access_key': API_ACCESS_KEY,
        "company_name": company_name
    })
    print(response)
    # Check if the request was successful
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch company data'}), 500

    # Extract the logo from the response
    data = response.json()
    logo_url = data['data'][0]['logo']

    # Return the logo URL as a JSON response
    return jsonify({'logo_url': logo_url})

if __name__ == '__main__':
    app.run(debug=True)
