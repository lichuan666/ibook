<template>
    <div class="b-example-divider"></div>

    <div class="container px-4 py-5" id="custom-cards">
        <h2 class="pb-2 border-bottom">选择自习室</h2>
        <div class="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
            <div v-for="room in room_list" class="col text-decoration-none">
                <a @click="redir(room.id)">
                    <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg">
                        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
                            <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold text-white">{{ room.name }}</h2>
                            <ul class="d-flex list-unstyled mt-auto">
                                <li class="me-auto">
                                    <img src="../../assets/img/logo.png" alt="大学" width="32" height="32"
                                         class="rounded-circle border border-white">
                                </li>
                                <li class="d-flex align-items-center me-3">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
                                         fill="currentColor" class="bi me-2" viewBox="0 0 16 16">
                                        <path fill-rule="evenodd"
                                              d="M4 4a4 4 0 1 1 4.5 3.969V13.5a.5.5 0 0 1-1 0V7.97A4 4 0 0 1 4 3.999zm2.493 8.574a.5.5 0 0 1-.411.575c-.712.118-1.28.295-1.655.493a1.319 1.319 0 0 0-.37.265.301.301 0 0 0-.057.09V14l.002.008a.147.147 0 0 0 .016.033.617.617 0 0 0 .145.15c.165.13.435.27.813.395.751.25 1.82.414 3.024.414s2.273-.163 3.024-.414c.378-.126.648-.265.813-.395a.619.619 0 0 0 .146-.15.148.148 0 0 0 .015-.033L12 14v-.004a.301.301 0 0 0-.057-.09 1.318 1.318 0 0 0-.37-.264c-.376-.198-.943-.375-1.655-.493a.5.5 0 1 1 .164-.986c.77.127 1.452.328 1.957.594C12.5 13 13 13.4 13 14c0 .426-.26.752-.544.977-.29.228-.68.413-1.116.558-.878.293-2.059.465-3.34.465-1.281 0-2.462-.172-3.34-.465-.436-.145-.826-.33-1.116-.558C3.26 14.752 3 14.426 3 14c0-.599.5-1 .961-1.243.505-.266 1.187-.467 1.957-.594a.5.5 0 0 1 .575.411z"/>
                                    </svg>
                                    <small>容量{{ room.capacity }}</small>
                                </li>
                                <li class="d-flex align-items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
                                         fill="currentColor" class="bi me-2" viewBox="0 0 16 16">
                                        <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z"/>
                                        <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                                    </svg>
                                    <small>时间{{ room.open_time }}到{{ room.close_time }}</small>
                                </li>
                            </ul>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
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
    name: "Room",
    data() {
        return {
            room_list: [
                {
                    "id": 1,
                    "name": "自习室1",
                    "capacity": 50,
                    "open_time": "20:19:56",
                    "close_time": "20:19:56"
                },
                {
                    "id": 2,
                    "name": "自习室2",
                    "capacity": 40,
                    "open_time": "20:19:56",
                    "close_time": "20:19:56"
                },
                {
                    "id": 3,
                    "name": "自习室3",
                    "capacity": 60,
                    "open_time": "20:19:56",
                    "close_time": "20:19:56"
                }
            ]
        }
    },
    async mounted() {

        try {
            const response = await apiClient.post('/index/room/', { /* 请求体数据 */});
            console.log(response.data); // 打印响应数据
            this.room_list = response.data.room_list
        } catch (error) {
            console.error(error); // 打印请求错误信息
        }

    },
    methods: {
        redir(id) {
            router.push(`/student/seat/${id}`)
        }
    }
}
</script>

<style scoped>

</style>