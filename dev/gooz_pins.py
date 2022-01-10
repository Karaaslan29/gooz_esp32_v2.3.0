import dev.gooz_pin_uart
import dev.gooz_pin_adc
import dev.gooz_thread
import dev.gooz_pin_gpio
import dev.gooz_pin_pwm
import _thread
def init(cmd_arr):
    if cmd_arr[1] == "uart":
        if not len(cmd_arr) > 2:
            print("Missing Argument!")
            return
        if cmd_arr[2] == "show":
            dev.gooz_pin_uart.show_registered_uart()
        elif cmd_arr[2] == "write":
            dev.gooz_pin_uart.write(cmd_arr)
        elif cmd_arr[2] == "listen":
            dev.gooz_pin_uart.listen(cmd_arr)
        elif cmd_arr[2] == "p2p":
            dev.gooz_pin_uart.p2p(cmd_arr)
        elif cmd_arr[2] == "del":
            dev.gooz_pin_uart.uart_delete(cmd_arr)
        else:
            print("Unknown uart command: "+'"'+cmd_arr[2]+'"')
            
    elif cmd_arr[1] == "adc":
        if not len(cmd_arr) > 2:
            print("Missing Argument!")
            return
        if cmd_arr[2] == "read":
            dev.gooz_pin_adc.read(cmd_arr)
        elif cmd_arr[2] == "listen":
            dev.gooz_pin_adc.listen(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.gooz_pin_adc.delete(cmd_arr)
        else:
            print("Unknown ADC command: "+'"'+cmd_arr[2]+'"')
            
    elif cmd_arr[1] == "gpio":
        if not len(cmd_arr) > 2:
            print("Missing Argument!")
            return
        if cmd_arr[2] == "write":
            dev.gooz_pin_gpio.write(cmd_arr)
        elif cmd_arr[2] == "read":
            dev.gooz_pin_gpio.read(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.gooz_pin_gpio.delete(cmd_arr)
        else:
            print("Unknown gpio command: "+'"'+cmd_arr[2]+'"')
            
    elif cmd_arr[1] == "pwm":
        if not len(cmd_arr) > 2:
            print("Missing Argument!")
            return
        if cmd_arr[2] == "write":          
            dev.gooz_pin_pwm.write(cmd_arr)
        elif cmd_arr[2] == "test":
            dev.gooz_pin_pwm.testing()
        elif cmd_arr[2] == "close":
            dev.gooz_pin_pwm.close(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.gooz_pin_pwm.delete(cmd_arr)
        else:
            print("Unknown PWM command: "+'"'+cmd_arr[2]+'"')
        
    if cmd_arr[1] == "var":
        if not len(cmd_arr) > 2:
            print("Missing Argument!")
            return
        if cmd_arr[2] == "uart":
            dev.gooz_pin_uart.register(cmd_arr)
        elif cmd_arr[2] == "adc":
            dev.gooz_pin_adc.register(cmd_arr)
        elif cmd_arr[2] == "gpio":
            dev.gooz_pin_gpio.register(cmd_arr)
        elif cmd_arr[2] == "pwm":
            dev.gooz_pin_pwm.register(cmd_arr)
        else:
            print("Unknown var command: "+'"'+cmd_arr[2]+'"')
