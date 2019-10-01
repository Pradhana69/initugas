import zerorpc
import paho.mqtt.client as mqtt

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:10000")

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/pulsa")

def on_message(client, userdata, msg):
	print("Message: " + msg.payload.decode())
	client.disconnect()

print ("Pilih Menu :")
print ("1. TopUp Saldo")
print ("2. Beli Pulsa")
pilih = input()
pilih = int(pilih)

if pilih == 1:
	print ("Masukkan Jumlah TopUp")
	amount = input()
	print ("Apakah sudah yakin ?")
	bool=input()
	if bool == "y" and "ya":
		print (c.topUp(int(amount)))
	else:
		print ("Terimaksaih")
		
if pilih == 2:
	print ("Masukkan Nomer HP")
	number = input()
	print ("Nama Operator")
	oper = input()
	print ("Jumlah pulsa")
	amount = input()
	print ("Apakah sudah yakin ?")
	bool=input()
	if bool == "y" and "ya":
		print (c.Pulsa(number, oper, int(amount)))
		mqtt_client = mqtt.Client()
		mqtt_client.connect("localhost", port=1883)
		mqtt_client.subscribe("/filkom/skt", qos=0)
		mqtt_client.on_connect = on_connect
		mqtt_client.on_message = on_message
		mqtt_client.loop_forever()
		mqtt_client.disconnect()
	else:
		print ("Terimaksaih")
