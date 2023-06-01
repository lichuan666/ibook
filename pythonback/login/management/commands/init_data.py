from datetime import datetime

from django.core.files import File
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model

import os

from login.models import *


class Command(BaseCommand):
    help = '初始化数据'

    def handle(self, *args, **options):
        # 清除所有数据
        self.clear_data()
        # 创建三个测试学生数据
        self.handle_student()
        # 创建三个测试自习室数据
        self.handle_room()
        # 创建自习室座位数据
        self.handle_seat()
        # 创建预约数据
        self.handle_reservation()
        # 添加管理员
        self.handle_admin()
        # 添加warning
        self.handle_warn()

    def clear_data(self):
        # 清除数据
        Student.objects.all().delete()
        Room.objects.all().delete()
        Seat.objects.all().delete()
        Reservation.objects.all().delete()
        Administrator.objects.all().delete()
        Warn.objects.all().delete()

    def handle_student(self):
        student1 = Student.objects.create(name='Tom', password='123456', phone='12345678900', email='tom@example.com',
                                          photo='Student/photo/tom.jpg')
        student2 = Student.objects.create(name='Mary', password='234567', phone='13345678901', email='mary@example.com',
                                          photo='Student/photo/mary.jpg')
        student3 = Student.objects.create(name='John', password='345678', phone='14345678902', email='john@example.com',
                                          photo='Student/photo/john.jpg')
        student1.save()
        student2.save()
        student3.save()

    def handle_room(self):
        # 创建三个测试自习室数据
        room1 = Room(name='自习室1', capacity=50, open_time=datetime.now().strftime("%H:%M:%S"),
                     close_time=datetime.now().strftime("%H:%M:%S"), is_active=True)
        img1_path = os.path.join(settings.BASE_DIR, 'login', 'static', 'img', 'room1.jpg')
        room1_photo = ImageFile(open(img1_path, 'rb'))
        room1.photo.save('room1_photo.jpg', File(room1_photo))
        room1.save()

        room2 = Room(name='自习室2', capacity=40, open_time=datetime.now().strftime("%H:%M:%S"),
                     close_time=datetime.now().strftime("%H:%M:%S"), is_active=True)
        img2_path = os.path.join(settings.BASE_DIR, 'login', 'static', 'img', 'room2.jpg')
        room2_photo = ImageFile(open(img2_path, 'rb'))
        room2.photo.save('room2_photo.jpg', File(room2_photo))
        room2.save()

        room3 = Room(name='自习室3', capacity=60, open_time=datetime.now().strftime("%H:%M:%S"),
                     close_time=datetime.now().strftime("%H:%M:%S"), is_active=True)
        img3_path = os.path.join(settings.BASE_DIR, 'login', 'static', 'img', 'room3.jpg')
        room3_photo = ImageFile(open(img3_path, 'rb'))
        room3.photo.save('room3_photo.jpg', File(room3_photo))
        room3.save()

    def handle_seat(self):
        # 创建5个座位数据
        room1 = Room.objects.get(name='自习室1')
        room2 = Room.objects.get(name='自习室2')
        room3 = Room.objects.get(name='自习室3')

        Seat.objects.create(room=room1, seat_id=1, pos=1, type='普通', state='空闲')
        Seat.objects.create(room=room2, seat_id=1, pos=2, type='靠电', state='空闲')
        Seat.objects.create(room=room3, seat_id=1, pos=3, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=2, pos=4, type='普通', state='关闭')
        Seat.objects.create(room=room1, seat_id=3, pos=5, type='靠电', state='空闲')
        Seat.objects.create(room=room1, seat_id=4, pos=6, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=5, pos=7, type='靠窗', state='空闲')
        Seat.objects.create(room=room1, seat_id=6, pos=8, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=7, pos=9, type='靠电', state='空闲')
        Seat.objects.create(room=room1, seat_id=8, pos=10, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=9, pos=11, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=10, pos=12, type='靠窗', state='空闲')
        Seat.objects.create(room=room1, seat_id=11, pos=13, type='普通', state='空闲')
        Seat.objects.create(room=room1, seat_id=12, pos=14, type='靠电', state='空闲')
        Seat.objects.create(room=room1, seat_id=13, pos=15, type='普通', state='空闲')
        Seat.objects.create(room=room2, seat_id=13, pos=15, type='靠电', state='空闲')

    def handle_reservation(self):
        # Creating a new reservation with status '0'
        from datetime import datetime, timedelta
        room1 = Room.objects.get(name='自习室1')
        seat1 = Seat.objects.get(room=room1, seat_id=1)
        student1 = Student.objects.get(name='Tom')
        start_time1 = datetime.now() + timedelta(hours=1)
        end_time1 = datetime.now() + timedelta(hours=2)
        reservation1 = Reservation.objects.create(
            seat=seat1,
            student=student1,
            start_time=start_time1,
            end_time=end_time1,
            status='0',
        )

        # Creating a new reservation with status '1'
        room2 = Room.objects.get(name='自习室2')
        seat2 = Seat.objects.get(room=room2, seat_id=1)
        student2 = Student.objects.get(name='Mary')
        start_time2 = datetime.now() - timedelta(hours=3)
        end_time2 = datetime.now() - timedelta(hours=2)
        reservation2 = Reservation.objects.create(
            seat=seat2,
            student=student2,
            start_time=start_time2,
            end_time=end_time2,
            status='1',
        )

        # Creating a new reservation with status '4'
        room3 = Room.objects.get(name='自习室3')
        seat3 = Seat.objects.get(room=room3, seat_id=1)  # Assuming there is a Student object with ID 3
        student3 = Student.objects.get(name='John')
        start_time3 = datetime.now() + timedelta(days=1)
        end_time3 = datetime.now() + timedelta(days=1, hours=1)
        reservation3 = Reservation.objects.create(
            seat=seat3,
            student=student3,
            start_time=start_time3,
            end_time=end_time3,
            status='4',
        )

    def handle_admin(self):
        # 添加管理员
        # Creating an active admin
        admin1 = Administrator.objects.create(
            name='admin1',
            password='123456',
            email='admin1@example.com',
            is_active=True,
        )

        # Creating an inactive admin
        admin2 = Administrator.objects.create(
            name='admin2',
            password='123456',
            email='admin2@example.com',
            is_active=True,
        )

        # Creating an admin with a specified date_joined value
        from datetime import datetime
        admin3 = Administrator.objects.create(
            name='admin3',
            password='123456',
            email='admin3@example.com',
            is_active=True,
        )

    def handle_warn(self):
        from datetime import datetime
        student = Student.objects.get(name='Tom')
        warn = Warn.objects.create(
            student=student,
            title='Behavior Warning',
            text='Your behavior in class has been unacceptable. Please meet with me to discuss ways to improve.',
            time=datetime.now(),
            is_active=True,
        )
