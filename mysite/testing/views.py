from django.shortcuts import render
from .forms import CodePostForm
import os
from subprocess import Popen, PIPE
def post_share(request):
    sent=False
    if request.method == 'POST':
        form = CodePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sql_code=""" 
import sqlite3 
import pprint 
conn = sqlite3.connect('C:/Users/user/Documents/GitHub/testing/mysite/testing/ONLINESHOP.db') 
c = conn.cursor()
c.execute('''
"""+cd['code']+""" ''')
pprint.pprint(c.fetchall(),indent=5,width=60,compact=False) 
c.close()
"""
            fl = open("C:/Users/user/Documents/GitHub/testing/mysite/testing/testingit.py", "w+")
            fl.write(sql_code)
            fl.close()
            otv=""
            result = Popen(['python', 'C:/Users/user/Documents/GitHub/testing/mysite/testing/testingit.py'], stdout=PIPE, bufsize=1)
            for example in iter(result.stdout.readline, b''):
                otv+=str(example)
            os.remove('C:/Users/user/Documents/GitHub/testing/mysite/testing/testingit.py')
            sent=True
            return render(request, 'share.html', {'form': form,'sent':sent,'result':otv})
        else:
            form=CodePostForm()
            return render(request, 'share.html',{'form': form})
    else:
        return render(request, 'share.html', {'form': CodePostForm()})