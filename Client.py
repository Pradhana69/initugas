import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:10000")
print ("Masukkan Nilai Top Up")
amount = input()
print ("Apakah sudah yakin ?")
bool=input()
if bool == "y":
	print (c.topUp(int(amount)))
else:
	print ("Ok!")