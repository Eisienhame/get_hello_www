from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
severport = 8080
text_exp = 'Hello, World wide web!'

class my_sever(BaseHTTPRequestHandler):

    def do_POST(self):
        pass

    def do_GET(self):
        pass