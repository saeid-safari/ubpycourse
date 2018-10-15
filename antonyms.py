d=dict()
while True:
    word=input("enter the word for dictionary")
    if word in d.keys():
        print (d[word])

    else:
        x=input("i dont khnow antony of this word , do you know ?(y/n)")
        if x=="y":
            word2=input("please learning to me")
            d[word]=word2
            d[word2]=word
        else:
            print("tank you")
