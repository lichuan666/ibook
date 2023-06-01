<template>
    <a-table :dataSource="seat_list" :columns="columns">
        <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'set'">
                <a-button type="primary" ghost @click="showModal(record.seat_id)">设置</a-button>
            </template>
        </template>
    </a-table>

    <a-modal v-model:visible="visible" title="Basic Modal" @ok="handleOK">
        请选择是否开启座位：
        <a-switch v-model:checked="checked"/>
        <p v-if="checked" style="display: inline;">可用</p>
        <p v-if="!checked" style="display: inline;">不可用</p>
        <br/>
        该座位是否靠近插座：
        <a-switch v-model:checked="checked2"/>
        <p v-if="checked2" style="display: inline;">靠电</p>
        <p v-if="!checked2" style="display: inline;">普通</p>
        <br/>
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
            checked2:true,      //是否靠电
            time: [],

            seat_list: [
                {
                    "seat_id": 1,
                    "pos": "1",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 2,
                    "pos": "4",
                    "type": "普通",
                    "state": "关闭"
                },
                {
                    "seat_id": 3,
                    "pos": "5",
                    "type": "靠电",
                    "state": "空闲"
                },
                {
                    "seat_id": 4,
                    "pos": "6",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 5,
                    "pos": "7",
                    "type": "靠电",
                    "state": "空闲"
                },
                {
                    "seat_id": 6,
                    "pos": "8",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 7,
                    "pos": "9",
                    "type": "靠电",
                    "state": "空闲"
                },
                {
                    "seat_id": 8,
                    "pos": "10",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 9,
                    "pos": "11",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 10,
                    "pos": "12",
                    "type": "靠电",
                    "state": "空闲"
                },
                {
                    "seat_id": 11,
                    "pos": "13",
                    "type": "普通",
                    "state": "空闲"
                },
                {
                    "seat_id": 12,
                    "pos": "14",
                    "type": "靠电",
                    "state": "空闲"
                },
                {
                    "seat_id": 13,
                    "pos": "15",
                    "type": "普通",
                    "state": "空闲"
                }
            ],

            columns: [
                {
                    title: '座位id',
                    dataIndex: 'seat_id',
                    key: 'seat_id',
                },
                {
                    title: '位置',
                    dataIndex: 'pos',
                    key: 'pos',
                },
                {
                    title: '类型',
                    dataIndex: 'type',
                    key: 'type',
                },
                {
                    title: '状态',
                    dataIndex: 'state',
                    key: 'state',
                },
                {
                    title: '设置',
                    dataIndex: 'set',
                    key: 'set',
                },
            ],
        };
    },
    methods: {
        showModal(id) {
            this.visible = true;
            this.id = id;
        },
        async handleOK() {
            // console.log(this.time[0])
            // const startDateString = moment(this.time[0]).format('HH:mm:ss');
            // const endDateString = moment(this.time[1]).format('HH:mm:ss');
            console.log(this.id)
            const data = {
                seatIDs: parseInt(this.id),
                state: this.checked? 'on': 'off',
                type: this.checked2? '靠电': '普通'
            };
            console.log(data)
            try {
                //const response = await apiClient.post('/admin/setseat/', data);
                axios.post('http://localhost:8080/admin/setseat/', data)      
                    .then(response => {
                        console.log(response.data,this.checked); // 打印响应数据
                        let zhuangtai
                        if(this.checked == true)        //可以再考虑加上被预约的状态
                        {
                            zhuangtai = '空闲'
                        }
                        else
                        {
                            zhuangtai = '关闭'
                        }

                        let power
                        if(this.checked2 == true)       
                        {
                            power = '靠电'
                        }
                        else
                        {
                            power = '普通'
                        }
                        this.seat_list[this.id-1].state = zhuangtai
                        this.seat_list[this.id-1].type = power
                        this.visible = false
                    })
                
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        },
    },
};
</script>