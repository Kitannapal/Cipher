from logo import logo 

print(logo) 

  

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

  

def cipher(input_text, shift_amount, its_direction): 

  output_text = "" 

  #global stop 

  if its_direction == "decode": 

    shift_amount *= -1 

  for char in input_text: 

    if char in alphabet: 

      position = alphabet.index(char) 

      new_position = position + shift_amount 

      new_position %= 26 

      output_text += alphabet[new_position] 

    else: 

      output_text += char 

  print(f"The {its_direction}d text is: {output_text} \n") 

  

stop = False 

while not stop: 

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 

  text = list(input("Type your message:\n").lower()) 

  shift = int(input("Type the shift number:\n")) 

  shift %= 26 

  cipher(input_text = text, shift_amount = shift, its_direction = direction) 

  repeat = input("If you want to go again, type 'y' else type 'n' \n") 

  if repeat == 'n': 

    stop = True 

    print("Goodbye!") 

  

  

  

  

logo = """            

,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,   

a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8   

8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88           

"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88           

`"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88    

            88             88                                  

           ""             88                                  

                          88                                  

,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,   

a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8   

8b         88 88       d8 88       88 8PP""""""" 88           

"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88           

`"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88           

              88                                              

              88            

""" 