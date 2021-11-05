from flask import *
from ip_api import userIP

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #App route for Post and Get Methods
def index():
    # Lines-10-13 For HTML communication
    if request.method == 'POST':
        searchInput = request.form.get('search') # Gets the data from the search input 
        parsed_info = userIP(searchInput).json() # Calls the function userIP for API communication and store the data into a json format

        if 'error' in parsed_info: # Indicates any error encountered when parsing the information. These reasons are provided by the website itself.
            error = True
            reason = parsed_info['reason']
            ip_address = parsed_info['ip'] # Parsing specific data from the Json file gathered.
            return render_template('index_error.html', error=error, reason=reason, ip_address=ip_address) # Stores the information to be displayed in HTML.
            
        else: #If the parsed_info returns correct, it will display the selected data from the json.
            ip_version = parsed_info['version'] # Parsing specific data from the Json file gathered. Lines 19-27
            ip_address = parsed_info['ip']
            city = parsed_info['city']
            region = parsed_info['region']
            latitude = parsed_info['latitude']
            longitude = parsed_info['longitude']
            timezone = parsed_info['timezone']
            org = parsed_info['org']
            asn = parsed_info['asn']
            print(ip_address)
            return render_template('index.html', ip_address=ip_address, ip_version=ip_version, city=city, 
                                    region=region, latitude=latitude, longitude=longitude, timezone=timezone,
                                    org=org, asn=asn) #Uses the parsed data and sends it to HTML file for it to be displayed using Jinja.
    elif request.method == 'GET':
        return render_template('index.html') #If not POST, get will be called returning the regular empty index file.

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000)