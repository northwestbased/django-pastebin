from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from random import randint
from collections import ChainMap

from tempfile import TemporaryFile
from .language import language
from .models import Paste, Comment

def index(request):
    latest_paste_list = Paste.objects.order_by('-pub_date').filter(public=True)[:10]
    context = {'latest_paste_list': latest_paste_list, 'language': language}
    return render(request, 'pastebin/index.html', context)

def detail(request, paste_id):
    paste = get_object_or_404(Paste, key=paste_id)
    return render(request, 'pastebin/detail.html', {'paste':paste})

def paste(request):
    text = request.POST['text']
    title = request.POST['title']
    syntax = request.POST['syntax']
    if title is "":
        title = "Untitled";
    if "public" in request.POST:
    	public = True
    else:
        public = False
    key = ''
    for i in range(0,10):
        char = randint(48, 122)
        while char > 90 and char < 97 or char > 57 and char < 65:
            char = randint(48, 122)
        key += chr(char)
    languages = ChainMap(*language);

    paste = Paste(title=title, text=text, public=public, pub_date=timezone.now(), key=key, syntax=languages[syntax])
    paste.save()
    return redirect("/%s" % key)

def getpaste(request, paste_id):
    a = get_object_or_404(Paste, key=paste_id).text
    response= HttpResponse(a, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="%s.txt"' % paste_id
    return response;

def createcomment(request, key):
    text = request.POST['text']
    title = request.POST['title']
    if title is "":
      title = "None";
    paste = get_object_or_404(Paste, key=key)
    comment = Comment(title=title, text=text, pub_date=timezone.now(), paste=paste)
    comment.save()
    return redirect("/%s" % key)
