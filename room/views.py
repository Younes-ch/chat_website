from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message

# Create your views here.

@login_required(login_url='login')
def list_rooms_view(request):
    rooms = Room.objects.all()
    
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required(login_url='login')
def detail_room_view(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
