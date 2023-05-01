from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
severport = 8080
text_exp = 'Hello, World wide web!'

class my_sever(BaseHTTPRequestHandler):

    def do_POST(self):
        # c_len = int(self.headers.get('Content-Length'))
        # client_data = self.rfile.read(c_len)
        pass

    def do_GET(self):
        print(text_exp)
        self.send_response(200)

if __name__ == "__main__":
    webServer = HTTPServer((hostname, severport), my_sever)
    print("Server started http://%s:%s" % (hostname, severport))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print('STOP')