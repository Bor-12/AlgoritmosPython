"""Dadas tres cadenas s1, s2 y s3, determina si s3 se puede formar intercalando los caracteres de s1 y s2, respetando el orden de cada una."""
def intercalacion_cadenas(s1, s2, s3):

    if len(s1) + len(s2) != len(s3):
        return False

    primera_opcion = False
    segunda_opcion = False

    if s1 and s1[0] == s3[0]:
        primera_opcion = intercalacion_cadenas(s1[1:], s2, s3[1:])
    if s2 and s2[0] == s3[0]:
        segunda_opcion = intercalacion_cadenas(s1, s2[1:], s3[1:])

    return primera_opcion or segunda_opcion


s1 = "abc"
s2 = "def"
s3 = "adbcef"
print(intercalacion_cadenas(s1, s2, s3))
