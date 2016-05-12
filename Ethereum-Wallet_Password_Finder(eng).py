import subprocess
import os
import itertools
import re



def setting_string():
	string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	print ("=======================================================================\nDefault : "+string)
	print ("=======================================================================")
	answer = input("[*] Would you like to use this default?[y/n]")
	if answer == 'Y' or answer == 'y':
		return string
	elif answer == 'N' or answer == 'n':
		string = input("[*] Please enter the string to use for the matching password.\n[*] Set String : ")
		return string
	else:
		print ("[*] incorrect value!")
		setting_string()

		
		
def min_check():
	min_len = int(input("[*] Please enter the minimum length of the string. : "))
	if min_len <= 0:
		print ("[*] Please enter a minimum length greater than 0.")
		min_len = min_check()
		return min_len
	else:
		return min_len

		
		
def max_check(min_len):
	max_len = int(input("[*] Please enter the maximum length of the string. : "))
	if max_len < min_len:
		print ("[*] Please enter a maximum length equal to or greater than the minimum length.")
		max_len = max_check(min_len)
		return max_len
	else:
		return max_len

		
		
def find_passwd(string, min_len, max_len, cmd_1):
	print ("[*] Extracting password...")
	for len in range(min_len, max_len+1):
		to_attempt = itertools.product(string, repeat = len)
		for attempt in to_attempt:
			passwd = ''.join(attempt)
			p = subprocess.Popen(cmd_1, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
			stdout = p.communicate(input=passwd.encode('utf-8'))
			print (">> Trying to match : "+passwd)
			if bool(re.search('Please give a new password',str(stdout[0]))):
				print ("======================================================================\n[*] Congratulations! The password is '"+passwd+"'.\n")
				print ("[*] If you would like to donate to the developers, please use the address below.[*] ninzacode's address : 0x6f5C338a68e1721309aD5b53c07B262F91Fd0c11")
				print ("======================================================================\n")
				return 1
			else:
				pass

				
				
if __name__ == "__main__":
	os.system('cls')
	print ("=======================================================================")
	print ("##                                                                   ##")
	print ("##  Ethereum-Wallet Password Finder ver.1.0                          ##")
	print ("##                                            created by ninzacode   ##")
	print ("##                                                                   ##")
	print ("##   * date : 2016.05.10                                             ##")
	print ("##   * Wallet address : 0x6f5C338a68e1721309aD5b53c07B262F91Fd0c11   ##")
	print ("##                                                                   ##")
	print ("=======================================================================")
	address = input("[*] Please enter your wallet address. \n : 0x")
	cmd_1 = "geth account update "+address
	
	string = setting_string()
	min_len = min_check()
	max_len = max_check(min_len)
	result = find_passwd(string, min_len, max_len, cmd_1)
	if result != 1: print ("[*] Can't find your password. Please try again.")
	os.system('Pause')
	
	