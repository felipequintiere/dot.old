#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#export MANPAGER='nvim -u ~/.config/nvim/init.vim +Man!'
export MANPAGER='nvim +Man!'


PS1='[\u@\h \W]\$ '
#PS1='[$(pwd)]\$ '

alias py='python3'
alias p='python3'

#alias ls='ls -1 --color=auto'
alias ls='ls -lh --color=auto'

alias sl='ls --color=auto'
alias s='ls --color=auto'
alias l='ls -l --color=auto'
alias ll='ls -l --color=auto'
alias lla='ls -la --color=auto'
alias la='ls -a --color=auto'
alias al='ls -a --color=auto'

alias sclear='clear'
alias grep='grep --color=auto'

alias v='nvim'
alias vi='nvim'
alias vim='nvim'


#alias off='shutdown -P now'
alias off='systemctl poweroff'
alias net='bash ~/.config/settings/net.sh'

#alias anime='ani-cli -v --dub --rofi'
alias anime='ani-cli -v --dub'
alias x='startx'

#update books list
alias ubook='find $HOME -name "*.pdf" > $HOME/.config/settings/.dmenu_books_log'
