from http.server import HTTPServer, BaseHTTPRequestHandler
import os.path


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path[:7] == '/?code=':
            code = self.path[7:-18]
            file = open('keys.py', 'w')
            file.write(code)
            file.close()
        else:
            pass


def run_server():
    httpd = HTTPServer(('localhost',8027),Serv)
    file_exists = os.path.exists('keys.py')
    while not file_exists:
        httpd.handle_request()
        file_exists = os.path.exists('keys.py')
