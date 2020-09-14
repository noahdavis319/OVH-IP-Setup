
import sys
from string import Template

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print("\nNot enough arguments.")
		print("Need interface name, ip address, and gateway address.\n")
		sys.exit(1)

	interface = sys.argv[1]
	ip_addr = sys.argv[2]
	gateway = sys.argv[3]

	data = ''
	with open('ovh-network-template.yaml', 'r') as tmplt:
		data = tmplt.read()

	data = Template(data)
	data = data.substitute(interface=interface, ip_addr=ip_addr, gateway=gateway)
	print(data)
