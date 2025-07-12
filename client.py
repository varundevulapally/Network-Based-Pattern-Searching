import socket
import json

# Set up the client socket
c1 = socket.socket()

host = "127.0.0.1"
port = 5500

c1.connect((host, port))

# Get filename and word to search from the user
filename = "elements.txt"
word = input("Enter the word to search: ")

# Prepare the data to send to the server
request = json.dumps({"filename": filename, "word": word})
c1.send(request.encode())

# Receive the result from the server
response = c1.recv(1024).decode()
result = json.loads(response)

if "error" in result:
    print(f"Error: {result['error']}")
else:
    formated_result = f'["{result[0]}",' + ','.join(f'({item[0]},"{item[1]}")' for item in result[1:])+']'
    print("Search Results:")
    print(formated_result)  # Directly print the result list received from the server

# Close the client connection
c1.close()
