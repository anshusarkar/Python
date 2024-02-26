# Hey you made it by your own insperations ! 
# Install the Neo theme press ctrl + k + t and select it 4344

import random 
import time 

ascii_art = """
N   N  EEEE   OOO
NN  N  E     O   O
N N N  EEEE  O   O
N  NN  E     O   O
N   N  EEEE   OOO
"""

l_hiragana = ['あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん']


l_katakana = ['ア', 'イ', 'ウ', 'エ', 'オ',
  'カ', 'キ', 'ク', 'ケ', 'コ',
  'サ', 'シ', 'ス', 'セ', 'ソ',
  'タ', 'チ', 'ツ', 'テ', 'ト',
  'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
  'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
  'マ', 'ミ', 'ム', 'メ', 'モ',
  'ヤ', 'ユ', 'ヨ',
  'ラ', 'リ', 'ル', 'レ', 'ロ',
  'ワ', 'ヲ', 'ン',
  'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
  'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
  'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
  'バ', 'ビ', 'ブ', 'ベ', 'ボ',
  'パ', 'ピ', 'プ', 'ペ', 'ポ',
  'キャ', 'キュ', 'キョ',
  'シャ', 'シュ', 'ショ',
  'チャ', 'チュ', 'チョ',
  'ニャ', 'ニュ', 'ニョ',
  'ヒャ', 'ヒュ', 'ヒョ',
  'ミャ', 'ミュ', 'ミョ',
  'リャ', 'リュ', 'リョ',
  'ギャ', 'ギュ', 'ギョ',
  'ジャ', 'ジュ', 'ジョ',
  'ビャ', 'ビュ', 'ビョ',
  'ピャ', 'ピュ', 'ピョ']

l_mix_font = l_hiragana + l_katakana




def print_fonts(l:list):

    while True :
        
        random_element = random.choice(l)
        
        second_rand_element = random.choice(l)
        
        third_rand_element = random.choice(l)
        
        time.sleep(0.01)
        
        print(f"\t{second_rand_element}\t" ,f"\t{random_element}\t",f"\t{third_rand_element}\t" ,end=" ") # end = " " is used to print all values horizontaly 
                                                                                                # python's print function prints values in a line like Sysout in java

while True :
    print("=============================\n")
    print(ascii_art)
    print("=============================\n")
    
    
    print("=============================\n")
    print("Press 1 for hiragana action ")
    print("Press 2 for katakana actions ")
    print("Press 3 for mixed action ")
    print("\n=============================\n")
    
    choice = int(input("\n\nEnter a value : "+"\n\n>> "))
       
    match choice :
        case 1 :
            print_fonts(l_hiragana)
        case 2 :
            print_fonts(l_katakana)
        case 3 :
            print_fonts(l_mix_font)
        case _:
            print("\nInput is wrong !\n\n")