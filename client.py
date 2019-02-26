import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")

daftar,status = client.beli(10000)

try:
    if type(daftar) is list:
        print(status)
        for hasil in daftar:
            print(hasil)
    else:
        print(status,daftar)
except ValueError:
    print("Error...")
