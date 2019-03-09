from simple_websocket_server import WebSocketServer, WebSocket


class WS(WebSocket):
    def handle(self):
        print("data: ", self.data) # handle data here
        # broadcast
        for client in clients:
            if client != self:
                client.send_message(str(self.address) + u'->\n' + self.data)

    def connected(self):
        print(self.address, 'connected')
        for client in clients:
            client.send_message(str(self.address) + u' - connected')
        clients.append(self)

    def handle_close(self):
        clients.remove(self)
        print(self.address, 'closed')
        for client in clients:
            client.send_message(str(self.address) + u' - disconnected')


clients = []

server = WebSocketServer('', 8000, WS)
server.serve_forever()