from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
severport = 8080
text_exp = 'Hello, World wide web!'

class my_sever(BaseHTTPRequestHandler):

    def do_POST(self):
        pass

    def do_GET(self):
        self.send_response(200, text_exp)

if __name__ == "__main__":
    webServer = HTTPServer((hostname, severport), my_sever)
    print('START')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print('STOP')