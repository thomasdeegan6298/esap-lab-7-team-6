#
# This is a starting point for many of the tasks in Lab 6.
# The code here is not complete and contains a deliberate 
# 'bug' that you'll need to fix (pay attention to the lab
# instruction text because there is a hint there!).
#
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

htmls = "<html>"
htmls += "<body>"
htmls += "<h1>"
htmls += "Sensor Data:"
htmls += "</h1>"
htmls += "<p>"
htmls += "Temperature Reading: "
htmls += "</p>"
htmls += "<p>"
htmls += "Humidity Reading: "
htmls += "</p>"
htmls += "</body>"
htmls += "</htmls>"

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Write your response message here:
        self.wfile.write(htmls)
        
def run(server_class=HTTPServer, handler_class=S, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

