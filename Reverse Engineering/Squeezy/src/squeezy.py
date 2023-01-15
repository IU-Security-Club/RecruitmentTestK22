import base64
def checkpass():
  userinput = input("Enter the password: ")
  key = "meownyameownyameownyameownyakiayameownyameownya"
  a = woah(key,userinput)
  b = str.encode(a)
  result = base64.b64encode(b, altchars=None)
  if result == b'JCspODwqJC4sOgwCSQ4GOiMeBUo+ODodRFoVDRI2FDclXhccQA8XBTJSB0YdWBw=':
      return True
  else:
      return False

def main():
    access = checkpass()
    if access == True:
        print("\nUnlocked. The flag is the password.")
        print("pwease let me do my nya~ next time!!")
        return
    else:
        print("Incorrect password!")
        print("sowwy but now you gunnu have to listen to me spweak in cat giwrl speak uwu~")
        catmain()

def catmain():
    access = catcheckpass()
    if access == True:
        print("s-senpai... i unwocked it fowr you.. uwu~")
        print("t-the fwlag is... the password.. nya!")
        return
    else:
        print("sowwy but that wasnt quite rwight nya~... pwease twy again")
        catmain()

def catcheckpass():
  userinput = input("pwease enter youwr password... uwu~ nya!!: ")
  key = "meownyameownyameownyameownyakiayameownyameownya"
  a = woah(key,userinput)
  b = str.encode(a)
  result = base64.b64encode(b, altchars=None)
  if result == b'JCspODwqJC4sOgwCSQ4GOiMeBUo+ODodRFoVDRI2FDclXhccQA8XBTJSB0YdWBw=':
      return True
  else:
      return False

def woah(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    
access = False
main()
input("\nPress Enter to continue...")