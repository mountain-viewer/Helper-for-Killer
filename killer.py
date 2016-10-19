from login import create_session

# Authentication
def get_username():
	print 'Enter the username:'
	return raw_input()

def get_password():
	print 'Enter the password:'
	return raw_input()
	
# Web address format
auth_address = 'http://2ka.fizteh.ru/accounts/login/?next=/'
profile_format = 'http://2ka.fizteh.ru/accounts/profile/%d/'
home_address = 'http://2ka.fizteh.ru/'

def main():
  username = get_username()
  password = get_password()
  
  with open('result.txt', 'w') as file:
    result = create_session(auth_address, username, password, home_address, profile_format)
    file.write('\n'.join('%s | %s | %s | %s | %s' % elem for elem in result))

if __name__ == '__main__':
	main()
