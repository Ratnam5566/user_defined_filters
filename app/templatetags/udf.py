from django import template
register=template.Library()
import re



@register.filter()
def udf(data):
    return data.upper()

@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def count(data,char):
    c=0
    for i in data:
        if i==char:
            c+=1
    return c


@register.filter()
def count1(data,arg):
    x=re.findall('[arg]',data)
    return len(x)


@register.filter()
def remove1(data):
    l=data.split()
    x=[]
    for i in range(len(l)):
        if i!=0 or i!=len(l)-1:
            x.append(l[i].upper())
        else:
            x.append(l[i])
    return ' '.join(x)
