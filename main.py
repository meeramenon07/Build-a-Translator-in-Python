def translate(word):
 translation = ""
 for letter in word:
   if letter.upper() in "BCDPQRWXYZ":
     if letter.islower():
       translation = translation + "edtechbymeera"
     else:
       translation = translation + "EDTECHBYMEERA"
   else:
     translation = translation + letter 
 return translation 
print(translate(input("Enter a word: ")))

    
   
   

     

    
       


