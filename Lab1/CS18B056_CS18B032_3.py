#use python3
from pwn import *

io = process('./CS18B056_CS18B032_3')

print(io.recvline())
print(io.recvline())

while(1):

	print(io.recvline())
	io.sendline("100")
	print(io.recvline())
	print(io.recvline())

