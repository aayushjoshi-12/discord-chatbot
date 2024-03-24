import random

def handle_response(msg):
    p_msg = msg.lower()

    if p_msg == "hello" :
        return "Hey there bitch!"
    
    if p_msg == "rolldice" :
        return str(random.randint(1,6))
    
    if p_msg == "!help" :
        return "`khud krle laude`"
    
    # return "Pan thuk kr bat kr"