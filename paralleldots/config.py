import ConfigParser
def set_api_key(apikey):
    config = ConfigParser.RawConfigParser()
    config.add_section('PD')
    config.set('PD', 'exist', 'true')
    config.set('PD', 'api_key', str(apikey))
    with open('settings.cfg', 'wb') as configfile:
        config.write(configfile)


def get_api_key():
    config = ConfigParser.RawConfigParser()
    try:
        config.read('settings.cfg')
        if config.getboolean('PD', 'exist'):
            return config.get('PD', 'api_key')
    except:
        return None

