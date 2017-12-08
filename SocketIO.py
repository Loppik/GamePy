from socketIO_client_nexus import SocketIO, LoggingNamespace

from events.EventFieldClick import EventFieldClick

class Socket:
    field = 0

    @staticmethod
    def on_connect():
        print('connect')

    @staticmethod
    def on_disconnect():
        print('disconnect')

    @staticmethod
    def onMessage(msg):
        try:
            creature = msg.get('creature')
            cellNumber = msg.get('cellNumber')
            print(creature + " cell " + str(cellNumber))
            cell = Socket.field.cells.getElement(cellNumber)
            EventFieldClick.moveCreatureInOtherPos(Socket.field.field, creature, cell)
            #print("creature1: " + str(Main.creature1Cell) + ",creature2: " + str(Main.creature2Cell))
        except(Exception):
            pass
            # print(msg)

    @staticmethod
    def on_aaa_response(*args):
        print('on_aaa_response', args)

    def __init__(self, port, field):
        self.__port = port
        self.field = field
        self.__socket = SocketIO('localhost', port, LoggingNamespace)

    def socketOn(self):
        self.socket.on('connection', Socket.on_connect)
        self.socket.on('message', Socket.onMessage)
        self.socket.on('disconnect', Socket.on_disconnect)
        self.socket.on('aaa_response', Socket.on_aaa_response)

    def emit(self, creature, cellNumber, field):
        print("-")
        Socket.field = field
        self.socket.emit('message', creature, cellNumber)
        self.socket.wait(seconds=1)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def socket(self):
        return self.__socket

    @socket.setter
    def socket(self, socket):
        self.__socket = socket