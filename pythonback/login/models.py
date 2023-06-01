from django.db import models
from django.utils.safestring import mark_safe


# 学生表
class Student(models.Model):
    id = models.AutoField(verbose_name="学生编号，主键", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=22, default='')
    password = models.CharField(verbose_name="密码", max_length=32, default='')
    phone = models.CharField(verbose_name="手机号", max_length=11, default='')
    email = models.CharField(verbose_name="邮箱", max_length=22, default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    photo = models.FileField(verbose_name="头像", default='', upload_to="Student/photo/")
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Student'

        # 后台管理名
        verbose_name_plural = '学生管理'

        managed = True


# 自习室
class Room(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=22, default='')
    capacity = models.IntegerField(verbose_name="座位数量", default=30)
    photo = models.FileField(verbose_name="头像", default='', upload_to="Room/photo/")
    open_time = models.TimeField(verbose_name="开放时间")
    close_time = models.TimeField(verbose_name="关闭时间")
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '自习室图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Room'
        # 后台管理名
        verbose_name_plural = '自习室管理'


# 座位表
class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="自习室编号")
    seat_id = models.IntegerField(verbose_name="座位编号")
    pos = models.CharField(verbose_name="座位位置", max_length=20, default='')
    type = models.CharField(verbose_name="座位类型", max_length=20, default='普通')
    state = models.CharField(verbose_name="座位状态", max_length=20, default='空闲')

    def __str__(self):
        return f"{self.room_id} - {self.seat_id} - {self.pos}"

    class Meta:
        # 数据库列表名
        db_table = 'Seat'
        # 后台管理名
        verbose_name_plural = '座位管理'
        # 设置联合主键
        unique_together = ('room_id', 'seat_id')


# 预约管理
class Reservation(models.Model):
    seat = models.ForeignKey(verbose_name="座位", to='Seat', on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(verbose_name="学生", to='Student', on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    STATUS_CHOICES = [
        ('0', '未进行'),
        ('1', '已结束'),
        ('2', '违约'),
        ('3', '已废弃'),
        ('4', '紧急预约')
    ]
    status = models.CharField(verbose_name="状态", max_length=1, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return self.student.name

    class Meta:
        # 数据库列表名
        db_table = 'Reservation'
        # 后台管理名
        verbose_name_plural = '预约管理'


# 警告管理
class Warn(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    student = models.ForeignKey(verbose_name="学生", to='Student', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="警告题目", max_length=220, default='')
    text = models.TextField(verbose_name="警告内容内容", max_length=220, default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def __str__(self):
        return self.student.name

    class Meta:
        # 数据库列表名
        db_table = 'Warn'
        # 后台管理名
        verbose_name_plural = '扣积分管理'

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.student.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True


# 管理员表
class Administrator(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Administrators ID')
    name = models.CharField(max_length=150, unique=True, verbose_name='Username')
    password = models.CharField(max_length=128, verbose_name='Password')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Last login')
    email = models.EmailField(max_length=254, verbose_name='Email address')
    is_active = models.BooleanField(default=False, verbose_name='Active status')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date joined')

    def __str__(self):
        return "Administrator: %s %s" % (self.id, self.name)

    class Meta:
        db_table = 'administrator'
        managed = True
        verbose_name = '管理员'
