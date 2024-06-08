import yaml

from flask import Flask
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

app = Flask(__name__)

# Load credentials from the YAML file
with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)

# Extract RPC credentials and node IP
rpc_user = config['rpc']['user']
rpc_password = config['rpc']['password']
node_ip = config['rpc']['node_ip']

# Construct the URL for the RPC connection
rpc_url = f"http://{rpc_user}:{rpc_password}@{node_ip}:8332"

@app.route('/')
def hello():
	# Establish the connection
	try:
	    rpc_connection = AuthServiceProxy(rpc_url)
	    # Example call: get blockchain info
	    blockchain_info = rpc_connection.getblockchaininfo()
	    print(blockchain_info)
	except JSONRPCException as e:
	    print(f"An error occurred: {e}")
	except Exception as e:
	    print(f"Connection error: {e}")
	return blockchain_info

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
