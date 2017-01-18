from NFCserver import *


def print_request(req: dict):
    # print("\n\n\n\n")
    # print(type(req))

    # print("parameters received by NFC reader:")

    # for cmd in sorted(req):
    #     print("\t", cmd, ":", req[cmd])
    return

NFCRequestHandler.subscribe(print_request)

start_server()