from http.server import BaseHTTPRequestHandler, HTTPServer

class myServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<h1>Harsh Bhat </h1>".encode())
    def do_DELETE(self):
        # Extract the task ID from the URL
        task_id = self.path.split('/')[-1]
        print(f"Deleting task with ID: {task_id}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"Task {task_id} deleted successfully.".encode())
    def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            print("Received data:", data.decode())
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        print("Received data:", data.decode())
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
port = HTTPServer(('localhost', 5000), myServer)
print('Started')
port.serve_forever()
