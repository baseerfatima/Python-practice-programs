def  con(sen):
    for i in [".", ",", "!", "?"]:
      sen=sen.replace(i," ")
    max_word= ""
    words=sen.split(" ")
    for word in words:
       if len(word)> len(max_word):
          max_word=word
    print(max_word)
sen="a good boy"
con(sen)
