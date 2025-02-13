#Hamilton Error Handling
Step_one_input = input("Is there an error on your hamilton?: ")
#def LB_station(intro_q,emergency,success,hardware_issue):
#    if intro_q == "Yes":

if Step_one_input == "Yes":
    emergency = input("Is this an emergency? Is this occuring mid-run?")
    if emergency == "Yes":
        print(""""Call The Automation Team
        1. Record error log
        2. Save trace files
        3. Email MDL Automation and Liquidbiopsy Mole""")
    elif emergency == "No":
        hardware_issue = input("Is this a hardware issue?: ")
        if hardware_issue == "Yes":
            print(""""Call The Automation Team
        1. Record error log
        2. Save trace files
        3. Email MDL Automation and Liquidbiopsy Mole""")
        elif hardware_issue == "No":
            print(""""Call The Automation Team
        1. Record error log
        2. Save trace files
        3. Email MDL Automation and Liquidbiopsy Mole""")
            
            
        
elif Step_one_input == "No":
    pass
        
    
