#Give instruction according to the traffic light

light = input("Enter the light :")

if(light == 'red') :
    print("Stop")

elif(light == 'yellow'):
    print("Look")

elif(light == 'green'):
    print("go")
    
else :
    print("Light is broken")