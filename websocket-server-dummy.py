#
# Simple websocket server that waits for connections from clients
# and then streams accelerometer readings from SenseHat sensor
# to the client.
#

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
##from sense_hat import SenseHat

class SimpleIMU(WebSocket):

    def handleMessage(self) :
        print ('incoming message')

    def handleConnected(self):
        print(self.address, 'connected')

    def handleMessage(self) :
        print ('incoming message')

    def handleClose(self):
        print(self.address, 'closed')


#
# program starts here
#

# Start server on port 9001
server = SimpleWebSocketServer('', 9001, SimpleIMU)
##sense = SenseHat()

while True :

    # x,y,z in 'g' units (range of x,y,z when not accelerating: -1 to 1 due to gravity)
    ##acceleration = sense.get_accelerometer_raw()
    acceleration = {"x": 12, "y": 10, "z": 13}
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    # display red ball on LED 8x8 matrix
    led_x = int(3+x*16+0.5)
    led_y = int(3+y*16+0.5)
    if (led_x < 0) :
        led_x = 0
    if (led_x > 7) :
        led_x = 7
    if (led_y < 0) :
        led_y = 0
    if (led_y > 7) :
        led_y = 7
    # clear all LEDs
    ##sense.clear()
    # set red pixel (red is RGB values 255,0,0)
    ##sense.set_pixel(int(led_x),int(led_y),255,0,0)

    # construct JSON message
    message = "\"x\":{}, \"y\":{}, \"z\":{}".format(x, y, z) 

    # broadcast accelerometer to all connected clients
    for client in server.connections.itervalues():
        if client.handshaked :
            print ('sending ', message , ' to ' , client.address[0])
            client.sendMessage(u'{' + str(message) + u'}')

    # call this once per main loop iteration for websocket server housekeeping
    server.serveonce()

