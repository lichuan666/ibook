<template>
    <body class="text-center">

    <main class="form-signin">
        <form @submit.prevent="submitForm">
            <img class="mb-4" src="../assets/img/logo.png" alt="" width="72" height="72">
            <h1 class="h3 mb-3 fw-normal">用户注册</h1>

            <div class="form text-start">
                <label for="floatingInput">用户名</label>
                <input required type="text" name="name" class="form-control" placeholder="用户名" v-model="name">

            </div>
            <div class="form mt-2 text-start">
                <label for="">密码</label>
                <input required type="password" name="password" class="form-control" placeholder="请输入密码"
                       v-model="password">
            </div>

            <div class="form text-start mt-2">
                <label for="floatingFile">手机号</label>
                <input required id="floatingFile" type="text" name="phone" class="form-control"
                       placeholder="请输入手机号" v-model="phone">
            </div>
            <div class="form text-start mt-2">
                <label for="floatingFile">邮箱</label>
                <input required id="floatingFile" type="email" name="email" class="form-control"
                       placeholder="请输入邮箱" v-model="email">
            </div>

            <div class="checkbox mb-3 mt-2 text-start">
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="submit">注册</button>

            <p class="mt-5 mb-3 text-muted">© 1962-2023</p>
        </form>
    </main>
    </body>
</template>

<script>
import qs from "qs";
import axios from "axios";
import { message } from 'ant-design-vue';


export default {
    name: "Register",
    data() {
        return {
            name: '',
            password: '',
            phone: '',
            email: '',
            type:'',       //管理员还是学生
        }
    },
    methods: {
        submitForm() {
            // 创建要发送的数据对象
            const data = {
                name: this.name,
                password: this.password,
                phone: this.phone,
                email: this.email,
                //type:this.type        //待检验
            };

            const params = qs.stringify(data);

            // 发送POST请求
            axios.post('http://127.0.0.1:8080/log/register/', params)
                .then(response => {
                        console.log(response.data);
                        if (response.data.status == "success") {
                            const stu_name = response.data.stu_name;
                            const stu_id = response.data.stu_id;
                            const stu_token = response.data.token;

                            console.log(stu_name);
                            console.log(stu_id);
                            console.log(stu_token);

                            // save the token in the local storage
                            localStorage.setItem("username", stu_name);
                            localStorage.setItem("userID", stu_id);
                            localStorage.setItem("token", stu_token);
                            this.$router.push('/');
                            message.success('注册成功');
                        } else {
                            message.warn('注册失败');
                        }
                    }
                )
                .catch(error => {
                    console.log(error);
                });
        }
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


</style>