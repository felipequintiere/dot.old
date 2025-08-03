#!/bin/bash

bash ~/.config/settings/monitor.sh
bash ~/.config/settings/.b.sh
bash ~/.config/settings/screensaver.sh

bash ~/.config/settings/mouse.sh
bash ~/.config/settings/keyboard.sh
bash /usr/bin/otd-daemon &
#bash ~/.config/settings/tablet.sh

picom -f &
bash ~/.fehbg &
