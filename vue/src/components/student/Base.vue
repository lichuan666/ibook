<template>
    <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#" style="width: 100%;">
                <img src="../../assets/img/logo.png" alt="" width="40" height="40">
                <a class="navbar-brand" href="#">复旦大学 <small>图书馆座位预约系统</small></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent" style="float: right; width: 70%">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0" style="float: left">
                        <li class="nav-item">
                            <router-link class="nav-link" to="/student">首页</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/student/room">预定座位</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/student/recording">预约记录</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/student/warn">警告记录</router-link>
                        </li>
                    </ul>
                    <ul class="navbar-nav  d-flex dropdown" style="--bs-scroll-height: 100px;margin-right: 30px;">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarScrollingDropdown" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            <img style="border-radius: 50%" src="../../assets/img/logo.png" alt="" width="40" height="40">
                        </a>

                        <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
                            <li><a class="dropdown-item" href="{% url 'pswd_update' %}">修改密码</a></li>
                            <li><a class="dropdown-item" href="{% url 'logout' %}">退出登录</a></li>
                        </ul>

                        <!--                        <a class=" btn btn-outline-secondary" href="{% url 'login' %}">-->
                        <!--                            登录/注册-->
                        <!--                        </a>-->
                    </ul>

                </div>
            </a>
        </div>
    </nav>
    <router-view></router-view>
    </body>
</template>

<script>
export default {
    name: "base"
}
</script>

<style scoped>

</style>