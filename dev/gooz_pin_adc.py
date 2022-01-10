import machine
import utime
import _thread

key = ""
value = ""
key_list = []
value_list = []
registered_key = []
registered_value = []
adc_dic = []
saved_adc = []
exit_flag = 0

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
        adc_name = ""
        adc_pin = ""
        
        for pairs in key_list:
            if pairs == "name":
                adc_name = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "pin":
                adc_pin = value_list[temp_counter]
                temp_counter += 1
                
        if adc_name == "" or adc_pin == "":
            print("Missing necessary argument(s)!")
            return
        
        isNameExist =False
        for myADC in saved_adc:
            if myADC["name"] == adc_name:
                isNameExist = True
        if isNameExist:
            print("The pin named "+'"'+adc_name+'"'+" already exists")
            return
        
        temp = {}
        temp["name"] = adc_name
        temp["pin"] = adc_pin
        saved_adc.append(temp)
        print(saved_adc)
    except:
        print("Unknown error while registering ADC pin!")
        
def delete(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!")
            return
        
        exported_pin ={"name":"","pin":""}
        for myADC in saved_adc:
            if myADC["name"] == cmd_arr[3]:
                exported_pin["name"] = myADC["name"]
                exported_pin["pin"] = myADC["pin"]
                saved_adc.remove(myADC)
                print(saved_adc)
        if exported_pin["name"] == "":
            print('There is no ADC pin named '+'"'+cmd_arr[3]+'"')
    except:
        print("Unknown error while deleting ADC pin!")
        
def read(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!")
            return
        exported_pin ={"name":"","pin":""}
        for myADC in saved_adc:
            if cmd_arr[3] == myADC["name"]:
                exported_pin["name"] = myADC["name"]
                exported_pin["pin"] = myADC["pin"]
                adc_t = machine.ADC(machine.Pin(int(exported_pin["pin"])))
                try:
                    if len(cmd_arr) > 4:
                        read_count = int(cmd_arr[4])
                        for i in range(0,read_count):
                            adc_t.atten(machine.ADC.ATTN_11DB)
                            reading = adc_t.read()
                            print(reading)
                    else:
                        adc_t.atten(machine.ADC.ATTN_11DB)
                        reading = adc_t.read()
                        print(reading)
                except ValueError:
                    print('"'+cmd_arr[4]+'"'+" is not a integer!")
                    
        if exported_pin["name"] == "":
            print('There is no ADC pin named '+'"'+cmd_arr[3]+'"')
    except:
        print("Unknown error while reading ADC pin!")

def listen(cmd_arr):
    try:
        global exit_flag
        
        if not len(cmd_arr) > 3:
            print("Missing Argument!")
            return
        
        if cmd_arr[3] == "stop":
            exit_flag = 1
            return exit_flag
        
        exported_pin = {"name":"","pin":"" }
        for myADC in saved_adc:
            if cmd_arr[3] == myADC["name"]:
                exported_pin["name"] = myADC["name"]
                exported_pin["pin"] = myADC["pin"]
                _thread.start_new_thread(listen_thread,(exported_pin["name"],exported_pin["pin"]))
        if exported_pin["name"] == "":
            print('There is no ADC pin named '+'"'+cmd_arr[3]+'"')   
    except:
        print("Unknown error while listening ADC pin!")

def listen_thread(adc_name,adc_pin):
    global exit_flag
    adc_pin_t = machine.Pin(int(adc_pin))
    adc_temp = machine.ADC(adc_pin_t)
    adc_temp.atten(machine.ADC.ATTN_11DB)
    while True:
        if exit_flag == 1:
            exit_flag = 0
            break
        readed = adc_temp.read()
        print(readed)
        utime.sleep(1)
    return 0
