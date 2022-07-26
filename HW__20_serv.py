"""
Требуется написать сервер который будет отдавать текст при подключении клиента.
Сервер продолжает работу после обработки запроса.
К примеру можно взять дзен пайтона
Клиент должен при подключении получить текст, раcпечатать его на экране и завершить работу.
"""

import socketserver

HOST = '127.0.0.1'
PORT = 65432

with open('Zen_of_Python.txt', 'rb') as file:
    data = file.read()


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = data
        self.request.sendall(self.data)


if __name__ == "__main__":

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

