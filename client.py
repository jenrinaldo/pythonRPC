import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")

daftar = client.beli(1000)

if type(daftar) is list:
    for hasil in daftar:
        print(hasil)
else:
    print(daftar)
