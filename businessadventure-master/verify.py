def verify_mail(m):
    retour = False
    l = len(m)
    x = 0
    if l > 40 :
        retour = False
    else:
        for x in range (0,l,1):
            if x >= 6 and m[x] == '@' and (m[l-3] =='.' or m[l-4]=='.'):
                retour = True
    return retour


        
    