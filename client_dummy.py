from gevent.socket import create_connection

ws = create_connection("ws://localhost:1443/websocket")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Reeiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()
