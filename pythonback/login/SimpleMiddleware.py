import re

from django.http import JsonResponse
from utils.token import check_token
from pathlib import Path


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #print("initial")

    def __call__(self, request):
        path = request.path       #原版path = request.path
        print("in login middleware")
        #新加
        BASE_DIR = Path(__file__).resolve().parent.parent
        #print("dist放哪儿了：",BASE_DIR)
        #path = 'dist'+path
        #request.path = path
        print("request:", request.method)

        # Process pre-request
        if request.method == "OPTIONS":
            print("here??")
            response = self.get_response(request)
            response['Access-Control-Allow-Origin'] = request.headers.get('Origin')
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Headers'] = 'Content-Type,Content-Length,Authorization,Accept,X-Requested-With,username,token'
            response['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
            print("OPTIONS pass")
            return response
        """
            1.判断是否登录
            2.判断是否访问
        """
        # 允许后台不登录情况下访问的路径
        allow_list = ['/', '/logout/', '/login/', '/login/register/', '/admin/login/']
        if re.match(r'/index/', path) and (path not in allow_list):
            # 从请求头中获取 username 和 token
            username = request.META.get('HTTP_USERNAME')
            token = request.META.get('HTTP_TOKEN')
            print("username:", username)
            print("token:", token)
            '''
            #这部分先不用，这是用来增强安全性的，但是无法正常获取用户名
            if username is None or token is None:
                return JsonResponse({'status': "error", 'msg': "未查询到登录信息"})
            else:
                # 调用 check_token 函数验证
                if check_token(username, token):
                    print("token pass")
                # else:
                #     return JsonResponse({'status': "error", 'msg': "登录信息错误或已过期"})
            '''    
        response = self.get_response(request)

        return response
