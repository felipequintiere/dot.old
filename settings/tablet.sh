#!/bin/bash

# https://wiki.archlinux.org/title/Graphics_tablet
# sudo pacman -S xf86-input-wacom
# sudo pacman -S usbutils
# sudo pacman -S xorg-xev

# lsusb
# xsetwacom list devices
# xev -event button


# $ lsusb
# Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 001 Device 002: ID 256c:006d  
# Bus 001 Device 003: ID 1c4f:0002 SiGma Micro Keyboard TRACER Gamma Ivory
# Bus 001 Device 004: ID 046d:c077 Logitech, Inc. Mouse
# Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub


# create a file in /etc/X11/xorg.conf.d, where VID:PID is your USB ID as seen by lsusb
# $ sudo  touch /etc/X11/xorg.conf.d/10-tablet.conf
# $ cat /etc/X11/xorg.conf.d/10-tablet.conf
# Section "InputClass"
#     Identifier "Tablet"
#     Driver "wacom"
#     MatchDevicePath "/dev/input/event*"
#     MatchUSBID "VID:PID" #in this case, VID:PID = 256c:006d
# EndSection


### 1
# [arch@archlinux .settings]$ xsetwacom list devices
# HID 256c:006d stylus            	id: 10	type: STYLUS    
# HID 256c:006d eraser            	id: 14	type: ERASER    
# OpenTabletDriver Virtual Artist Tablet stylus	id: 16	type: STYLUS    
# OpenTabletDriver Virtual Artist Tablet eraser	id: 17	type: ERASER    
#
# //HID 256c:006d Touch Strip pad   	id: 9	type: PAD
# //HID 256c:006d Dial pad          	id: 10	type: PAD
# //HID 256c:006d Pen stylus        	id: 11	type: STYLUS
# //HID 256c:006d Pad pad           	id: 12	type: PAD

### 2 (example: identify the pen's buttons  
# [arch@archlinux ~]$ xev -event button
# Outer window is 0x1800001, inner window is 0x1800002
#
# ButtonPress event, serial 25, synthetic NO, window 0x1800001,
#     root 0x3d6, subw 0x1800002, time 220414, (41,42), root:(1005,75),
#     state 0x0, button 2, same_screen YES
#
# ButtonRelease event, serial 25, synthetic NO, window 0x1800001,
#     root 0x3d6, subw 0x1800002, time 220578, (44,43), root:(1008,76),
#     state 0x200, button 2, same_screen YES
# ^C

# 10 is the id seen on the output of xsetwacom list devices, it is the id of the:
# HID 256c:006d stylus            	id: 10	type: STYLUS 
xsetwacom set 10 Button 2 "key +ctrl +Shift p -Shift -ctrl"
xsetwacom set 10 Button 3 "key +ctrl +Shift e -Shift -ctrl"

# 10 is the id  seen on the output of xsetwacom list devices, it is the id of the:
# HID 256c:006d stylus            	id: 10	type: STYLUS    
xsetwacom set 10 Area 0 0 32000 18000

# 16 is the id seem on the output of xsetwacom list devices, it is the id of the:
# OpenTabletDriver Virtual Artist Tablet stylus	id: 16	type: STYLUS    

xsetwacom set 16 Button 1 "key +ctrl +Shift + -Shift -ctrl"
xsetwacom set 16 Button 2 "key +ctrl - -ctrl"
xsetwacom set 16 Button 3 "key +ctrl +Shift a -Shift -ctrl"
xsetwacom set 16 Button 8 "key +ctrl +Shift g -Shift -ctrl"
xsetwacom set 16 Button 9 "key +ctrl +Shift z -Shift -ctrl"
xsetwacom set 16 Button 10 "key +ctrl z -ctrl"
