import re


 def function(m): 
   if (m.group(0)=='&amp;'):
     return '&'
   
   
   elif (m.group(0)=='&gt;'):
     return '>'


   elif (m.group(0)=='&lt;'):
     return '<'


   else:
     return ' '	


 
q1 = re.compile('<title>(.+?)</title>')	
q2 = re.compile('<!--.*?-->',re.DOTALL)  
q3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) 
q4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 
q51 = re.compile(r'<.+?>|</.+?>',re.DOTALL) 
q52 = re.compile(r'<.+?/>',re.DOTALL) 
q6 = re.compile(r'&(amp|gt|lt|nbsp);') 
q7 = re.compile(r'\s+')



with open('testpage.txt','r') as fp:



   tx = fp.read() 
   m = q1.search(tx) 
   print(m.group(1))	
   tx = q2.sub(' ',tx)
   tx = q3.sub(' ',tx) 
   for m in q4.finditer(tx): 
     print('{}    {}'.format(m.group(1),m.group(2)))
   tx = q51.sub(' ',tx) 
   tx = q52.sub(' ',tx) 
   tx = q6.sub(function,tx) 
   tx = q7.sub(' ',tx) 
   print(tx)
