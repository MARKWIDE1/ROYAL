import base64 
 import os 
 def key(): 
         x=input("\nENTER EKY : ") 
  
         x1 = x.encode("ascii") 
  
         x2 = base64.b64encode(x1) 
  
         x3 = x2.decode("ascii").upper() 
  
         print(x3) 
         key() 
  
 key()
