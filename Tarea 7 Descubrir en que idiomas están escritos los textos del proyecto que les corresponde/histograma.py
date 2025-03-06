# Tarea 7

texto1 = "Oitlt xlt onb ovjtc bd jtbjqt nib ngqq otqq vbr oixo vbr zxmmbo yxkt x egddtltmzt gm oigc nblqe: oibct nib xlt xdlxge ob olv xme oibct nib xlt xdlxge vbr ngqq crzztte Crzztcc gc qgkgmu vbrlctqd, qgkgmu nixo vbr eb, xme qgkgmu ibn vbr eb go Nitmtftl vbr dgme vbrlctqd bm oit cget bd oit yxwblgov, go gc ogyt ob jxrct xme ltdqtzo Kttj vbrl dxzt xqnxvc obnxle oit crmcigmt xme cixebnc ngqq dxqq htigme vbr Gd vbr ixft tftlvoigmu rmetl zbmolbq, vbr xlt mbo ybfgmu dxco tmbrui Go gc erlgmu brl exlktco ybytmoc oixo nt yrco dbzrc ob ctt oit qguio"
texto2 = "Jz bzz qwjjd ped nevvd le vkzhd eo mod hdlvd kelwkhd odvmkdjw d neknd hwove naejzpwvke qe qelvdobd. Vmvvd jd bzod w qwjepevdvd odvmkdjpwovw qd gdkwve kznnezlw z kegeqe gwoqee, umeoqe gwk jd pdffezk gdkvw qwfje doepdje ozo lzoz ownwlldkew fdccew, ow lgwnedje kwneolezoe. Lzjz rwjeoe dcevdoz j'oend gdkvw naemld, naw ad qe rdjvz jd lvwlld vkelvwbd qwe jzkz znnae kdllwfodve. Lzoz dggwod dkkehdvz eo Evdjed wq w mo jmzfz qdhhwkz eondovwhzjw. Ewke az helevdvz ej nwovkz qe Kzpd w qwhz qekw naw w qdhhwkz mod nevvd nzo pzjve pzompwove dovenae, eordvve lzoz keldjwove djj’wgznd Kzpdod. Az helvz ej Nzjzllwz w qwhz dppwvvwkw naw gwoldhz rzllw gem gennzjz, eohwnw w fkdoqw wq w qdhhwkz mo cwj pzompwovz, gwnndvz naw ozo lzoz kemlnevz dq wovkdkw."

# Para texto 1

histo = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for c in alfabeto:
    histo[c] = 0
for c in texto1:
    if c in alfabeto:
        histo[c] += 1

cad = ""
for c in histo.keys():
    cad += c + "," + str(histo[c]) + "\n"

arch = open("salida1.csv", 'w')
arch.write(cad)
arch.close()

# Para texto 2

histo = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for c in alfabeto:
    histo[c] = 0
for c in texto2:
    if c in alfabeto:
        histo[c] += 1

cad = ""
for c in histo.keys():
    cad += c + "," + str(histo[c]) + "\n"

arch = open("salida2.csv", 'w')
arch.write(cad)
arch.close()
