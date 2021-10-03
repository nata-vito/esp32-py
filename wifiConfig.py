import network 

sta_if = network.WLAN(network.STA_IF)               # Instance to station, please read the documentation for more details
ap_if = network.WLAN(network.AP_IF)                 # Instance to acess point, ..........................................

print("STA_IF: ", sta_if.active())                                   # Cheking if station mode is active
print("AP_IF: ", ap_if.active())                                     # Cheking if acess point is active
print("AP Settings: ", ap_if.ifconfig())                             # Cheking wifi settings from acess point
print("STA Settings: ", sta_if.ifconfig())                           # Cheking wifi settings from station 

sta_if.active(True)                                                  # Activating the station mode 
print("STA_IF: ", sta_if.active())                                   # Cheking if station mode is active

sta_if.connect('<your ESSID>', '<your password>')                    # Conect to your wifi router
print("STA Is Connected: ", sta_if.isconnected())                    # Cheking connection
print("STA Settings: ", sta_if.ifconfig())                           # Cheking wifi settings from station 