from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message

from .forms import RoomForm

from django.utils.text import slugify

# Create your views here.

@login_required(login_url='login')
def list_rooms_view(request):
    rooms = Room.objects.all()
    
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required(login_url='login')
def create_room_view(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            try:
                last_id = Room.objects.latest('id').id
            except Room.DoesNotExist:
                last_id = 0
            room = form.save(commit=False)
            room.slug = slugify(f"{room.name}-{last_id}")
            room.save()
            return redirect('rooms')

    form = RoomForm()
    context = {
        'form': form
    }
    return render(request, 'room/room_create.html', context)

@login_required(login_url='login')
def detail_room_view(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required(login_url='login')
def delete_room_view(request, slug):
    room = Room.objects.get(slug=slug)
    room.delete()
    return redirect('rooms')

