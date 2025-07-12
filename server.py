import socket
import threading
import json
from search import Search

class MyThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        try:
            # Receive request from client 
            request = self.client.recv(1024).decode()
            data = json.loads(request)
            filename = data.get("filename")
            word = data.get("word")

            # Use Search class to search for the word in the file
            search_instance = Search(filename)
            search_instance.clean()
            lines = search_instance.getLines(word)

            # Send the result back to the client
            response = json.dumps(lines)
            self.client.send(response.encode())

        except Exception as e:
            error_message = json.dumps({"error": str(e)})
            self.client.send(error_message.encode())

        finally:
            # Close the client connection
            self.client.close()

# Set up the server socket
s1 = socket.socket()

host = "127.0.0.1"
port = 5500

s1.bind((host, port))
s1.listen(5)



while True:
    # Accept incoming client connections
    client, addr = s1.accept()
    
    
    # Start a new thread to handle the client
    t1 = MyThread(client)
    t1.start()