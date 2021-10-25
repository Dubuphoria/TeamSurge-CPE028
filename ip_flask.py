from flask import *
from ip_api import userIP

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        searchInput = request.form.get('search')
        parsed_info = userIP(searchInput).json()
        if 'error' in parsed_info:
            error = True
            reason = parsed_info['reason']
            ip_address = parsed_info['ip']
            return render_template('index_error.html', error=error, reason=reason, ip_address=ip_address)
        else:
            ip_version = parsed_info['version']
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
                                    region=region, latitude=latitude, longitude=longitude, timezone=timezone, org=org, asn=asn)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)