def word():
    article = input("Write your article here: ")
    replacement = input("Write your replacement here: ")
    new_word = input("Write your new word here: ")
    new_article = article.replace(replacement, new_word)
    print(new_article)
word()