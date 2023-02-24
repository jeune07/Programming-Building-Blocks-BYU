
print("""You are a detective on the trail of a ruthless killer. The city is on edge as the killer has claimed
several victims and shows no signs of stopping. You are determined to bring this killer to justice.
As you begin your investigation, you have several options for where to start:
Option A: Interview the victims families
Option B: Examine the crime scenes
Option C: Review the police reports""")

options=input("Please chose A, B, or C to start the investigation")
options=options.capitalize()
if options=="A":
    print("Great you choose the option A")
    print("""
    You speak with the families of the victims and learn that they all had something in common 
 they were all involved in a local charity organization. This leads you to suspect that the 
 killer may have a personal vendetta against the charity.
 """)
    print("Ther are two way ossible")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Option A")
    print("""Investigate the charity organization and its members to see if anyone had a motive for committing the 
    murders.""")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Option B")
    print("""Interview the families and friends of the victims again to see if they had received any suspicious
     messages or threats related to their involvement in the charity.""")
    scen1Option=input("what option will you choose A or B")
    scen1Option=scen1Option.capitalize()
    if scen1Option=="A":
        print("""
            you would conduct follow-up interviews with the families and friends of the victims to see if they
            had received any suspicious messages or threats related to their involvement in the charity. You could also
            look for any patterns in the timing or nature of the messages, such as whether they were all sent around the
            same time, or if there were any similar themes or language used in the messages. Additionally, you could check
            the victims' social media accounts to see if they had any interactions or conversations related to the charity
            that could be relevant to the case.
            You could also check the victims' phone records, email and other forms of communication to see if there were any 
            suspicious messages or calls.
            It's also important to check if any of the victims received any visits or calls from any strangers or people they
             don't know in the days leading up to the murders.
        """)
    elif scen1Option=="B":
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("""you choose option two and have gathered enough information and evidence, you could then present your findings 
        to the authorities and work with them to arrest and prosecute the perpetrator. It's important to work closely with the 
        authorities to ensure that the investigation and any subsequent trial is conducted legally and ethically. This could involve 
        collaborating with forensic experts, witnesses, and other law enforcement agencies to build a strong case and secure a conviction.
        It's also important to keep the victims' families informed of the progress of the investigation and any developments in the case. They may 
        have questions or concerns and it's important to address them and provide them with the support they need.
        It's also important to consider the possibility that the killer may have had an accomplice or have tried to hide the evidence, so it's 
        important to keep an open mind and consider all possibilities throughout the investigation.""")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("the possibles options are A or B, please start again")


    
elif options=="B":
    print("""
    At the crime scenes, you notice that each victim was killed in a different way, but 
there's one common thing: a flower, a red rose, left at the scene of the crime. 
This leads you to believe that the killer may be sending a message.
    """)
elif options=="C":
    print("""
The police reports indicate that all of the victims were killed at night, and all had a history of late-night activities.
 This leads you to suspect that the killer may be targeting people who are out late at night.
    """)
else:
    print("Please choose option: A, B or C")