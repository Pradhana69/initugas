import zerorpc
user = {
    "nama": "Satya",
    "saldo": 150000
}
marketplace = {
    "nama":"TokoJualPulsa",
    "saldo": 15000000
}

class Bank(object):
    def transfer(self, amount):

    	user["saldo"] = user["saldo"] - amount
    	marketplace["saldo"] = marketplace["saldo"] + amount

    	return "Transfer sukses Rp. %s " % amount

s = zerorpc.Server(Bank())
s.bind("tcp://0.0.0.0:9999")
s.run()