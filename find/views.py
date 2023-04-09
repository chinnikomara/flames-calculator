from django.shortcuts import render
#from django.http import 
import random
from .models import Destiny
def show(request):
    return render(request,'home.html')
def res(request):
    dest=Destiny()
    name1=request.GET["name1"]
    n1=name1.upper()
    name2=request.GET["name2"]
    n2=name2.upper()
    f='FLAMES'
    flist=list(f)
    alist=list(n1)
    blist=list(n2)
    for i in alist:
        if i in blist:
            alist.remove(i)
            blist.remove(i)
    alist.extend(blist)
    for s in alist:
        if s==' ':
            alist.remove(s)
    l=len(alist)
    while(len(flist)!=1):
        fl=len(flist)
        r=l%fl
        flist.pop(r-1)
    if flist[0]=='F':
        z='Friends..!'
        dest.img='b_freinds.gif'
    elif flist[0]=='L':
        z='Lovers..!'
        i1='b_love.gif'
        i2='b_love2.gif'
        dest.img=random.choice([i1,i2])
    elif flist[0]=='A':
        z='Attraction..!'
        i1='attraction1.gif'
        i2='b_attraction.gif'
        dest.img=random.choice([i1,i2])
    elif flist[0]=='M':
        z='Marriage..!'
        i1='b_marriage.gif'
        i2='b_marriage2.gif'
        dest.img=random.choice([i1,i2])
    elif flist[0]=='E':
        z='Enemies..!'
        i1='enemies1.gif'
        i2='b_enemies.gif'
        dest.img=random.choice([i1,i2])
    elif flist[0]=='S':
        z='Sister / Brother..!'
        i1='b_sister.gif'
        i2='b_sister2.gif'
        i3='b_sister3.gif'
        dest.img=random.choice([i1,i2,i3])
    dest.out=z
    dest.bg='b_background.gif'
    return render(request,'result.html',{'dest1':dest})