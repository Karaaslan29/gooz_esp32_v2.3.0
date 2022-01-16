# Gooz Project for ESP32
This project aim is offering to use usely your Pico and getting power with own OS

# Basics

Basic gooz commands to use operating system like Linux.

```bash
list  # lists available functions

help  # gives fundeamental informations about Gooz

history  # shows past commands

print "data"  # prints "data" to terminal

shutdown  # shuts the system

clear  # clears the terminal screen

delay x  # delays the all programs as x second
```

## File Operations

```bash
pwd  # shows current path

ls  # shows files and directories in current directory

ls "path"  # shows files and directories in "path"

cd "directory"  # goes "directory" path

cd ..  # goes upper directory

mkdir "name"  # creates a directory named "name"

rm "name"  # deletes file named "name" in current directory 

rmdir "name"  # deletes directory named "name" in current directory 

cat "name" # reads file named "name" in current directory
```

## Edigooz Commands

```bash
edigooz run # opens the edigooz text editor

edigooz clean # cleans the text page

edigooz save "name" # saves the text page

edigooz cat "name" # shows the contents of the text page

edigooz ls # shows the saved text pages
```
