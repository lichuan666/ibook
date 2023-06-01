<template>

    <body class="text-center">
    <main class="form-signin">
        <form @submit.prevent="submitForm">
            <img class="mb-4" src="../assets/img/logo.png" alt="" width="72" height="72">
            <h1 class="h3 mb-3 fw-normal">用户登录</h1>
            <div class="form-floating">
                <input type="text" required name="name" class="form-control" id="floatingInput"
                       placeholder="name@example.com" v-model="name">
                <label for="floatingInput">用户名</label>
            </div>
            <div class="form-floating">
                <input type="password" required name="password" class="form-control" id="floatingPassword"
                       placeholder="Password" v-model="password">
                <label for="floatingPassword">密码</label>
            </div>
            <div class="checkbox mb-3 text-start">
                <label>
                    <input type="checkbox" v-model="isAdmin"> 管理员
                </label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">登录</button>
            <router-link to="/register" class="w-100 btn btn-lg btn-light mt-3">注册</router-link>
            <p class="mt-5 mb-3 text-muted">© 1962-2023</p>
        </form>
    </main>

    </body>

</template>

<script>
//原版
import qs from "qs";
import router from "@/router";
import apiClient from "../axios";
import axios from "axios";
import { message } from 'ant-design-vue';      //这句不确定
/*

import qs from "qs";


*/
export default {
    name: "Login",
    data() {
        return {
            name: '',
            password: '',
            isAdmin: false,
        }
    },
    methods: {
        submitForm() {
            // 创建要发送的数据对象
            const data = {
                name: this.name,
                password: this.password,
                admin:this.isAdmin,       //是否是管理员
            };
            const params = qs.stringify(data);
            console.log("data",params)
            
            // 发送请求(改)

            if (this.isAdmin == false) {
                axios.post('http://localhost:8080/log/login/', params)       //为什么要加log啊我真的不理解
                    .then(response => {
                            console.log(response.data);
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

                            router.push(`/student`)
                        }
                    )
                    .catch(error => {
                        console.log(error);
                    });
                //this.$router.push('/student');
            }
            else
            {
                axios.post('http://localhost:8080/log/login/', params)
                    .then(response => {
                            console.log(response.data);
                            const stu_name = response.data.name;
                            const stu_id = response.data.id;
                            const stu_token = response.data.token;

                            console.log(stu_name);
                            console.log(stu_id);
                            console.log(stu_token);

                            // save the token in the local storage
                            localStorage.setItem("username", stu_name);
                            localStorage.setItem("userID", stu_id);
                            localStorage.setItem("token", stu_token);
                            this.$router.push('/admin');
                        }
                    )
                    .catch(error => {
                        console.log(error);
                    });
                //this.$router.push('/admin');
            }

/*
//原版
            if (this.isAdmin == false) {
                apiClient.post('/log/login/', params)
                    .then(response => {
                            console.log(response.data);
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

                            router.push(`/student`)
                        }
                    )
                    .catch(error => {
                        console.log(error);
                    });
            } 
            else {
                apiClient.post('/log/login/', params)
                    .then(response => {
                            console.log(response.data);
                            const stu_name = response.data.name;
                            const stu_id = response.data.id;
                            const stu_token = response.data.token;

                            console.log(stu_name);
                            console.log(stu_id);
                            console.log(stu_token);

                            // save the token in the local storage
                            localStorage.setItem("username", stu_name);
                            localStorage.setItem("userID", stu_id);
                            localStorage.setItem("token", stu_token);
                        }
                    )
                    .catch(error => {
                        console.log(error);
                    });
                }
                                
*/
        },

        callDjangoFunction(){
            const data = {
                name: this.name,
                password: this.password,
            };
            const params = qs.stringify(data);
                axios.get('http://localhost:8080/login/', params)
                    .then(response => {
                            console.log(response.data);
                   })
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

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>