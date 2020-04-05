from django.shortcuts import render
from .forms import CodePostForm
import sqlite3
from subprocess import Popen, PIPE
def post_share(request):
    sent=False
    if request.method == 'POST':
        form = CodePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            conn = sqlite3.connect('C:/Users/user/Documents/GitHub/testing/mysite/testing/ONLINESHOP.db')
            c = conn.cursor()
            c.execute(cd['code'])
            otv=""
            for res in c.fetchall():
                otv+=str(res)
            c.close()
            sent=True
            return render(request, 'share.html', {'form': form,'sent':sent,'result':otv})
        else:
            form=CodePostForm()
            return render(request, 'share.html',{'form': form})
    else:
        return render(request, 'share.html', {'form': CodePostForm()})