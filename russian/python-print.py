def text_create(name,msg):
    desktop_path = 'c:/Users/weixue/Desktop/'
    full_path = desktop_path + name +'.txt'
    print(full_path)
    file = open(full_path,'w')
    text_clear = text_filter(msg)
    file.write(text_clear)
    file.close()
    print('Done')


def text_filter(word,censored_word = 'Lame',changed_word = 'Awesome'):
    return word.replace(censored_word,changed_word)

print(text_filter('Python is Lame!'))

def censored_text_create(name, msg):

    text_create(name,msg)


censored_text_create('try', 'Lame!Lame!Lame!')
