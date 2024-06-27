import socket
import os

def call_rule(RULE_ID=2100498):
   if RULE_ID == 2100498: rule_2100498()

def rule_2100498 (DEST_IP=""): 
  Send_Text_to_IP (TOSEND = b"uid=0(root) gid=0(root) groups=0(root)", DEST_IP=DEST_IP, PORT=80)

def Send_Text_to_IP (TOSEND = b"uid=0(root) gid=0(root) groups=0(root)", DEST_IP="", PORT=80):

  
  if DEST_IP == "" : # if empty DEST_IP, select the default broadcast IP
    
    DEST_IP = get_default_gateway_ip()
    print ("Destination IP assigned to "+ str(DEST_IP))


  SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Socket creation
  SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1) # Just in case the address was BroadcastIp
  SOCK.sendto(TOSEND,(DEST_IP,PORT))
  SOCK.close()

  print ("Enviado " + str(TOSEND) + "a " + DEST_IP + ":" + str(PORT))

def get_default_gateway_ip():
    with os.popen("ip route | grep default") as f: # I use os in order to reduce non standard modules.
        return f.read().split()[2]

if __name__ == "__main__":
  call_rule()