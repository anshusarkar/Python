# Hey you made it by your own insperations ! 
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



while True :
    
    random_element = random.choice(l)
    
    second_rand_element = random.choice(l)
    
    third_rand_element = random.choice(l)
    
    time.sleep(0.01)
    
    print(f"\t{second_rand_element}\t" ,random_element,f"\t{third_rand_element}\t" ,end=" ") # end = " " is used to print all values horizontaly 
                                                                                             # python's print function prints values in a line like Sysout in java
