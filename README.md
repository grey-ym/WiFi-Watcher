# WiFi SNMP Device Notifier
This Python script scans a WiFi network for a specific device using SNMP.
It performs a network check with the snmpwalk command and sends an SMTP email notification when the device is detected.

Requirements:
 · SNMP must be enabled on your router
 · SMTP is configured using Yahoo Mail (as an example)
 · Tested on D-Link DIR-843 router with custom ISP firmware (МТС)
