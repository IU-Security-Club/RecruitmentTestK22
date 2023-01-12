def checkpass():
  userinput = input("Enter the password: ")
  if userinput[0:11] == "INFORSECIU{":
        if userinput[17:20] == "rE4":
            if userinput[29:32] == "hi5":
                if userinput[11:14] == "y34":
                    if userinput[23:26] == "_di":
                        if userinput[14:17] == "H_u":
                            if userinput[20:23] == "lly":
                                if userinput[26:29] == "d_7":
                                    if userinput [32:34] == "!}":
                                        return True
  else:
    return False
def main():
    access = checkpass()
    if access == True:
        print("\nUnlocked. The flag is the password.")
        print("b-but i wunna show off my catswpeak uwu~... why wont you let me do my nya!!\noh well... good luck with the rest of the ctf :/\nbut I WANT TO SPWEAK CATGIRL NEXT TIME SO YOU BETTER LET ME >:(")
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
        print("sowwy but that wasnt quite rwight nya~")
        catmain()

def catcheckpass():
  userinput = input("Enter the password: ")
  if userinput[0:11] == "INFORSECIU{":
        if userinput[17:20] == "rE4":
            if userinput[29:32] == "hi5":
                if userinput[11:14] == "y34":
                    if userinput[23:26] == "_d1":
                        if userinput[14:17] == "#_u":
                            if userinput[20:23] == "lly":
                                if userinput[26:29] == "d_7":
                                    if userinput [32:34] == "!}":
                                        return True
  else: 
    return False

access = False
main()
input("\nPress Enter to continue...")