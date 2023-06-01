<template>
    <main class="container">
        <div class="row">
            <div class="col-3 mt-3 bg-light" v-for="reservation in reservation_list">
                <div class="p-4 rounded mt-3 h-100">
                    <h5>座位号：{{ reservation.seat }}</h5>
                    <h5>开始时间：{{ reservation.start_time }}</h5>
                    <h5>结束时间：{{ reservation.end_time }}</h5>
                    <h5>状态：{{ reservation.status }}</h5>

                    <p class="lead text-center">请保持良好的学习环境！</p>
                    <p class="text-center">
                        <a type="button" class="btn btn-outline-success" data-bs-toggle="modal"
                           data-bs-target="#exampleModal-1">取消预约</a>
                    </p>


                    <!-- Button trigger modal -->


                    <!-- Modal -->
                    <div class="modal fade" id="exampleModal-1" tabindex="-1"
                         aria-labelledby="exampleModalLabel"
                         aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">请确认一下信息！</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                                            aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <p class="h5">你确定取消吗？</p>


                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                                        取消
                                    </button>
                                    <a class="btn btn-danger">确定</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--            <main class="container">-->
            <!--                <div class="bg-light p-5 rounded mt-3">-->
            <!--                    <h1>你没有预约记录！！</h1>-->
            <!--                    <p class="lead">请保持良好的学习环境！</p>-->

            <!--                </div>-->
            <!--            </main>-->
        </div>
    </main>
</template>

<script>
import axios from 'axios';
import router from "@/router";

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8080/',
});
apiClient.interceptors.request.use(config => {
    config.headers['token'] = localStorage.getItem('token');
    config.headers['username'] = localStorage.getItem('username');
    return config;
});
export default {
    name: "Recording",
    data() {
        return {
            reservation_list: [
                {
                    "seat": 1,
                    "start_time": "2023-04-15T21:19:56.824734",
                    "end_time": "2023-04-15T22:19:56.824734",
                    "status": "2"
                },
                {
                    "seat": 4,
                    "start_time": "2023-04-14T10:00:00",
                    "end_time": "2023-04-14T11:00:00",
                    "status": "1"
                }
            ]
        }
    },
    async mounted() {
        try {
            const response = await apiClient.get('/index/view_reservation/', {});
            console.log(response.data); // 打印响应数据
            this.reservation_list = response.data.reservation_list
        } catch (error) {
            console.error(error); // 打印请求错误信息
        }
    },
}
</script>

<style scoped>

</style>