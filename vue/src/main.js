import {createApp} from 'vue'
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';
import Antd from 'ant-design-vue';
import router from './router'

const app = createApp(App)

// 导入共用组件
//import global from './global.vue'
//Vue.prototype.global = global

app.use(router)
app.use(Antd)

app.mount('#app')

//新添加
/*

const adamin = require('./components/adamin/Base.vue');
const student = require('./components/student/Base.vue');

const routes = [
    {
        name: 'admin',
        path: '/admin',                   //默认显示页面用/
        component: adamin
    },
    {
        name: 'student',
        path: '/student',
        component: student
    },
];
*/
