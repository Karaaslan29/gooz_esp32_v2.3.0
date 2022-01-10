#gooz_pin_pwm.py v1
from machine import PWM,Pin
import utime

key = ""
value = ""
key_list = []
value_list = []
registered_key = []
registered_value = []
pwm_dic = []
saved_pwms = []

def register(cmd_arr):
    global key
    global value
    global key_list
    global value_list
    global registered_key
    global registered_value
    global pwm_dic
    global saved_pwm
    
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
    pwm_name = ""
    pwm_freq = ""
    pwm_pin = ""
    
    for pairs in key_list:
        if pairs == "name":
            pwm_name = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "freq":
            pwm_freq = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "pin":
            pwm_pin = value_list[temp_counter]
            temp_counter += 1
    if pwm_name =="" or pwm_pin =="":
        print("Missing necessary argument(s)!")
        return
    #Saving
    isNameExist =False
    for myPWM in saved_pwms:
        if myPWM["name"] == pwm_name:
            isNameExist = True
            
    
    if isNameExist:
        print("The pin named "+'"'+pwm_name+'"'+" already exists")
        return
    
    temp = {}
    temp["name"] = pwm_name
    temp["pin"] = pwm_pin    
    if not pwm_freq == "":
        temp["freq"] = pwm_freq
    else:
        temp["freq"] = "5000"
    saved_pwms.append(temp)
    print(saved_pwms)
        
        
def write(cmd_arr):
    exported_pin = {"name":"","freq":"","pin":""}
    for myPWM in saved_pwms:
        if cmd_arr[3] == myPWM["name"]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
            pwm_t = PWM(Pin(int(exported_pin["pin"],Pin.OUT)),freq=int(exported_pin["freq"]))
            if len(cmd_arr) > 4:
                pwm_t.duty(int(cmd_arr[4]))
                print("PWM has been started")
            else:
                print("Missing Argument!")
    if exported_pin["name"] == "":
        print("There is no PWM pin named "+'"'+cmd_arr[3]+'"')
        
def close(cmd_arr):
    exported_pin = {"name":"","freq":"","pin":""}
    for myPWM in saved_pwms:
        if cmd_arr[3] == myPWM["name"]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
            pwm_t = PWM(Pin(int(exported_pin["pin"],Pin.OUT)),freq=int(exported_pin["freq"]))
            pwm_t.deinit()
    if exported_pin["name"] == "":
        print("There is no PWM pin named "+'"'+cmd_arr[3]+'"')

def delete(cmd_arr):
    try:
        global saved_pwms
        pwm_names =[]
        for tempName in saved_pwms:
            pwm_names.append(tempName["name"])
        if cmd_arr[3] in pwm_names:
            for myPWM in saved_pwms:
                if myPWM["name"] == cmd_arr[3]:
                    saved_pwms.remove(myPWM)
                    print(cmd_arr[3]+" Successfully deleted")
                    print(saved_pwms)
        else:
            print("There is no PWM pin named "+'"'+cmd_arr[3]+'"')
    except:
        print("Unknown error while deleting PWM pin!")

"""   
def testing():
    pwm2 = PWM(Pin(2,Pin.OUT))
    pwm2.duty(512)
"""
    
