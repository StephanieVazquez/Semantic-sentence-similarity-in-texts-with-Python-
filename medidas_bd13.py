import math
from nltk import bigrams
import collections

def jacard(cadena1,cadena2):
    lista1=cadena1.split(" ") 
    lista2=cadena2.split(" ")
    interseccion = set(lista1)& set(lista2)
    union = set(lista1)|set(lista2)
    return float(float(len(interseccion)))/float(float(len(union)))
     
def super_posicion_terminos(cadena1,cadena2):
    lista1=cadena1.split(" ") 
    lista2=cadena2.split(" ")
    interseccion = set(lista1)& set(lista2)
    return float(len(interseccion)/min(len(lista1),len(lista2)))

def bhattacharyya(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    suma=0
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    for i in range(len(contar_p1)):
        suma=suma+math.sqrt(contar_p1[i]*contar_p2[i])
    return (suma)

def euclidiana(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    suma_euc=0
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    for i in range(len(contar_p1)):
        suma_euc=suma_euc+(contar_p1[i]-contar_p2[i])**2
    suma_eucfinal=math.sqrt(suma_euc)
    return float(suma_eucfinal)
    
def manhattan(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    suma_manh=0
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    for i in range(len(contar_p1)):
        suma_manh=suma_manh +abs(contar_p1[i]-contar_p2[i])
    return float(suma_manh)

def levenshtein(str1, str2):
  d=dict()
  for i in range(len(str1)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(str2)+1):
     d[0][i] = i
  for i in range(1, len(str1)+1):
     for j in range(1, len(str2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
  return d[len(str1)][len(str2)]

def chebyshev(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    res=[]
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    for i in range(len(contar_p1)):
        res.append(abs(contar_p1[i]-contar_p2[i]))
    return(max(res))

def dice(cadena1,cadena2):
    lista1=cadena1.split(" ") 
    lista2=cadena2.split(" ")
    interseccion = set(lista1)& set(lista2)
    long= len(lista1)+ len(lista2)
    c_dice=2*float(len(interseccion)/long)
    return c_dice

def jackie(cad1,cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    a=[]
    b=[]
    for r in vocabulario:
        if r in list1:
            a.append(1)
        else:
            a.append(0)
        if r in list2:
            b.append(1)    
        else:
            b.append(0)
    ####producto punto
    sum_total=0
    for i in a:
        sum_aux=0
        for j in b:
            sum_aux=sum_aux+(i*j)
        sum_total=sum_total+sum_aux
    sim=(2*sum_total)/(2*(len(a)*len(a)))
    return sim

def pearson(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    #print vocabulario
    contar_p1=[]
    contar_p2=[]
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    sumxy=0
    sumx=0
    sumy=0
    sumx2=0
    sumy2=0
    n=len(contar_p1)
    for i in range(len(contar_p1)):
        sumx=sumx+contar_p1[i]
        sumx2=sumx2+(contar_p1[i]*contar_p1[i])
        sumy=sumy+contar_p2[i]
        sumy2=sumy2+(contar_p2[i]*contar_p2[i])
        sumxy=sumxy+(contar_p1[i]*contar_p2[i])
    try:
        r=(sumxy-(sumx*sumy/n))/(math.sqrt((sumx2-((sumx*sumx)/n))*(sumy2-((sumy*sumy)/n))))
    except ZeroDivisionError:
        r=-1
    return(r)

def pmi(w, t, corpus, pw1, count_pl2):
    bg=collections.Counter(bigrams(corpus))
    n_bg=0
    ##numero total de bigramas
    for i in bg:
        n_bg=n_bg+bg[i]
    
    l2=len(t)
    sim_max=0
    for i in t:
            pw2=count_pl2[i]/l2
            aau='('+ w + ', ' + i +')'
            if aau in bg:
                val=bg[aau]/n_bg
            else:
                val=0
            try:
                sim=math.log2(val/(pw1*pw2))
            except ValueError:
                sim=-float('inf')
            if sim>sim_max:
                sim_max=sim       
    return sim_max

def jaro(cad1,cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    m=0
    t=0
    for i in range(len(list1)):
        try:
            if list1[i]==list2[i]:
                m=m+1
        
            else:
                if list1[i] in list2:
                    t=t+(1)
        except IndexError:
            pass
    try:
        dj=float((1/3)*((m/len(list1))+(m/len(list2))+((m-t)/m)))
    except ZeroDivisionError:
        dj=0
    return(dj)

def conjunto(cad1,cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    
    a=len(list1)-len(list2)
    b=len(list2)- len(list1)
    c=len(set(list1)-set(list2))
    d=len(set(list2)-set(list1))
    maximo=max(a,b,c,d)
    return(maximo)

def canberra(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    #print vocabulario
    contar_p1=[]
    contar_p2=[]
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    suma=0
    for i in range(len(contar_p1)):
        suma=suma+(abs(contar_p1[i]-contar_p2[i])/(contar_p1[i]+contar_p2[i]))
    return (suma)

def rada(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    l1=len(list1)
    l2=len(list2)
    corpus=list1+list2
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    idf={}
    count_pl1={}
    count_pl2={}
    for x in range(len(vocabulario)):
        if vocabulario[x] in list1:
            contar_p1.append(1)
            count_pl1[vocabulario[x]]=list1.count(vocabulario[x])
        else:
            contar_p1.append(0)
        if vocabulario[x] in list2:
            contar_p2.append(1)
            count_pl2[vocabulario[x]]=list2.count(vocabulario[x])
        else:
            contar_p2.append(0)  
    for i in range(len(contar_p1)):
        idf[vocabulario[i]]=2/(contar_p1[i]+contar_p2[i])#calculo de idf en hash
    sumatoria_a=0
    sumatoria_b=0
    t_idf=0
    t_idf2=0
    for i in list1:
        pw1=float(count_pl1[i]/l1)
        sumatoria_a=sumatoria_a+(pmi(i,list2, corpus, pw1, count_pl2)*idf[i])
        t_idf=idf[i]+t_idf
    for i in list2:
        pw1=float(count_pl2[i]/l2)
        sumatoria_b=sumatoria_b+(pmi(i,list1, corpus, pw1, count_pl1)*idf[i])
        t_idf2=idf[i]+t_idf2
    s_rada=0.5*((sumatoria_a/t_idf) +  (sumatoria_b/t_idf2))
    return (s_rada)

def simCos(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    sum_a=0
    raiz_a=0
    raiz_b=0
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    for i in range(len(contar_p1)):
        sum_a=sum_a+(contar_p1[i]*contar_p2[i])
        raiz_a=raiz_a+(contar_p1[i]*contar_p1[i])
        raiz_b=raiz_b+(contar_p2[i]*contar_p2[i])
    raiz_a=math.sqrt(raiz_a)
    raiz_b=math.sqrt(raiz_b)
    sim_cos=(sum_a)/(raiz_a*raiz_b)
    return sim_cos

def tanimoto(cad1, cad2):
    list1=cad1.split(" ") 
    list2=cad2.split(" ")
    vocabulario = set(list1)|set(list2)
    vocabulario=list(vocabulario)
    contar_p1=[]
    contar_p2=[]
    for x in range(len(vocabulario)):
        contar_p1.append(list1.count(vocabulario[x]))
        contar_p2.append(list2.count(vocabulario[x]))
    pro=0
    for i in contar_p1:
        sum_aux=0
        for j in contar_p2:
            sum_aux=sum_aux+(i*j)
        pro=pro+sum_aux
    try:
        sim=pro/(((len(list1)**2)*(len(list2)**2))-pro)
    except ZeroDivisionError:
        sim=0
    return(sim)

def hamming(cad1, cad2):
    lista1 = cad1.split(" ")
    h = []
    for i in lista1:
        if i != "":
            h.append(i)
    r = 0
    lista2 = cad2.split(" ")
    for j in lista2:
        if j != "" and j not in h:
            r += 1
    return r

###########################################

entrada = open("test.txt","r")
salida = open("salida_test_13.arff","w")


salida.write("@relation train_predicted" + "\n" +"@attribute atributo1 numeric" + "\n" +
    "@attribute atributo2 numeric" + "\n" +"@attribute atributo3 numeric" + "\n" +
    "@attribute atributo4 numeric" + "\n" + "@attribute atributo5 numeric" + "\n" +
    "@attribute atributo6 numeric" + "\n" + "@attribute atributo7 numeric" + "\n" +
    "@attribute atributo8 numeric" + "\n" + "@attribute atributo9 numeric" + "\n" +
    "@attribute atributo10 numeric" + "\n" + "@attribute atributo11 numeric" + "\n" +
    "@attribute atributo12 numeric" + "\n" + "@attribute atributo13 numeric" + "\n" +
    "@attribute atributo14 numeric" + "\n" + "@attribute atributo15 numeric" + "\n" +
    "@attribute atributo16 numeric" + "\n" + "\n" + "@attribute tipo {4,5,0,1,2,3}"  + "\n" +"@data"+"\n")


for linea in entrada.readlines():
   linea=linea.lower()
   linea=linea.replace("\n","")
   sentencia=linea.split("\t")
   if len(sentencia)>2:
       rjacard = jacard(sentencia[0],sentencia[1])
       reuclidiana = euclidiana(sentencia[0], sentencia[1])
       rmanhattan = manhattan(sentencia[0],sentencia[1])
       rleven = levenshtein(sentencia[0], sentencia[1])
       coseno=simCos(sentencia[0],sentencia[1])
       #sim_rada=rada(sentencia[0],sentencia[1])
       sim_che=chebyshev(sentencia[0],sentencia[1])
       sim_dice=dice(sentencia[0],sentencia[1])
       sim_j=jackie(sentencia[0],sentencia[1])
       sim_jaro=jaro(sentencia[0],sentencia[1])
       sim_con=conjunto(sentencia[0],sentencia[1])
       sim_pear=pearson(sentencia[0], sentencia[1])
       sim_canberra=canberra(sentencia[0], sentencia[1])
       sim_super=super_posicion_terminos(sentencia[0],sentencia[1])
       sim_bha=bhattacharyya(sentencia[0], sentencia[1])
       sim_tani=tanimoto(sentencia[0], sentencia[1])
       sim_ham=hamming(sentencia[0], sentencia[1])
       """
       salida.write(str(rjacard) + " " + str(reuclidiana) + " " + str(rmanhattan)
       + " " + str(rleven) + " "+ str(coseno) + " "+ 
        str(sim_che)+" " + str(sim_dice) +" "+ str(sim_j) +" "+ str(sim_jaro) +
       " " + str(sim_pear)+" "+ str(sim_canberra)+" "+str(sim_super)+" "+
       str(sim_bha)+" "+str(sim_tani)+ " "+  "?" + "\n")
       """
       
       salida.write(str(rjacard) + " " + str(reuclidiana) + " " + str(rmanhattan)
       + " " + str(rleven) + " "+ str(coseno) + " "+ 
       str(sim_che)+ " " + str(sim_dice) +" "+ str(sim_j) +" "+ str(sim_jaro) + " "+ str(sim_con)
       +" "+str(sim_pear)+" "+ str(sim_canberra)+" "+str(sim_super)+" "+ str(sim_bha)+" "+
       str(sim_tani)+ " "+ str(sim_ham)+ " "+ "?" + "\n")