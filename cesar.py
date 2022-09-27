import string 

txt1 = "NWLAHYCXPAJYQRNUNLQROOANVNWCYJAMNLJUJPNJDBBRLXWWDLXVVNUNLQROOANMNLNBJAXDUNLXMNMNLNBJANBCDWNVNCQXMNMNLQROOANVNWCCANBBRVYUNDCRURBNNYJASDUNBLNBJAMJWBBNBLXAANBYXWMJWLNBBNLANCNB"
txt2 = "vcfgrwqwfsbhfsntowbsobgfsbhfsnqvsnjcigsghqsoixcifrviwtshseicwbsgojsnjcigdogeisjcigoihfsgofhwgobgjcigbsrsjsnqwfqizsfrobgzsgfisgzsgxcifgcijfopzsgeiojsqzsggwubsgrsjchfsdfctsggwcbdofzseiszsghhcbashwsf"
alphabet = string.ascii_uppercase

def breakcaesar(s1):
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



print("Text 1 Décrypté : ")
print(breakcaesar(txt1))
print("Text 2 Décrypté : ")
print(breakcaesar(txt2))