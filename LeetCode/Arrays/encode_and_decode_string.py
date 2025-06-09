#Problema 271 (es de pago , hacerlo en lintcode
from typing import List
def encode(strs: List[str]) -> str:
    palabra_codificada = ""
    for palabra in strs:
        numero_letras = str(len(palabra))
        palabra_codificada = palabra_codificada + numero_letras + "#" + palabra
    return palabra_codificada
def decode(s: str) -> List[str]:
    palabras_decodificadas, i  = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        longitud_palabra = int(s[i:j])
        palabra_decodificada = s[j + 1: j + longitud_palabra + 1]
        palabras_decodificadas.append(palabra_decodificada)
        i  = j + 1 + longitud_palabra
    return palabras_decodificadas

print(decode(encode(["neet", "code", "love", "you"]
)))
