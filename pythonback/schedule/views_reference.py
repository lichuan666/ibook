from django.http import HttpResponse

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job

from login.models import Reservation

"""
reference:
https://itutd.blog.csdn.net/article/details/129935390?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-129935390-blog-123926503.235%5Ev35%5Epc_relevant_increate_t0_download_v2_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-129935390-blog-123926503.235%5Ev35%5Epc_relevant_increate_t0_download_v2_base&utm_relevant_index=5
https://blog.csdn.net/qq_21570029/article/details/80772561?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-80772561-blog-123926503.235%5Ev35%5Epc_relevant_increate_t0_download_v2_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-80772561-blog-123926503.235%5Ev35%5Epc_relevant_increate_t0_download_v2_base&utm_relevant_index=10
"""


def job2(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


def job3(name):
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


# 实例化调度器
scheduler = BackgroundScheduler(timezone='Asia/Shanghai')  # 这个地方要加上时间，不然他有时间的警告

# 调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")


# 添加任务1
# 每隔5s执行这个任务，这个就是装饰器的玩法
@register_job(scheduler, "interval", seconds=5, args=['老K'], id='job1', replace_existing=True)
def job1(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


# 下面这就是add_job的方式 interval
scheduler.add_job(job2, "interval", seconds=10, args=['老Y'], id="job2", replace_existing=True)

# 下面这就是add_job的方式 crontab  16点 38分  40分执行
scheduler.add_job(job3, 'cron', hour='16', minute='38,40', args=['鬼人'], id='job3', replace_existing=True)

"""
20220408更新 
id可以不加,如果不加ID是这个应用view下的函数名字

replace_existing=True 这个东西不加的话，他会提示ID冲突了,我查了好多文章，把这答案找出来了 。
"""
# 调度器开始运行
print("start")
scheduler.start()


def index(request):
    return HttpResponse('ok')
