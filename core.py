


def pack4(a,b,c,d):
#---partie ou on enleve les 0---
    nmove=0
    if c==0:
        if d != 0:
            nmove+=1
        c,d=d,0
    if b==0:
        if c != 0:
            nmove+=1
        b,c,d=c,d,0
    if a==0:
        if b != 0:
            nmove+=1
        a,b,c,d=b,c,d,0
        nmove += 1
#--- ici on enleve 1 aux compteur si les deux premier sont = a 0--
    if a== 0 and b == 0:
        nmove -= 1
#-----partie de fusion--------

    if a==b and a>0:
        a,b,c,d=2*a,c,d,0
        nmove += 1
    if b==c and b>0:
        b,c,d=2*b,d,0
        nmove +=   1
    if c==d and c>0:
        c,d=2*c,0
        nmove +=   1
    return (a,b,c,d,nmove)






#------ zone de test -------
print(pack4(0,0,0,2))
print(pack4(0,0,2,2))
print(pack4(2,0,2,2))
print(pack4(2,2,2,2))
print(pack4(0,2,0,2))
print(pack4(2,2,4,0))
print(pack4(2,2,4,2))
print(pack4(0,2,2,2))
print(pack4(2,0,0,2))
