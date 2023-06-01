import time

from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
from django_apscheduler.jobstores import DjangoJobStore, register_job
# from django.core.mail import send_mail
from utils.email_tool import send_email
from django.utils import timezone

from login.models import Reservation, Warn


def check_reservation():
    """
    check the reservation before 15 minutes before the start time
    circularly check the reservation 45 minutes every hour
    """
    reservations = Reservation.objects.filter(status=0)
    # filter the reservation today
    cur_time = timezone.now()
    reservations = reservations.filter(start_time__range=(cur_time, cur_time + timezone.timedelta(minutes=30)))
    return reservations


def check_reservation_late():
    """
    check the reservation after 10 minutes after the start time
    circularly check the reservation 15 minutes every hour
    """
    reservations = Reservation.objects.filter(status=0)
    # filter the reservation today
    cur_time = timezone.now()
    reservations = reservations.filter(start_time__range=(cur_time - timezone.timedelta(minutes=30),
                                                          cur_time + timezone.timedelta(minutes=15)))
    return reservations


def check_release_reservation():
    """
    check the reservation after 15 minutes after the start time
    circularly check the reservation 15 minutes every hour
    """
    reservations = Reservation.objects.filter(status=0)
    # filter the reservation today late already
    cur_time = timezone.now()
    reservations = reservations.filter(start_time__range=(cur_time - timezone.timedelta(minutes=16),
                                                          cur_time - timezone.timedelta(minutes=14)))
    return reservations


def release_reservation(reservations: Reservation.objects):
    """
    release the reservation and remind the student
    Warn the student
    """
    if reservations is None:
        return
    for reservation in reservations:
        reservation.status = 2  # Set the reservation status to 2(违约)
        reservation.save()
        stu = reservation.student
        warn = Warn.objects.create(title=f"违约警告-{reservation.start_time}",
                                   text=f"您在{reservation.start_time}预约的{reservation.room}已经被系统释放",
                                   student=stu,
                                   time=timezone.now())
        warn.save()
        mail_content = "You are late, your reservation has been released and you have been warned"
        send_email(to_email=stu.email, mail_content=mail_content)


def get_email_data(reservations: Reservation.objects):
    email_list = []
    time_start_list = []
    time_end_list = []
    student_name = []
    if reservations is None:
        return email_list, student_name, time_start_list, time_end_list
    for reservation in reservations:
        email_list.append(reservation.student.email)
        student_name.append(reservation.student.name)
        time_start_list.append(reservation.start_time)
        time_end_list.append(reservation.end_time)
    return email_list, student_name, time_start_list, time_end_list


def send_a_email(address, name, time_start, time_end, remind_type=0):
    if remind_type == 0:
        content = f"Dear {name},\n" \
                  f"Your reservation from {time_start} to {time_end} is coming soon.\n" \
                  f"Please come to the library on time.\n" \
                  f"Thank you for your cooperation.\n" \
                  f"Best regards,\n" \
                  f"Library"
    else:
        content = f"Dear {name},\n" \
                  f"Your reservation from {time_start} to {time_end} already begin.\n" \
                  f"Please come to the library.\n" \
                  f"Or your reservation will be canceled.\n" \
                  f"And you will be punished.\n" \
 \
    # send email
    subject = 'Reservation Reminder'
    from_email = 'library@qq.com'
    # send_mail(subject, content, from_email, [address], fail_silently=False)
    send_email(to_email=address, mail_content=content)


def remind_job():
    print("remind job begin")
    reservations_list = check_reservation()
    print(len(reservations_list))
    email_list, student_name, time_start_list, time_end_list = get_email_data(reservations_list)
    for i in range(len(email_list)):
        print("send email to", email_list[i])
        print("student name", student_name[i])
        send_a_email(email_list[i], student_name[i], time_start_list[i], time_end_list[i])


def remind_job_again():
    print("remind job again begin")
    reservations_list = check_reservation_late()
    email_list, student_name, time_start_list, time_end_list = get_email_data(reservations_list)
    for i in range(len(email_list)):
        print("send email to", email_list[i])
        print("student name", student_name[i])
        send_a_email(email_list[i], student_name[i], time_start_list[i], time_end_list[i])


def release_reservation_job():
    print("release reservation job begin")
    reservations_list = check_release_reservation()
    release_reservation(reservations_list)

#
# # 实例化调度器
# scheduler = BackgroundScheduler(timezone='Asia/Shanghai')  # 这个地方要加上时间，不然他有时间的警告
# # 调度器使用DjangoJobStore()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
# # 每个小时的45分执行一次remind_job
# scheduler.add_job(remind_job, 'cron', hour='*', minute='45', id="remind_job", replace_existing=True)
# # 每个小时的15分执行一次remind_job_again
# scheduler.add_job(remind_job_again, 'cron', hour='*', minute='15', id="remind_job_again", replace_existing=True)
# # 每个小时的30分执行一次release_reservation
# scheduler.add_job(release_reservation_job, 'cron', hour='*', minute='30', id="release_reservation",
#                   replace_existing=True, )
#
# # 调度器开始运行
# print("start scheduler")
# scheduler.start()


def index(request):
    print("in schedule index")
    remind_job()
    return HttpResponse('ok')
