from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("127.0.0.1", 8889))

currentSaldo = 100000

def transa(a):
    global currentSaldo
    if a < currentSaldo:
        currentSaldo -= a
        return currentSaldo, "success"
    else:
        return 0, "failed"


server.register_function(transa, "transaksi")
server.register_multicall_functions()
server.serve_forever()
