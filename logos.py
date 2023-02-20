from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/logo/<company_name>')
def get_company_logo(company_name):
    # Step 1: Set UpLead API Key
    headers = {
        "Authorization": "bce217ccda0935d80b96a3368a31c9e5"
    }
    
    # Step 2: Search for Company
    search_url = "https://api.uplead.com/v2/company/search/"
    search_params = {
        "name": company_name,
        "limit": 1  # Limit to 1 result to avoid excessive API usage
    }
    search_response = requests.get(search_url, params=search_params, headers=headers)
    
    if search_response.status_code == 200:
        search_results = search_response.json()["results"]
        if len(search_results) == 0:
            return jsonify(error="No results found for company name"), 404
        company_id = search_results[0]["id"]
    else:
        return jsonify(error="Company search failed"), search_response.status_code
    
    # Step 3: Retrieve Company Details
    details_url = "https://api.uplead.com/v2/company/details/"
    details_params = {
        "id": company_id,
        "fields": "logo"
    }
    details_response = requests.get(details_url, params=details_params, headers=headers)
    
    if details_response.status_code == 200:
        logo_url = details_response.json()["logo"]
    else:
        return jsonify(error="Failed to fetch company details"), details_response.status_code
    
    # Step 4: Download Logo and Return Response
    logo_response = requests.get(logo_url)
    if logo_response.status_code == 200:
        return logo_response.content, 200, {'Content-Type': 'image/png'}
    else:
        return jsonify(error="Failed to download company logo"), logo_response.status_code
