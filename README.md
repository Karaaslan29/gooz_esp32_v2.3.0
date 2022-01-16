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

# WiFi

Wifi library helps to connect any hotspot wifis

## Activating & deactivating wifi

```bash
wifi on
wifi off
```

## Finding available wifis

```bash
wifi ls
```

## Connecting wifi

```bash
wifi connect "wifi_name" "wifi_password"
```

## Disconnecting wifi

```bash
wifi disconnect
```

## Active wifi connection status

```bash
wifi status # shows network connection

ifconfig  # shows detailed network connection informations
```
# Package Installer

## Package Install

```bash
pkg install [PACKAGE_NAME]
```

## Package Uninstall

```bash
pkg uninstall [PACKAGE_NAME]
```
## Package Installer Templates

For JSON file

```json
{
    "name" : "tester",
    "codes" : [{"filename":"main.py","code":"def run():\\n    print('Hello from tester')"}],
    "managersnip":"    elif cmd_arr[0] == 'tester':\\n        try:\\n            import app.tester.main\\n            app.tester.main.run()\\n        except:\\n            print('This app is deleted')\\n"
}
```

There are 3 fields for packaging. These are `name`, `codes` and `managersnip` 

Name field includes package name and this name also exists in .json file as a name

Codes field include `.py` files and their codes. Every code have to be written as string format. This format must be same Thonny IDE code styling. So `\t` does not be used.

Gooz Package Installer seperates these files and their codes, after it creates a application folder under `app` folder. The file which is `[pkgmanager.py](http://pkgmanager.py)` manages application orchestration. So, `pkgmanager` must include runner codes. It is provided with managersnip field in JSON file. Managersnip codes have to be like example JSON file.

For new line `\\n` must be used

Every application has any folder when turning on package, because every application contains only `.py` files. Unlimited py files can be used but not contain any folder.
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
# PWM

Commands for PWM pins.

## Pin Registering

```bash
pin var pwm -name=() -pin=() -freq=()
```

## Parameters

```bash
-name=() # takes pin name
-name=(myPWM) #new PWM pin name is myPWM
```

```bash
-pin=() # takes pin number
-pin=(2) # sets new PWM pin on 32
```

```bash
-freq=() # set PWM frequency from 1Hz to 40MHz
				 # Default value: 5000
-freq=(20000) # set PWM frequency 20KHz
```

## Using PWM Pins

```bash
pin pwm write $name $x # Set duty cycle from 0 to 1023 (0v - 3.3v)

pin pwm close $name # turn off PWM on the pin

pin pwm del $name # Deletes the PWM pin of pin named "name" 
pin pwm delete $name
```
# UART
Commands for Uart pins.

## Pin Registering

```bash
pin var uart -name=() -baudrate=() -rx=() -tx=() -type=()
```

## Parameters

```bash
-name=() #takes pin name 

-name=(My_pin)
```

```bash
-type=() # takes pin type, could be 1 or 0

-type=(0) # Closes Uart to use this pin in other activities
-type=(1) # Opens Uart
 
```

```bash
-baudrate=()# takes baudrate values

-baudrate(9600)
-baudrate(115200)
```

```bash
-rx=() -tx=() # takes rx tx pin values

-rx(16) #use the second uart pins in esp32 board
-tx(17)
```

## Using Uart Pins

```bash
pin uart write $(uart_name) "write what do you desire here"  --> # sends message 
pin uart listen $(uart_name) --> # helps you to read sent data
pin uart listen $(uart_name) stop --> # helps you to stop reading the data 
pin uart show $(uart_name) --> # shows the parametres you edited --> like (type= "1", baudrate="9600" ...)
pin uart del $(uart_name) --> # deletes the parametres from your uart port
pin uart p2p $(uart_name) --> # firstly sends data then sets it self to listen mode

```
# I2C

Commands for I2C pins.

## Pin Registering

```bash
pin var i2c -name=(asd) -scl=() -sda=() -freq=()
```

## Parameters

```bash
-name=() #takes pin name 

-name=(My_pin)
```

```bash
-scl=() #takes scl pin

-scl=(36)
```

```bash
-sda=() #takes sda pin

-sda=(33)
```

```bash
-freq=() #takes frequency (SCL clock rate)
				 #-freq=(400000) as default

-freq=(200000)
```

## Using I2C Pins

```bash
pin i2c write $(i2c_name) $(tx_data) --> # sends "tx_data" message to "i2c_name"
pin i2c listen $(i2c_name) --> # takes message from "i2c_name"
pin i2c listen $(i2c_name) stop --> # stops reading the data from "i2c_name"
pin i2c show --> # shows infos about current i2c pin or pins
pin i2c del $(i2c_name) --> # deletes the i2c pins named "i2c_name"
pin i2c p2p $(i2c_name) $(tx_data) --> # firstly sends "tx_data" message to "i2c_name" then takes message from "i2c_name"
```
