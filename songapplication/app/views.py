from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View

# Create your views here.

def songlist(request):
      song = Song.objects.all()
      return render(request,'songlist.html',{'song':song})

def addsong(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        file = request.FILES['file']
        Song.objects.create(title=title, artist=artist, album=album, file=file)
        return redirect('/')
    return render(request, 'addsong.html')


def delete(request, pk):
    song = Song.objects.get(id=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('/')
    return render(request, 'delete.html', {'song': song})


def updateview(request, pk):
    song = Song.objects.get(id=pk)
    
    return render(request, 'update.html', {'song': song})

def update(request):
    
    if request.method == 'POST':
        pk = request.POST['pk']
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        file = request.FILES.get('file')
        song_obj = Song.objects.get(id=pk)
        song_obj.title=title
        song_obj.artist=artist
        song_obj.album=album
        if file:
            song_obj.file=file
        song_obj.save()
   # NewSong.objects.create(title=title, artist=artist, album=album, file=file)
        return redirect('/')
    

def playsong(request, pk):
    song = Song.objects.filter(id=pk)
    #return HttpResponse(f'Now playing: {song.title}') 
    return render(request, 'playsong.html', {'song': song})  


     