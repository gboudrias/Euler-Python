'''
Created on 2012-01-13

@author: Guigui
'''

spelled_out_numbers = {
                       1:'one', 
                       2:'two', 
                       3:'three', 
                       4:'four',
                       5:'five',
                       6:'six',
                       7:'seven',
                       8:'eight',
                       9:'nine',
                       10:'ten',
                       11:'eleven',
                       12:'twelve',
                       13:'thirteen',
                       14:'fourteen',
                       15:'fifteen',
                       16:'sixteen',
                       17:'seventeen',
                       18:'eighteen',
                       19:'nineteen',
                       20:'twenty',
                       30:'thirty',
                       40:'forty',
                       50:'fifty',
                       60:'sixty',
                       70:'seventy',
                       80:'eighty',
                       90:'ninety',
                       }                       

def projfunc():
    return spell_to_one_thousand()

def spell_to_one_thousand():
    total_letters = 0
    
    for i in range(1,1000):
        total_letters += count_letters(i)
        
        
    # Less complicated than implementing last bit of logic.
    total_letters += len('onethousand')
    
    return total_letters

def count_letters(i):
    total_letters = 0
    
    if i >= 100:
        hundreds = i // 100
        
        total_letters += len(spelled_out_numbers[hundreds]) + len('hundred')
        
        if i % 100 != 0:
            total_letters += len('and')
    
        i = int(str(i)[1] + str(i)[2])
    
    if i != 0:
        if i < 20:
            total_letters += len(spelled_out_numbers[i])
        else:
            total_letters += len(spelled_out_numbers[int(str(i)[0]) * 10])
            
            if i % 10 != 0:
                total_letters += len(spelled_out_numbers[int(str(i)[1])])
    
    return total_letters
            
if __name__ == '__main__':
    print(projfunc())