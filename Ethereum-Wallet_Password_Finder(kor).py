import subprocess
import os
import itertools
import re



def setting_string():
	string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	print ("======================================================================\n문자열 : "+string)
	print ("======================================================================")
	answer = input("[*] 비밀번호 매칭에 사용할 문자열을 그대로 사용하시겠습니까?[y/n]")
	if answer == 'Y' or answer == 'y':
		return string
	elif answer == 'N' or answer == 'n':
		string = input("[*] 비밀번호 매칭에 사용할 문자열을 입력해주세요.\n[*] 문자열 입력 : ")
		return string
	else:
		print ("[*] 잘못된 값을 입력하였습니다.")
		setting_string()

		
		
def min_check():
	min_len = int(input("[*] 매칭 문자열 최소 길이 : "))
	if min_len <= 0:
		print ("[*] 최소 길이를 0보다 크게 설정해주세요.")
		min_len = min_check()
		return min_len
	else:
		return min_len

		
		
def max_check(min_len):
	max_len = int(input("[*] 매칭 문자열 최대 길이 : "))
	if max_len < min_len:
		print ("[*] 최대 길이를 최소 길이보다 크거나 같게 설정해주세요.")
		max_len = max_check(min_len)
		return max_len
	else:
		return max_len

		
		
def find_passwd(string, min_len, max_len, cmd_1):
	print ("[*] 비밀번호 추출 중...")
	for len in range(min_len, max_len+1):
		to_attempt = itertools.product(string, repeat = len)
		for attempt in to_attempt:
			passwd = ''.join(attempt)
			p = subprocess.Popen(cmd_1, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
			stdout = p.communicate(input=passwd.encode('utf-8'))
			print (">> 대입 문자열 : "+passwd)
			if bool(re.search('Please give a new password',str(stdout[0]))):
				print ("======================================================================\n[*] 비밀번호는 '"+passwd+"' 입니다.")
				return 1
			else:
				pass

				
				
if __name__ == "__main__":
	os.system('cls')
	print ("======================================================================")
	print ("##                                                                  ##")
	print ("##  Ethereum-Wallet Password Finder ver.1.0                         ##")
	print ("##                                            created by ninzacode  ##")
	print ("##                                                                  ##")
	print ("##   * date : 2016.05.10                                            ##")
	print ("##   * Wallet address : 0x6f5C338a68e1721309aD5b53c07B262F91Fd0c11  ##")
	print ("##                                                                  ##")
	print ("======================================================================")
	print ("[*] 해당 파일을 Ethereum-Wallet\\resources\\node\\geth에 위치시켜 주십시오.")
	address = input("[*] 지갑주소를 입력해주세요. : 0x")
	cmd_1 = "geth account update "+address
	
	string = setting_string()
	min_len = min_check()
	max_len = max_check(min_len)
	result = find_passwd(string, min_len, max_len, cmd_1)
	if result != 1: print ("[*] 비밀번호를 찾지 못했습니다. 대입할 문자열을 재설정하세요.")
	os.system('Pause')
	
	