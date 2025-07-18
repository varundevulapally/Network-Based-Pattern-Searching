# Network-Based-Pattern-Searching
Network-Based Pattern Searching

This project demonstrates a client-server network application where a client sends a request to a multithreaded server to search for a specific word or pattern in a text file. The server processes the request, searches for the pattern, and sends the results back to the client.


---

Project Structure

The project contains the following files:

1. search.py:
Implements the Search class with methods to read, clean, and search for patterns in a file.


2. server.py:
Implements a multithreaded server that listens for client connections, processes search requests, and sends the results back.


3. client.py:
Implements the client application that connects to the server, sends search requests, and displays results.


4. elements.txt:
A sample text file used for testing the pattern search functionality.




---

Features

Multithreaded Server: Handles multiple clients simultaneously.

Pattern Searching: Uses regular expressions to search for words or patterns in a file.

Error Handling: Handles file not found and word not found errors gracefully.

JSON Communication: Uses JSON for communication between the client and server.



---

How to Run

1. Start the Server

1. Open a terminal and navigate to the directory containing server.py.


2. Run the server using the command:

python server.py


3. The server will start and listen for client connections on 127.0.0.1:5656.



2. Run the Client

1. Open another terminal and navigate to the directory containing client.py.


2. Run the client using the command:

python client.py


3. Enter the word you want to search for when prompted.




---

Input Format

Client Request:
The client sends a JSON object containing:

{
  "filename": "elements.txt",
  "word": "land"
}

Server Response:
The server responds with either:

A JSON object containing the list of line numbers and lines where the word is found.

An error message in case of issues (e.g., file not found, word not found).




---

Example

Sample Input

Word to search: Artificial


Sample Output

Enter the word to search: 
Search Results:
["Artificial",(1,"Artificial Intelligence is a new technology in the field of computer science"),(2,"Artificial means manmade that is not natural and Intelligence refers to the ability to think and make decisions"),(3,"Therefore we can say that making machines like computers to take their own decisions is Artificial Intelligence")]

---

Dependencies

Python 3.x

JSON module (standard library)

socket module (standard library)

threading module (standard library)
