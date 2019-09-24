import zerorpc
user = {
    "nama": "joko",
    "saldo": 50000
}
marketplace = {
    "nama":"Tokotokoan",
    "saldo": 5000000
}

class Bank(object):
    def transfer(self, amount):

    	user["saldo"] = user["saldo"] - amount
    	marketplace["saldo"] = marketplace["saldo"] + amount

    	return "Transfer sukses Rp. %s " % amount

s = zerorpc.Server(Bank())
s.bind("tcp://0.0.0.0:9999")
s.run()