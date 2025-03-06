a = "1. Oitlt xlt onb ovjtc bd jtbjqt nib ngqq otqq vbr oixo vbr zxmmbo yxkt x egddtltmzt gm oigc nblqe: oibct nib xlt xdlxge ob olv xme oibct nib xlt xdlxge vbr ngqq crzztte Crzztcc gc qgkgmu vbrlctqd, qgkgmu nixo vbr eb, xme qgkgmu ibn vbr eb go Nitmtftl vbr dgme vbrlctqd bm oit cget bd oit yxwblgov, go gc ogyt ob jxrct xme ltdqtzo Kttj vbrl dxzt xqnxvc obnxle oit crmcigmt xme cixebnc ngqq dxqq htigme vbr Gd vbr ixft tftlvoigmu rmetl zbmolbq, vbr xlt mbo ybfgmu dxco tmbrui Go gc erlgmu brl exlktco ybytmoc oixo nt yrco dbzrc ob ctt oit qguio"

def cifraCesar(cadena, llave):
    if llave < 0:
        llave = 24 - llave
    cadena = cadena.lower()
    nuevaCadena = ""
    #alfabeto = "abcdefghijklmnopqrstuvwxyz" #26 Aleman
    #alfabeto = "abcdefghijklmnopqrstuvxyz" #25 Frances
    #alfabeto = "abcdefghijklmnopqrstuvwxyz" #26 Ingles
    #alfabeto = "abcdefghijlmnopqrstuvxz" #23 Italiano
    alfabeto = "abcdefghijlmnopqrstuvxyz" #24 Portugues
    for l in cadena:
        if l in alfabeto:
            posicionLetra = alfabeto.find(l)
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra + llave) % 24)]
        else:
            nuevaCadena = nuevaCadena + l
    return nuevaCadena

def descifraCesar(cadena, llave):
    return cifraCesar(cadena, 24 - llave)


for llave in range(24):
    prueba = descifraCesar(a , llave)
    print (llave, prueba)
    print ()
    





