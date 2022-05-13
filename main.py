import logging

from http_server import PCControllerHTTPServer

logging.basicConfig(level=logging.DEBUG)

BINDING_ADDRESS = ('127.0.0.1', 8080)


def main():
    server = PCControllerHTTPServer(BINDING_ADDRESS)
    server.serve()


if __name__ == '__main__':
    main()
