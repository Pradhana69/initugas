import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9999")

saldoAwal = 0

class Marketplace(object):
    def topUp(self, amount):
        print (c.transfer(amount))
        global saldoAwal
        saldoAwal = saldoAwal + amount
        return "TopUp berhasil ditambahkan Rp. %s" % saldoAwal

s = zerorpc.Server(Marketplace())
s.bind("tcp://0.0.0.0:10000")
s.run()