#Author: Sudeep Reddy Dodda
"""
	Description: This python script searches for nearby Bluetooth LE devices that are advertising and displays device MAC address, rssi and advertising data
				 within a fixed scanning time.
"""

from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev:
			print "Discovered device", dev.addr
		elif isNewData:
			print "Receiver new data from: ", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
	print "Device %s (%s), RSSI = %d dB" %(dev.addr, dev.addrType, dev.rssi)
	for (adtype, desc, value) in dev.getScanData():
		print "  %s = %s" %(desc, value)	
