#!/bin/bash
# sudo pacman -S bc xorg-xrandr

x=$(cat $HOME/.config/settings/.b_log)

if (( $(echo "$x <= 0" | bc -l) )); then
	x=.10
fi

n=$(echo "$x - 0.05" | bc)

if (( $(echo "$n <= 0" | bc -l) )); then
	n=$x
fi

xrandr --output HDMI-2 --brightness $n
echo "$n" > $HOME/.config/settings/.b_log 
echo "#!/bin/bash
xrandr --output HDMI-2 --brightness $n" > $HOME/.config/settings/.b.sh
