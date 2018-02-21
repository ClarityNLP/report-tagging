import configparser

config = configparser.RawConfigParser()
config.read('./config.cfg')

conn_string = "host='%s' dbname='%s' user='%s' password='%s' port=%s" % (config.get('pg', 'host'),
                                                                         config.get('pg', 'dbname'),
                                                                         config.get('pg', 'user'),
                                                                         config.get('pg', 'password'),
                                                                         str(config.get('pg', 'port')))
