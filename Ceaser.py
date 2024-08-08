import string
def get_shift():
  """Prompts the user for a number between 1 and 10, repeatedly until a valid input is provided."""
  while True:
    try:
      shift = int(input("Enter the shift value 1-25: "))
      if 1 <= shift <= 25:
        return shift
      else:
        print("\nInvalid input. Please Enter the shift value 1-25: .\n")
    except ValueError:
      print("\nInvalid input. Please enter a number\n")
            
	
def encrypt(text,shift):
    result=""
    for spell in text:
         if spell.islower():
            encrypted_text=(ord(spell) - ord('a') + shift) % 26 + ord('a') 
            result+=chr(encrypted_text)
         elif spell.isupper():
             encrypted_text=(ord(spell) - ord('A') + shift) % 26 + ord('A')
             result+=chr(encrypted_text)
         else:
             result+=spell
    return result

while True:
    choise=input("-----------\nceaser cipher\n-----------\n1.encrypt \n2.decrypt \n3.exit \nEnter your choise :")
    if choise == '1':
        shift=get_shift()
        text=input("Enter the string for encrypt :")
        result=encrypt(text,shift)
        print("Encrypted value",result,"\n")
    elif choise == '2':
            shift= get_shift()
            text=input("Enter the string for decrypt : ")
            result=encrypt(text,-shift)
            print("decrypted value",result,"\n")
    elif choise == '3':
            break
    else:
            print("\nEnter number correctly\n")
