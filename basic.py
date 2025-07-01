# secret code program
import random
import string
while True:
    try:
        st = input("Enter a secret code\nor type 0 to exit: ")
        if st == "0":
            print("Thank you for using this")
            break
        words = st.split()
        coding = int(input("Enter 1 for coding or 2 for decoding: "))
        coding = True if coding == 1 else False
        print(coding)
        if (coding): 
            nwords = []
            for word in words:
                if (len(word) >= 4):
                    r1 = ''.join(random.choices(string.ascii_lowercase, k=2))
                    r2 = ''.join(random.choices(string.ascii_lowercase, k=2))
                    new_word = r1 + word[1:] + word[0] + r2
                    nwords.append(new_word)
                else:
                    nwords.append(word[::-1])
            print(' '.join(nwords))

        else:            
            nwords = []
            for word in words:
                if (len(word) >= 4):
                    stnew = word[2:-2]
                    stnew = stnew[-1] + stnew[:-1]  
                    nwords.append(stnew)
                else:
                    nwords.append(word[::-1])
            print(' '.join(nwords))
    except:
        break                