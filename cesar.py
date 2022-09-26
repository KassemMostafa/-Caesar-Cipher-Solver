import string 

txt1 = "NWLAHYCXPAJYQRNUNLQROOANVNWCYJAMNLJUJPNJDBBRLXWWDLXVVNUNLQROOANMNLNBJAXDUNLXMNMNLNBJANBCDWNVNCQXMNMNLQROOANVNWCCANBBRVYUNDCRURBNNYJASDUNBLNBJAMJWBBNBLXAANBYXWMJWLNBBNLANCNB"
txt2 = "vcfgrwqwfsbhfsntowbsobgfsbhfsnqvsnjcigsghqsoixcifrviwtshseicwbsgojsnjcigdogeisjcigoihfsgofhwgobgjcigbsrsjsnqwfqizsfrobgzsgfisgzsgxcifgcijfopzsgeiojsqzsggwubsgrsjchfsdfctsggwcbdofzseiszsghhcbashwsf"
alphabet = string.ascii_uppercase

# def stringtolist(s1):
#     list=[]
#     list[:0]=s1
#     return s1

def breakcesaradroite(s1):
    # l1=[]
    # l1[:0] = str
    # l1 = stringtolist(str)
    s1 = s1.upper()
    decrypted = ""
    maxchar = max(s1,key=s1.count)
    n = ord(maxchar) #valeur ascii de la lettre la plus fréquente
    n = abs(n-ord("E")) #decalage

    for c in s1:
        k = ord(c) - n
        if (k < 65):
            k += 26       
        decrypted += chr(k)
    return decrypted

def breakcesaragauche(s1):
    # l1=[]
    # l1[:0] = str
    # l1 = stringtolist(str)
    s1 = s1.upper()
    decrypted = ""
    maxchar = max(s1,key=s1.count)
    print(maxchar)
    n = ord(maxchar) #valeur ascii de la lettre la plus fréquente
    n = abs(n-ord("E")) #decalage

    for c in s1:
        k = ord(c) + n
        if (k > 90):
            k -= 26       
        decrypted += chr(k)
    return decrypted


print("Text 1 Décrypté -> : ")
print(breakcesaradroite(txt1))
print("Text 1 Décrypté <- : ")
print(breakcesaragauche(txt1))
print("Text 2 Décrypté ->: ")
print(breakcesaradroite(txt2))
print("Text 2 Décrypté <-: ")
print(breakcesaragauche(txt2))