from collections import Counter

from django.http import JsonResponse
from django import forms
from rest_framework import serializers

from datetime import datetime, timedelta

from login.models import *      #login.models
import json


# This is the timerange form, including start time and end time
class TimeForm(forms.Form):
    start_time = datetime.now().replace(minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(hours=24)

    # Add a time form which can choose the time
    start_time_form = forms.DateTimeField(
        label='预约开始时间',
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'min': start_time, 'max': end_time}
        )
    )
    end_time_form = forms.DateTimeField(
        label='预约结束时间',
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'min': start_time + timedelta(hours=1), 'max': end_time}
        )
    )


# 使用Serializer序列化数据，直接返回json数据即可
class RoomSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'open_time', 'close_time']


# Rooms students can see
def stu_room_available(request):
    print("in room_available")

    room_query_set = Room.objects.filter(is_active=True)
    room_serializer = RoomSerializerForStudent(room_query_set, many=True)
    room_data = room_serializer.data
    return JsonResponse({"room_list": room_data}, safe=False)


class SeatSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_id', 'pos', 'type', 'state']


def seat(request):
    print("in seat")

    if request.method == "GET":
        room_id = request.GET.get('room_id')
        room_obj = Room.objects.get(id=room_id)
        room_list = Room.objects.all()
        room_id = request.GET.get('room_id')
        if room_id:
            room = Room.objects.get(id=room_id)
            if room.is_active:
                seat_query_set = Seat.objects.filter(room=room)
                seat_serializer = SeatSerializerForStudent(seat_query_set, many=True)
                seat_data = seat_serializer.data
                return JsonResponse({"seat_list": seat_data}, safe=False)
            else:
                return JsonResponse({"status": "error", "msg": "该自习室已被关闭！"})
    elif request.method == "POST":
        # search for seat
        seat_type = request.POST.get('type')
        seat_pos = request.POST.get('pos')
        seat_room = request.POST.get('room_id')
        seat_list = Seat.objects.all()
        if seat_type is not None:
            seat_list = seat_list.filter(type=seat_type)
        if seat_pos is not None:
            seat_list = seat_list.filter(pos=seat_pos)
        if seat_room is not None:
            seat_list = seat_list.filter(room=seat_room)
        seat_serializer = SeatSerializerForStudent(seat_list, many=True)
        seat_data = seat_serializer.data
        return JsonResponse({"seat_list": seat_data}, safe=False)

    else:
        return JsonResponse({"status": "error", "msg": "请求方法错误！"})

#预约座位
def exe_reservation(request):
    
    print("in reservation")
    '''
    username = request.META.get('HTTP_USERNAME')
    stu_id = Student.objects.get(name=username).id
    student_obj = Student.objects.get(id=stu_id)
    #print(username,stu_id,student_obj)
    '''    

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))       #如果获取的数据是none就加一下
        '''
        room_id = request.POST.get('room_id')
        seat_id = request.POST.get('seat_id')
        the_seat = Seat.objects.get(room_id=room_id, pos=seat_id)
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        '''
        room_id = data.get('room_id')
        seat_id = data.get('seat_id')
        id = data.get('sid')
        student_obj = Student.objects.get(id=id)             
        the_seat = Seat.objects.get(id=room_id, pos=seat_id)
        print(the_seat)
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        
        # transform the time format
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        print(start_time,end_time)
        # Check if the person has a reservation
        if Reservation.objects.filter(student=student_obj, status=1).exists():
            return JsonResponse({"status": "error", "msg": "您已有预约！"})

        # create a reservation
        reservation_obj = Reservation.objects.create(
            student_id=id,
            seat_id=seat_id,
            start_time=start_time,
            end_time=end_time,
            status=1
        )
        reservation_obj.save()

        return JsonResponse({"status": "success", "msg": "预约成功！"})
    else:
        return JsonResponse({"status": "error", "msg": "预约失败！"})


class ReservationSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['seat', 'start_time', 'end_time', 'status']


def view_reservation(request):
    print("in view reservation")

    username = request.META.get('HTTP_USERNAME')
    stu_id = Student.objects.get(name=username).id

    if request.method == "GET":
        reservation_query_set = Reservation.objects.filter(student_id=stu_id)
        reservation_serializer = ReservationSerializerForStudent(reservation_query_set, many=True)
        reservation_data = reservation_serializer.data
        return JsonResponse({"reservation_list": reservation_data}, safe=False)

    elif request.method == "POST":
        reservation_id = request.POST.get('reservation_id')
        reservation_obj = Reservation.objects.get(id=reservation_id)
        reservation_obj.status = 3  # update the status
        reservation_obj.save()
        return JsonResponse({"status": "success", "msg": "取消成功！"})


class WarnSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Warn
        fields = ['title', 'text', 'time', 'is_active']


def view_my_warn(request):
    username = request.META.get('HTTP_USERNAME')
    stu_id = Student.objects.get(name=username).id
    warn_query_set = Warn.objects.filter(student_id=stu_id)
    warn_serializer = WarnSerializerForStudent(warn_query_set, many=True)
    warn_data = warn_serializer.data
    return JsonResponse({"warn_list": warn_data}, safe=False)


def sign(request):
    print("in sign")
    username = request.META.get('HTTP_USERNAME')
    student_obj = Student.objects.get(name=username)
    if request.method == "POST":
        cur_time = request.POST.get('cur_time')
        seat_id = request.POST.get('seat_id')
        # transform the time format
        cur_time = datetime.strptime(cur_time, "%Y-%m-%d %H:%M:%S")
        try:
            the_reservation = Reservation.objects.get(student=student_obj, seat_id=seat_id)
            if the_reservation:
                reservation_start_time = the_reservation.start_time
                if the_reservation.status == "1":
                    return JsonResponse({"status": "error", "msg": "签到失败！您已签到！"})
                if reservation_start_time - timedelta(minutes=10) > cur_time:
                    return JsonResponse({"status": "error", "msg": "签到失败！签到时间未到！"})
                if reservation_start_time + timedelta(minutes=5) < cur_time:
                    return JsonResponse({"status": "error", "msg": "签到失败！签到时间已过！"})
                the_reservation.status = 1
                the_reservation.save()
                return JsonResponse({"status": "success", "msg": "签到成功！"})
        except Reservation.DoesNotExist:
            return JsonResponse({"status": "error", "msg": "签到失败！对象不存在！"})


def recommend(request):
    """根据用户的历史预定记录，推荐自习室"""
    username = request.META.get('HTTP_USERNAME')
    student_obj = Student.objects.get(name=username)
    the_reservations = Reservation.objects.filter(student=student_obj).order_by('-start_time')
    # order by the seat_id group count
    seat_id_list = [re.seat_id for re in the_reservations]
    # figure out the most frequent seat
    seat_id_count = Counter(seat_id_list)
    seat_id_count = sorted(seat_id_count.items(), key=lambda x: x[1], reverse=True)

    # figure out the top 3 seat
    topK = 3
    if len(seat_id_count) < 3:
        topK = len(seat_id_count)
    topK_seat_id = [seat_id_count[i][0] for i in range(topK)]

    seat_query_set = Seat.objects.filter(id__in=topK_seat_id)
    seat_serializer = SeatSerializerForStudent(seat_query_set, many=True)
    seat_data = seat_serializer.data
    return JsonResponse({"seat_list": seat_data}, safe=False)


