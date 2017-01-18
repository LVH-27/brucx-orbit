from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from NFCresp import *

PORT_NUMBER = 80


# This class will handles any incoming request from
# the NFC reader. It doesn't respond to any requests
# sent by NFC reader as it already sends all required
# information

class NFCRequestHandler(BaseHTTPRequestHandler):
    subscribers = []

    def do_GET(self):
        # Handler for the GET requests

        req = NFCRequestHandler.parse_req(self.path) 
        # req contains a dictionary of the HTTP request sent by Orbit
        # its structure:
            # cmd = command being sent (CO for scan, PU for powerup, PG for ping etc)
            # date = self-explanatory
            # id = Orbit's IP address (by default: 192.168.7.200)
            # mac = Orbit's MAC address
            # md5 = MD5 hash of the whole request
            # time = hh:mm:ss
            # uid = NFC tag of the card read

        NFCRequestHandler.call_subscribers(req)
        #urllib.request.urlopen("http://tomcat.marinpetrunic.com/brucx-ws/swagger-ui.html#/students-controller")
        
        print("TEST TU SMO")
        cmd = req['cmd'][0]
        print ("CMD " + cmd)

        resp = ""

        if cmd == "CO":
            resp = do_CO(req)

        if cmd == "PG":
            resp = do_PG(req)

        print("OVO" + resp)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(str(resp), "utf-8"))
        #self.wfile.write(bytes("<html></head>", "utf-8"))

        #self.wfile.write(bytes("<body><ORBIT>\nLED1=2000\t", "utf-8"))
        #self.wfile.write(bytes("\nBEEP=1\t", "utf-8"))
        #self.wfile.write(bytes("\nLED=0\t", "utf-8"))

        #self.wfile.write(bytes("</ORBIT></body></html>", "utf-8"))

        



        #self.send_error(404, 'OK tnx') # <ORBIT>LED=1</ORBIT>

        return

    @staticmethod
    def parse_req(req: str):

        start = 0
        if "?" in req:
            start = req.find("?")

        result = urllib.parse.parse_qs(req[start+1::])
        return result

    @staticmethod
    def subscribe(method):
        # add a method to call when request is sent by NFC reader
        # parameter will be a single dict with NFC request commands

        NFCRequestHandler.subscribers.append(method)
        return

    @staticmethod
    def call_subscribers(cmd):
        for sub in NFCRequestHandler.subscribers:
            sub(cmd)
        return

    #def send_resp():



def start_server():
    try:
        # Create a web server and define the handler to manage the
        # incoming request
        server = HTTPServer(('', PORT_NUMBER), NFCRequestHandler)
        print('Started NFC reader http server on port ', PORT_NUMBER)

        # Wait forever for incoming http requests
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutting down server")
