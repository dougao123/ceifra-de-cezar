def caesarCipher(s, k):
    resultado = ""
    k = k % 26
    for i in s:
        if i.isalpha():
            if i.isupper():
                base = ord('A')
                resultado += chr((ord(i) - base + k) % 26 + base)
            else:
                base = ord('a')
                resultado += chr((ord(i) - base + k) % 26 + base)
        else:
            resultado += i
    return resultado