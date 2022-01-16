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

# GPIO

Commands for GPIO settings

## Pin Registering

```bash
pin var gpio –name=() –type=() –mode=() –pin=()
```

### Parameters

```bash
-name=()  # takes pin name
-name=(My_Pin)
```

```bash
-type=()  # takes pin type

-type=(in)
-type=(out)
-type=(alt)
-type=(opendrain)
-type=(altopendrain)
```

```bash
-mode=()  # takes mode of pin

-mode=(pullup)
-mode=(pulldown)
```

```bash
-pin=()  # takes pin number

-pin=(12)
```

## Using GPIO Pins

```bash
pin gpio write "name" HIGH  # applies HIGH voltage to pin named "name"

pin gpio write "name" LOW  # applies LOW voltage to pin named "name"
```

```bash
pin gpio read "name"  # reads the digital value of pin named "name"
```

```python
pin gpio del "name" # deletes the gpio pin of pin named "name"
pin gpio delete "name" 
```
<br/>

# ADC

Commands for ADC pins.

## Pin Registering

```bash
pin var adc -name=() -pin=()
```

## Parameters

```bash
-name() # takes pin name
-name(myAdc) #new adc pin name is myAdc
```

```bash
-pin() # takes pin number
-pin(32) # sets new adc pin on 32
```

## Using ADC Pins

```bash
pin adc read $name # Read and print ADC pin value
                   # Value between 0-4095

pin adc read $name $x #Read and print ADC pin value x times

pin adc listen $name # Read data with 1 second interval until it stops
pin adc listen stop # Stop listening data

pin adc del $name # Deletes the ADC pin of pin named "name" 
pin adc delete $name
```
