def do_CO(req: dict):
	print("")
	print("")
	print("Opa, kartica!")
	uid = req['uid'][0]
	print("NFC tag read: " + uid)
	
	resp = "<html>\n<body>\n<ORBIT>\n"

	for student in dbmock:
		if student["nfcId"] == uid:
			print("NFC tag found in the database!")
			if student["tickets"]:
				print("Student has a ticket!")
				if student["tickets"]["used"] == 0:
					resp += "LED3=2000\n"
					resp += "BEEP=1\n"
					student["tickets"]["used"] = 1
					print("Ticket set as used!\n")
				else:
					resp += "LED1=2000\n"
					resp += "BEEP=0\n"
					print("Ticket already used!\n")
			else:
				resp += "LED2=2000\n"
				print("Student has no ticket!\n")
			break
		else:
			resp += "LED2=2000\nBEEP=1\n"
			print("NFC tag not found!\n")

	resp += "</ORBIT>\n</body>\n</html>"

	return resp


def do_PG(req: dict):
	print("")
	print("")
	print("")
	print("Ping!")
	resp = "<html>\n<body>\n<ORBIT>\n"
	resp += "LED3=1000\n"
	resp += "</ORBIT>\n</body>\n</html>"
	#print(resp)
	print("")
	print("")
	return resp

dbmock = [{"jmbag":"0036478030","nfcId":"AF17400B","name":"Leonard","surname":"Volari? Horvat","email":"leonard.volaric-horvat@fer.hr","image":"","tickets":{"used":0},"freshmen":False}]