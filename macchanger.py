import subprocess
import optparse

def macchange(interface,mac):
	print("[+] changing " + interface + " to " + mac)
	subprocess.call(["ifconfig", interface , "down"])
	subprocess.call(["ifconfig", interface , "hw" , "ether" , mac])
	subprocess.call(["ifconfig", interface , "up"])

def parsr():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help ="interface to change its 	maccadress")
	parser.add_option("-m", "--mac", dest="mac", help ="new maccadress") 
	return parser.parse_args()

(options,argument) = parsr()
macchange(options.interface,options.mac)
