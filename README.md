# jdfm

Joe's Dotfile Manager. Simple dotfile manager written in python that keeps all dotfiles and backups of them in one place.


# Installation

Download the `jdfm` file via curl, put it in your PATH (`~/bin` in my case), and make it executable

`curl "https://raw.githubusercontent.com/joeysnclr/jdfm/master/jdfm" --output ~/bin/jdfm`

`chmod +x ~/bin/jdfm`

# Uninstall

Remove the jdfm script, remove jdfm directory

`rm ~/bin/jdfm`

`rm -rf ~/dfm`

# Usage

### Help

displays help command

`jdfm help`

### Init

initializes jdfm with a ~/dfm directory in your home folder where it creates a config file and where it will store all of your dotfiles

this should be the first command you run

`jdfm init`

### Add file

creates a jdfm copy of the dotfile in the ~/dfm directory and adds the corresponding file to the config

`jdfm add {path-to-file}`

### Remove file

removes a file from the ~/dfm direcory and its config

`jdfm remove {name-of-file (not path)}`

### Update Dotfiles

writes all changed dotfiles in the ~/dfm directory to their corresponding locations on your system

`jdfm update`
