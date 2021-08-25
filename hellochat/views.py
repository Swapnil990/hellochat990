from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def sign(request):
    return render(request,"sign.html")

def checkview(request):
    print('c1')
    room = request.POST['room_name']
    print('c2')
    username = request.POST['username']
    print('c3')
    if Room.objects.filter(name=room).exists():
        print('c4')
        return redirect('/'+room+'/?username='+username)

    else:
        print('c5')
        new_room = Room.objects.create(name=room)
        print('c6')
        new_room.save()
        print('c7')
        return redirect('/'+room+'/?username='+username)

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

