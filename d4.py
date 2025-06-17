def con(sen):
    count_con=0
    count_vow=0
    vow=["a", "e", "i", "o", "u"]
    for char in sen.lower():
        if char.isalpha():
            if char in vow:
                count_vow+=1
            else:
                count_con+=1
    print(f"vowel count: {count_vow}, cons count: {count_con}")
sen=input("enter a sentence: ")
con(sen)