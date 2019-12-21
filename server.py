from websocket_server import WebsocketServer
from Q_A_main import queryAnswer
# Called for every client connecting (after handshake)
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    server.send_message(client, "robot: 您好，我是智能客服小龙人，请问有什么能帮助您的。您可输入您需要办理的业务，例如：银行卡开户。")


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
    print("Client(%d)_address%s said: %s" % (client['id'],client['address'], message))
    res = queryAnswer(message)
    msg = ''
    if res == None:
        msg = "对不起，小龙人暂时没有该功能呢"
    # 编辑距离为0，返回答案，否则返回相似问题，让用户确认答案
    if res[0][0] == 0:
        msg = res[0][2]
    else:
        msg = '请选择您需要办理的业务：'
        for qa in res:
            msg += '<br/>' + qa[1]
    server.send_message(client, "robot: " + msg)

print('server connecting...')
PORT=9001
server = WebsocketServer(PORT,host="127.0.0.1")
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()