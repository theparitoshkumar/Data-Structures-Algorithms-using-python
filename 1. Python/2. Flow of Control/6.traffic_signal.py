# Display the appropriate message as per the colour of signal at the road crossing.

signal = input("Enter the traffic light colour: ")

if signal == "red" or signal == "RED":
    print("STOP")
elif signal == "orange" or signal == "ORANGE":
    print("Be Slow")
elif signal == "green" or signal == "GREEN":
    print("Go!")