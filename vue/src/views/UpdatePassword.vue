<template>
    <body class="text-center">

    <main class="form-signin">
        <form @submit.prevent="submitForm">
            <img class="mb-4" src="../assets/img/logo.png" alt="" width="72" height="72">
            <h1 class="h3 mb-3 fw-normal">修改密码</h1>

            <div class="form-floating mb-3">
                <input type="text" disabled class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">用户名</label>
            </div>
            <div class="form-floating">
                <input type="password" name="password_1" required class="form-control" id="floatingPassword"
                       placeholder="Password">
                <label for="floatingPassword">原密码</label>
            </div>
            <div class="form-floating">
                <input type="password" name="password_2" required class="form-control" id="floatingPassword"
                       placeholder="Password">
                <label for="floatingPassword">新密码</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="submit">修改</button>
            <p class="mt-5 mb-3 text-muted">© 1962-2022</p>
        </form>
    </main>
    </body>
</template>

<script>
import axios from "axios";
import qs from "qs";
import {message} from "ant-design-vue";

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8080/',
});
apiClient.interceptors.request.use(config => {
    config.headers['token'] = localStorage.getItem('token');
    config.headers['username'] = localStorage.getItem('username');
    return config;
});
export default {

    name: "UpdatePassword",
    data() {
        return {
            name: localStorage.getItem('username'),
            id: localStorage.getItem('userID'),
            password_old: '',
            password_new: '',
        }
    },
    methods: {

        async submitForm() {
            const data = {
                student_name: this.name,
                student_id: this.id,
                password_old: this.password_old,
                password_new: this.password_new,
            };

            const params = qs.stringify(data);
            try {
                const response = await apiClient.post('/log/pwd_update/', params);
                console.log(response.data); // 打印响应数据
                message.success('修改成功');
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        },
    }
}
</script>

<style scoped>
.bd-placeholder-img {
    font-size: 1.125rem;
    text-anchor: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
}

@media (min-width: 768px) {
    .bd-placeholder-img-lg {
        font-size: 3.5rem;
    }
}

.b-example-divider {
    height: 3rem;
    background-color: rgba(0, 0, 0, .1);
    border: solid rgba(0, 0, 0, .15);
    border-width: 1px 0;
    box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

.b-example-vr {
    flex-shrink: 0;
    width: 1.5rem;
    height: 100vh;
}

.bi {
    vertical-align: -.125em;
    fill: currentColor;
}

html,
body {
    height: 100%;
}

body {
    display: flex;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
}

.form-signin {
    width: 100%;
    max-width: 400px;
    padding: 15px;
    margin: auto;
}

.form-signin .checkbox {
    font-weight: 400;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>