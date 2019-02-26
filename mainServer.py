from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

server = SimpleXMLRPCServer(("0.0.0.0", 8888))
client = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")
client2 = xmlrpc.client.ServerProxy("http://127.0.0.1:8887")


def buy(a):
    nilai, status = client.transaksi(a)
    if status == "success":
        trans = client2.histori(1, nilai)
        return trans
    else:
        return "transaksi gagal, saldo tidak cukup"


server.register_function(buy, "beli")
server.serve_forever()
