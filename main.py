from flask import Flask, request, jsonify
import ipaddress

app = Flask(__name__)

def get_client_ipv4_and_ipv6(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.version == 4:
            ipv4_address = str(ip_obj)
            ipv6_address = None
        elif ip_obj.version == 6:
            ipv4_address = str(ip_obj.ipv4_mapped)
            ipv6_address = str(ip_obj)
        else:
            ipv4_address = None
            ipv6_address = None
    except ValueError:
        ipv4_address = None
        ipv6_address = None
    
    return ipv4_address, ipv6_address

@app.route('/get-my-ip', methods=['GET'])
def get_my_ip():
    # Get the client's public IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Extract the IPv4 and IPv6 addresses
    ipv4_address, ipv6_address = get_client_ipv4_and_ipv6(client_ip)
    
    # Print both IPv4 and IPv6 addresses
    print(f'Client IPv4 Address: {ipv4_address}')
    print(f'Client IPv6 Address: {ipv6_address}')
    
    # Return only the IPv4 address to the client
    return jsonify({'Your Public IPv4 Address is': ipv4_address}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
