# Hey you made it by your own insperations ! 
# Install the Neo theme press ctrl + k + t and select it 4344
import random 
import time 


l = ['あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん']



def print_fonts(l:list) :
    
    random_element = random.choice(l)
    
    second_rand_element = random.choice(l)
    
    third_rand_element = random.choice(l)
    
    time.sleep(0.01)
    
    print(f"\t{second_rand_element}\t" ,random_element,f"\t{third_rand_element}\t" ,end=" ") # end = " " is used to print all values horizontaly 
                                                                                             # python's print function prints values in a line like Sysout in java
    print_fonts(l)

print_fonts(l)