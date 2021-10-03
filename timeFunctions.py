from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct
import time


def getNTPTimeLocal(host="pool.ntp.org"):
	port = 123
	buf = 1024
	address = (host, port)
	msg = '\x1b' + 47 * '\0'

	# TEMPO AO INICIAR
	requestTime = time.time()
	# TEMPO AO ENCERRAR
	responseTime = time.time()
	difTime = responseTime - requestTime

	# tempo de referência (em segundos desde 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00

	# conectar ao servidor
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg.encode('utf-8'), address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970 + (difTime * 2)
	return time.ctime(t).replace("  ", " ")



