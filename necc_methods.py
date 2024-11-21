def format_a_word_title_case(word):
    char_list = list(word)
    0
    w = char_list[0]
    for i in range(len(char_list)):

        if not char_list[i].isalpha() and i < len(char_list) - 1:
            c = char_list[i + 1].upper()
            w = w + c
        elif char_list[i].isalpha() and i < len(char_list) - 1:
            w = w + char_list[i + 1]
        print(w)
        i = i + 1

    formatted_word = w
    return formatted_word


def Title_Case(original_text):
    words = original_text.split()
    formatted_words = []
    formated_text = ''
    for word in words:
        word = word.lower().capitalize()
        word = format_a_word_title_case(word)
        formated_text = formated_text + word + ' '

    return formated_text

def Gjej_Kudo_Ku_Gjendet(filan,text):
    final_indexs=[]
    where=text.find(filan)
    final_indexs.append(where)
    print(final_indexs)
    while where!=-1:
        text=text[where+len(filan):len(text)]
        print(text)
        where=text.find(filan)
        if where!=-1:
            final_indexs.append(where)
            print(final_indexs)
    return final_indexs
def special_min(vec):
    min=1000000
    ji=0
    i=0
    for x in vec:
        if x<min and x >=0:
            min=x
            ji=i
        i=i+1
    return min,ji

def Separate_into_sentences(text):
    w=0
    sh_p=['... ','. ','? ',"! "]
    fjalite=[]
    wheres=[]
    while w!=1000000:
        for x in sh_p:
            where=text.find(x)
            wheres.append(where)
        w,i=special_min(wheres)
        fjalia = text[0:w+len(sh_p[i])]
        if fjalia!='':
            fjalite.append(fjalia)
        text=text[w+len(sh_p[i]):len(text)]
        wheres=[]
    return fjalite


def Sentence_Case(original_text):
    sentences=Separate_into_sentences(original_text)
    txt=''
    for sentence in sentences:
        txt=txt+sentence.capitalize()
    return txt

def lower_case(original_text):
    return original_text.lower()

def UpperCase(original_text):
    return original_text.upper()

def Capitalized_Case(original_text):
    words=original_text.split(' ')
    txt=''
    for word in words:
        txt=txt+word.capitalize()+' '
    return txt

def AlternatingCase(original_text):
    txt=''
    i=0
    for char in original_text:
        if char==' ':
            i=i+1
        if i%2==0:
            txt=txt+char.upper()
        else:
            txt=txt+char.lower()
        i=i+1
    return txt