#connect to ftp
import ftplib
# import config config.cfg and include
# ftp_host, ftp_user, ftp_password
import configparser
config = configparser.ConfigParser()
config.read('config.cfg')

ftp_host = config['ftp']['ftp_host']
ftp_user = config['ftp']['ftp_user']
ftp_password = config['ftp']['ftp_password']
#connect to DB
ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user,ftp_password)
ftp.retrlines('LIST')
ftp.quit()
