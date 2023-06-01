<template>
    <a-table :dataSource="room_list" :columns="columns">
        <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'set'">
                <a-button type="primary" ghost @click="showModal(record.id, record.open_time, record.close_time)">设置</a-button>
            </template>
            <template v-if="column.key === 'toDetail'">
                <a-button type="primary" ghost @click="toSeat(record.id)">查看</a-button>
            </template>
        </template>
    </a-table>

    <a-modal v-model:visible="visible" title="Basic Modal" @ok="handleOK">
        请选择是否开启自习室：
        <a-switch v-model:checked="checked"/>
        <p v-if="checked" style="display: inline;">可用</p>
        <p v-if="!checked" style="display: inline;">不可用</p>
        <br/>
        请选择自习室开放时间：
        <a-time-range-picker v-model:value="time" value-format="HH:mm:ss"/>
    </a-modal>
</template>
<script>
import apiClient from "../../axios";
import moment from "moment/moment";
import router from "@/router";
import axios from "axios";

export default {
    data() {
        return {
            id: 1,
            visible: false,
            checked: true,
            time: [],

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
            ],

            columns: [
                {
                    title: 'id',
                    dataIndex: 'id',
                    key: 'id',
                },
                {
                    title: '自习室名称',
                    dataIndex: 'name',
                    key: 'name',
                },
                {
                    title: '容量',
                    dataIndex: 'capacity',
                    key: 'capacity',
                },
                {
                    title: '开启时间',
                    dataIndex: 'open_time',
                    key: 'open_time',
                },
                {
                    title: '关闭时间',
                    dataIndex: 'close_time',
                    key: 'close_time',
                },
                {
                    title: '设置',
                    dataIndex: 'set',
                    key: 'set',
                },
                {
                    title: '查看详细',
                    dataIndex: 'toDetail',
                    key: 'toDetail',
                },
            ],
        };
    },
    methods: {
        showModal(id, start_time, end_time) {
            this.time[0] = start_time;
            this.time[1] = end_time;
            this.visible = true;
            this.id = id;
        },
        onRangeOk(value) {
            this.time = value;
        },
        async handleOK() {
            // console.log(this.time[0])
            // const startDateString = moment(this.time[0]).format('HH:mm:ss');
            // const endDateString = moment(this.time[1]).format('HH:mm:ss');
            console.log("vue:", parseInt(this.id))
            const data = {
                roomIDs: parseInt(this.id),
                state: this.checked? 'on': 'off',
                open_time: this.time[0],
                close_time: this.time[1],
            };
            //console.log(data)
            try {
                //const response = await apiClient.post('/admin/setroom/', data);
                //console.log(response.data); // 打印响应数据
                console.log("data:",data)
                axios.post('http://localhost:8080/admin/setroom/', data)      
                    .then(response => {
                        console.log(response.data); // 打印响应数据
                        this.visible = false
                        this.room_list[this.id-1].start_time = this.time[0]
                        this.room_list[this.id-1].close_time = this.time[1]       //数组下标减一
                        console.log("room_list:",this.room_list,this.room_list[this.id-1])
                        })
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        },
        toSeat(id) {
            router.push(`/admin/seat/${id}`)
        }
    },
};
</script>