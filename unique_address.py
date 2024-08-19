import os
import traceback

try:
    fobj =open('source.ip.txt','r')
    fobj1=open('unique.ip.txt','w')
    content =fobj.readlines()
    uniquecontent=list(set(content))
    fobj1.writelines(uniquecontent)

except Exception as e:
    print(e)

finally:
    fobj.close()
    fobj1.close()
