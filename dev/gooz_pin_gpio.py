from machine import Pin
import time
import _thread
import utime
import dev.gooz_thread

key = ""
value = ""
key_list = []
value_list = []
registered_key = []
registered_value = []
gpio_dic = []
saved_gpio = []

def register(cmd_arr):
    try:
        global key
        global value
        global key_list
        global value_list
        global registered_key
        global registered_value
        
        for i in cmd_arr:
            if i[0] == "-":
                for a in range(1,len(i)):
                    if i[a] == "=":
                        break
                    key += i[a]
                key_list.append(key)
                door = 0
                for index in range(1,len(i)):
                    if i[index] == ")":
                        door = 0
                    if door == 1:
                        value += i[index]
                    elif i[index] == "(":
                        door = 1
                value_list.append(value)
                key = ""
                value = ""
        registered_key.append(key_list)
        registered_value.append(value_list)
        temp_counter = 0
        gpio_name = ""
        gpio_type = ""
        gpio_in_type = ""
        gpio_pin = ""
        
        for pairs in key_list:
            if pairs == "name":
                gpio_name = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "type":
                gpio_type = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "mode":
                gpio_in_type = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "pin":
                gpio_pin = value_list[temp_counter]
                temp_counter += 1
        
        if gpio_name == "" or gpio_type == "" or gpio_pin == "":
            print("Missing necessary argument(s)!")
            return
        
        isNameExist = False
        for myGPIO in saved_gpio:
            if myGPIO["name"] == gpio_name:
                isNameExist = True
        if isNameExist:
            print("The pin named "+'"'+gpio_name+'"'+" already exists")
            return
        
        #Saving
        temp = {}
        temp["name"] = gpio_name
        temp["type"] = gpio_type
        temp["mode"] = gpio_in_type
        temp["pin"] = gpio_pin
        saved_gpio.append(temp)
        
        print(saved_gpio)
    except:
        print("Unknown error while registering GPIO pin!")
        

def delete(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!")
            return
        
        exported_pin = {"name":"","pin":"","type":"","mode":""}
            
        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
                saved_gpio.remove(myGPIO)
                print(saved_gpio)
        if exported_pin["name"] == "":
            print('There is no ADC pin named '+'"'+cmd_arr[3]+'"')
    except:
        print("Unknown error while deleting GPIO pin!")
    
            
def write(cmd_arr):
    try:
        if not len(cmd_arr) > 4:
            print("Missing Argument!")
            return
        
        exported_pin ={"name":"","pin":"","type":"","mode":""}

        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
            
        if exported_pin["name"] == "":
            print('There is no GPIO pin named '+'"'+cmd_arr[3]+'"')
            return
        
        global type_pin
        global in_type_pin
        global gpio_t
        if exported_pin["type"] == "out":
            type_pin = Pin.OUT
        elif exported_pin["type"] == "in":
            type_pin = Pin.IN
        elif exported_pin["type"] == "alt":
            type_pin = Pin.ALT
        elif exported_pin["type"] == "opendrain":
            type_pin = Pin.OPEN_DRAIN
        elif exported_pin["type"] == "altopendrain":
            type_pin = Pin.ALT_OPEN_DRAIN
        if exported_pin["mode"] == "pullup":
            in_type_pin = Pin.PULL_UP
        elif exported_pin["mode"] == "pulldown":
            in_type_pin = Pin.PULL_DOWN
        try:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin,in_type_pin)
        except:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin)
        try:
            if cmd_arr[4] == "HIGH" or cmd_arr[4] == "1":
                gpio_t.value(1)
            elif cmd_arr[4] == "LOW" or cmd_arr[4] == "0":
                gpio_t.value(0)
        except:
            print("Your Pin:"+exported_pin["name"]+" didn't work")
    except:
        print("Unknown error while writing GPIO pin!")

def read(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!")
            return
        
        exported_pin = {"name":"","pin":"","type":"","mode":""}
        
        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
        
        if exported_pin["name"] == "":
            print('There is no GPIO pin named '+'"'+cmd_arr[3]+'"')
            return

        global type_pin
        global in_type_pin
        global gpio_t
        if exported_pin["type"] == "out":
            type_pin = Pin.OUT
        elif exported_pin["type"] == "in":
            type_pin = Pin.IN
        elif exported_pin["type"] == "alt":
            type_pin = Pin.ALT
        elif exported_pin["type"] == "opendrain":
            type_pin = Pin.OPEN_DRAIN
        elif exported_pin["type"] == "altopendrain":
            type_pin = Pin.ALT_OPEN_DRAIN
        if exported_pin["mode"] == "pullup":
            in_type_pin = Pin.PULL_UP
        elif exported_pin["mode"] == "pulldown":
            in_type_pin = Pin.PULL_DOWN
        try:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin,in_type_pin)
        except:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin)
        try:
            print(gpio_t.value())
        except:
            print("Your Pin:"+'"'+exported_pin["name"]+'"'+" didn't work")
    except:
        print("Unknown error while reading GPIO pin!")
