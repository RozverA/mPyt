from machine import Pin

d0 = Pin(16, Pin.OUT)    # create output pin on GPIO0
d1 = Pin(5, Pin.OUT)    # create output pin on GPIO0
d2 = Pin(4, Pin.OUT)    # create output pin on GPIO0
d3 = Pin(0, Pin.OUT)    # create output pin on GPIO0
d4 = Pin(2, Pin.OUT)    # create output pin on GPIO0
d5 = Pin(14, Pin.OUT)    # create output pin on GPIO0
d6 = Pin(12, Pin.OUT)    # create output pin on GPIO0
d7 = Pin(13, Pin.OUT)    # create output pin on GPIO0
pins = [d0,d1,d2,d3,d4,d5,d6,d7]

def led_switch():
    i: int = 0
    print(i)
    print(pins[i].value())
    for i in range(8):
        if ((pins[i].value()) == 1):
            pins[i].value(0)
        else:
            pins[i].value(1) 
        print("pin ",i,pins[i].value())

def led_all_off():
    d0.off()
    d1.off()
    d2.off()
    d3.off()
    d4.off()
    d5.off()
    d6.off()
    d7.off()

def led_all_on():
    d0.on()
    d1.on()
    d2.on()
    d3.on()
    d4.on()
    d5.on()
    d6.on()
    d7.on()

    
#__________void main()___________
print("pin 0 = ",pins[0].value())
led_all_off()
#print("pin 0 = ",pins[0].value())

#print("pin 0 = ",pins[0].value())
#led_all_on()

d0.on()
print("pin 0 = ",pins[0].value())
d4.on()
d5.on()
led_switch()
print("pin 0 = ",pins[0].value())
#p0.value(1)             # set pin to on/high

#p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
#print(p2.value())       # get value, 0 or 1

#p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
#p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation

