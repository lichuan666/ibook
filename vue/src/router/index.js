import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/LoginView.vue";
import roomView from "@/views/roomView.vue";
import login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import UpdatePassword from "@/views/UpdatePassword.vue";
import stuBase from "@/components/student/Base.vue";
import Seat from "@/views/student/Seat.vue";
import Warn from "@/views/student/Warn.vue";
import Recording from "@/views/student/Recording.vue";
import Index from "@/views/student/Index.vue";
import Room from "@/views/student/Room.vue";
import adminBase from "@/components/admin/Base.vue";
import AdminRoom from "@/views/admin/AdminRoom.vue";
import AdminSeat from "@/views/admin/AdminSeat.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'login',
            component: login
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        },
        {
            path: '/updatepassword',
            name: 'updatepassword',
            component: UpdatePassword
        },
        {
            path: '/student',
            component: stuBase,
            children: [
                {
                    path: '',
                    component: Index
                },
                {
                    path: 'room',
                    component: Room,
                },
                {
                    path: 'seat/:id',
                    name: 'seat',
                    component: Seat,
                },
                {
                    path: 'warn',
                    component: Warn,
                },
                {
                    path: 'recording',
                    component: Recording,
                },
            ]
        },
        {
            path: '/admin',
            component: adminBase,
            children: [
                {
                    path: '',
                    component: AdminRoom,
                },
                {
                    path: 'seat/:id',
                    name: 'adminSeat',
                    component: AdminSeat,
                }
            ]
        },
    ]
})

export default router
