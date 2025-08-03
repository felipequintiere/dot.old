#!/bin/bash
#sudo pacman -S bc xorg-xrandr

x=$(cat $HOME/.config/settings/.b_log)
n=$(echo "$x + 0.05" | bc)

xrandr --output HDMI-2 --brightness $n
echo "$n" > $HOME/.config/settings/.b_log 
echo "#!/bin/bash
xrandr --output HDMI-2 --brightness $n" > $HOME/.config/settings/.b.sh
