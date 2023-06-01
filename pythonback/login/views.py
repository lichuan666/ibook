from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from login.models import *
from utils.token import create_token


# Create your views here.
#登录
def login(request):
    print("in login")
    if request.method == 'POST':
        stu_name = request.POST.get('name')
        stu_password = request.POST.get('password')
        print("execute here")
        admin = request.POST.get('admin')
        print("is admin?",admin)
        if admin == "false":
            print("is student")
            stu = Student.objects.filter(name=stu_name, password=stu_password)
            if stu:
                print("Success")
                student_info = Student.objects.get(name=stu_name, password=stu_password)
                token = create_token(stu_name)
                response = {
                "status": "success",
                "msg": "登陆成功",
                "stu_name": student_info.name,
                "stu_id": student_info.id,
                "token": token
                }
                return JsonResponse(response)
            else:
                msg = "账号或密码错误！！"
                return JsonResponse({"status": "error", "msg": "账号或密码错误！！"}, safe=False,
                                json_dumps_params={'ensure_ascii': False}, status=400)
        else:
            print("is admin")
            adm = Administrator.objects.filter(name=stu_name, password=stu_password)       #如果是管理员
            print(adm)
            if adm:
                print("Success")
                student_info = Administrator.objects.get(name=stu_name, password=stu_password)
                token = create_token(stu_name)
                response = {
                "status": "success",
                "msg": "登陆成功",
                "stu_name": student_info.name,
                "stu_id": student_info.id,
                "token": token
                }
                return JsonResponse(response)
            else:
                msg = "账号或密码错误！！"
                return JsonResponse({"status": "error", "msg": "账号或密码错误！！"}, safe=False,
                                json_dumps_params={'ensure_ascii': False}, status=400)
        '''
        stu = Student.objects.filter(name=stu_name, password=stu_password)
        if stu:
            print("Success")
            student_info = Student.objects.get(name=stu_name, password=stu_password)
            token = create_token(stu_name)
            response = {
                "status": "success",
                "msg": "登陆成功",
                "stu_name": student_info.name,
                "stu_id": student_info.id,
                "token": token
            }
            return JsonResponse(response)
        else:
            msg = "账号或密码错误！！"
            return JsonResponse({"status": "error", "msg": "账号或密码错误！！"}, safe=False,
                                json_dumps_params={'ensure_ascii': False}, status=400)
        '''
    if request.method == 'GET':
        print("now method",request.method)
        return JsonResponse({"status": "error", "msg": "请求方式错误！！"}, safe=False,
                            json_dumps_params={'ensure_ascii': False}, status=400)

#注册
def register(request):
    print("register")
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        # photo = request.FILES.get('photo')

        #可以考虑增加管理员的注册
        stu = Student.objects.filter(is_active=True, name=name)

        if stu:
            msg = '用户已存在！'
            status = 'error'
            return JsonResponse({"status": status, "msg": msg})
        else:
            try:
                stu = Student.objects.create(
                    name=name,
                    password=password,
                    phone=phone,
                    email=email,
                )
                stu.save()
            except Exception as e:
                print(e)
            msg = "注册成功！"
            return JsonResponse({"status": "success", "msg": msg})


def password_update(request):
    if request.method == "POST":
        stu_name = request.POST["student_name"]
        stu_id = request.POST["student_id"]
        password_old = request.POST["password_old"]
        password_new = request.POST["password_new"]

        stu = Student.objects.get(name=stu_name, id=stu_id)
        if stu.password == password_old:
            stu.password = password_new
            stu.save()
            return JsonResponse({"status": "success", "msg": "修改成功！"})
        else:
            msg = "账号或密码错误！"
            return JsonResponse({"status": "error", "msg": msg})


def logout(request):
    if 'name' in request.session:
        del request.session['name']

    return HttpResponseRedirect('/login/')


def index(request):
    try:
        text = Text.objects.filter(is_active=True).order_by('time')
        return render(request, 'index/index.html', {"text": text})
    except Exception as e:
        print(e)
        return render(request, 'index/index.html')
