#!/bin/bash

if ! pgrep -f "alacritty.*--class dropdown";then
	alacritty --class dropdown &
fi
