from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest

from login.models import *
from utils.token import create_token
from rest_framework import serializers

from django.shortcuts import render, HttpResponseRedirect
import json

def login(request):
    print("in login")
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        admin = Administrator.objects.filter(name=name, password=pwd)
        if admin:
            print("Success")
            admin_info = Administrator.objects.get(name=name, password=pwd)
            token = create_token(name)
            response = {
                "status": "success",
                "msg": "登陆成功",
                "name": admin_info.name,
                "id": admin_info.id,
                "token": token
            }
            return JsonResponse(response)
        else:
            msg = "账号或密码错误！！"
            return JsonResponse({"status": "error", "msg": "账号或密码错误！！"}, safe=False,
                                json_dumps_params={'ensure_ascii': False}, status=400)
    if request.method == 'GET':
        return JsonResponse({"status": "error", "msg": "请求方式错误！！"}, safe=False,
                            json_dumps_params={'ensure_ascii': False}, status=400)

#设置座位
def setseat(request):
    print('in setseat')
    #seat_ids = request.POST.getlist('seatIDs')
    #state = request.POST.get('state')
    data = json.loads(request.body.decode('utf-8'))       #如果获取的数据是none就加一下
    seat_ids = data.get('seatIDs')
    state = data.get('state')
    type = data.get('type')
    print(seat_ids,state)
    #assert state in ['on', 'off'] #['启用', '禁用']
    if state == 'on':
        state = '空闲'
    else:
        state = '关闭'
    try:
        result = Seat.objects.filter(id=seat_ids)
        for res in result:
            res.state = state
            res.type = type
            res.save(update_fields=["state","type"])              #更新的话可能要加点内容
        return JsonResponse({"status":"success"})
    except:
        return JsonResponse({"status":"failed"})
            

def statistic(request):
    print('in statistic')
    room_ids = request.POST.getlist('roomIDs',None)
    seat_ids = request.POST.getlist('seatIDs',None)
    start_time = request.POST.get('start_time',None)
    end_time = request.POST.get('end_time',None)
    if room_ids is not None and room_ids != ['']:
        seats = Seat.objects.filter(room_id__in=room_ids)
        seat_ids = [seat.seat_id for seat in seats]
    
    assert seat_ids is not None and seat_ids != ['']
    seat_ids = [int(seat_id) for seat_id in seat_ids]

    # get reservation infos
    class SerializerForRevervation(serializers.ModelSerializer):
        class Meta:
            model = Reservation
            fields = ['id','start_time', 'end_time', 'create_time', 'status', 'seat_id', 'student_id']

    revervations = Reservation.objects.filter(seat_id__in=seat_ids)
    reserve_serializer = SerializerForRevervation(revervations, many=True)
    reserve_data = reserve_serializer.data
    return JsonResponse({"reservations": reserve_data}, safe=False)

#设置教室
def setroom(request):
    print('in setroom')
    data = json.loads(request.body.decode('utf-8'))       #
    room_ids = data.get('roomIDs')    
    state = data.get('state')
    open_time = data.get('open_time')
    close_time = data.get('close_time')
    print(state,open_time,close_time)

    try:
        print("roomid:",room_ids)
        rooms = Room.objects.filter(id=room_ids)
        print("which room:",rooms)
        #print("imfo:",rooms.capacity,rooms.photo)
        for room in rooms:
            if state == 'on':
                room.is_active = 1
            else:
                room.is_active = 0
            room.open_time = open_time
            room.close_time = close_time
        #rooms.update(is_active = is_active, open_time = open_time,close_time = close_time)
            room.save(update_fields=["is_active","open_time","close_time"])          #此处有问题
        print("come here???")
        return JsonResponse({"status":"success"})
    except:
        return JsonResponse({"status":"failed"})
    '''
    room_ids = request.POST.getlist('roomIDs')     #原版
    state = request.POST.get('state')
    open_time = request.POST.get('open_time', None)
    close_time = request.POST.get('close_time', None)
    print(state,open_time,close_time)

    try:
        print("roomid:",room_ids)
        rooms = Room.objects.filter(id__in=room_ids)
        print("which room:",rooms)
        for room in rooms:
            if state is not None and state is not '':
                room.is_active = 1 if state == '启用' else 0
            if open_time is not None and open_time is not '':
                room.open_time = open_time
            if close_time is not None and close_time is not '':
                room.close_time = close_time
            room.save()
        return JsonResponse({"status":"success"})
    except:
        return JsonResponse({"status":"failed"})
    '''