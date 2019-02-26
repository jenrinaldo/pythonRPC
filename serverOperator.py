from xmlrpc.server import SimpleXMLRPCServer
import datetime

server = SimpleXMLRPCServer(("127.0.0.1", 8887))
daftTransaksi = ["Waktu               Nilai Transaksi"]
lasId = 1


def histori(id, nominal):
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    currentDT = str(currentDT)
    nominal = str(nominal)
    if lasId == id:
        strTotal = currentDT+" "+nominal
        daftTransaksi.append(strTotal)
    else:
        daftTransaksi.clear()
    return daftTransaksi


server.register_function(histori,"histori")
server.register_multicall_functions()
server.serve_forever()
