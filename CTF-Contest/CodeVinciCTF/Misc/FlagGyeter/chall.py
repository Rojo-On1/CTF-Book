import signal, base64
#from secret import FLAG; 
import sys

if len(sys.argv) < 2:
    print("Usage: <CANT>")
    exit(1)

FLAG = "{CTFTIMEYESSS}"

print("""
,------.,--.                    ,----.                    ,--.    ,--.                 
|  .---'|  | ,--,--. ,---.     '  .-./  ,--. ,--.,--,--.,-'  '-.,-'  '-. ,---. ,--.--. 
|  `--, |  |' ,-.  || .-. |    |  | .---.\  '  /' ,-.  |'-.  .-''-.  .-'| .-. :|  .--' 
|  |`   |  |\ '-'  |' '-' '    '  '--'  | \   ' \ '-'  |  |  |    |  |  \   --.|  |    
`--'    `--' `--`--'.`-  /      `------'.-'  /   `--`--'  `--'    `--'   `----'`--'    
                    `---'               `---'                                          

-----------------------------------------------------------------------

Bro really thinks he can try solving this :skull:
Remember: try not to hit by the great meme depression of 2025.""")

OMEGA = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? - Barry? - Adam? - Can you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money mewing those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. - You got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be diddy row 118,000. - Bye!".encode()
SIGMA = str("0" * int(sys.argv[1])).encode()
print("PASS -> ",SIGMA)

if __name__ == "__main__":
    print("Testing...")
    print("Lenght Needed: ", len(base64.b64encode(OMEGA).hex()))
    print("Lengh Obtained: ",len(base64.b85encode(SIGMA).hex()))

    signal.alarm(300)
    if len(base64.b85encode(SIGMA).hex()) == len(base64.b64encode(OMEGA).hex()):
        print("Yah, you'd win " + FLAG)
    else:
        print("Bro thinks he can get me to spill the flag, get your unemployed ahhh out of here.")
