import sys

if ( sys.version_info > (3, 0) ):   # For Python 3
	import configparser as cp
else:                               # For Python 2
	import ConfigParser as cp

def set_api_key( apikey ):
	config = cp.RawConfigParser()
	config.add_section('PD')
	config.set('PD', 'exist', 'true')
	config.set('PD', 'api_key', str(apikey))
	with open('settings.cfg', 'w') as configfile:
		config.write(configfile)


def get_api_key():
	config = cp.RawConfigParser()
	try:
		config.read('settings.cfg')
		if config.getboolean('PD', 'exist'):
			return config.get('PD', 'api_key')
	except:
		return None