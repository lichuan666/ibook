<template>
    <main class="mb-5">
        <div class="container px-2 py-3" id="custom-cards">
            <h3 class="pb-2 m-1">请选择条件</h3>
            <form action="" class="row pb-2 g-3 border-bottom">

                <div class="col-md-6">
                    <label for="inputState" class="form-label">类型</label>
                    <a-select class="form-select"
                              ref="select"
                              v-model:value="value2"
                              @change="handleChange2"
                    >
                        <a-select-option value='正常'>正常</a-select-option>
                        <a-select-option value='靠电'>靠电</a-select-option>
                    </a-select>
                </div>

                <div class="col-md-6">
                    <label for="inputCity" class="form-label">座位</label><br/>
                    <a-select class="form-select"
                              ref="select"
                              v-model:value="value1"
                              @change="handleChange1"
                              :options="pos"
                    >
                        <!--                        <a-select-option value="jack">Jack</a-select-option>-->
                    </a-select>
                </div>


            </form>
        </div>
    </main>

  <!--    <a-space>-->
  <!--        <a-select-->
  <!--            ref="select"-->
  <!--            v-model:value="value1"-->
  <!--            style="width: 30%"-->
  <!--            @focus="focus"-->
  <!--            @change="handleChange"-->
  <!--        >-->
  <!--            <a-select-option value="jack">Jack</a-select-option>-->
  <!--            <a-select-option value="lucy">Lucy</a-select-option>-->
  <!--            <a-select-option value="disabled" disabled>Disabled</a-select-option>-->
  <!--            <a-select-option value="Yiminghe">yiminghe</a-select-option>-->
  <!--        </a-select>-->
  <!--        <a-select v-model:value="value2" style="width: 120px" disabled>-->
  <!--            <a-select-option value="lucy">Lucy</a-select-option>-->
  <!--        </a-select>-->
  <!--        <a-select v-model:value="value3" style="width: 120px" loading>-->
  <!--            <a-select-option value="lucy">Lucy</a-select-option>-->
  <!--        </a-select>-->
  <!--    </a-space>-->

    <div class="m-1 mb-5">
        <div class="accordion-item border-0">
            <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                 data-bs-parent="#accordionExample">
                <div class="accordion-body">

                    <input type="text" name="room" value="">
                    <input type="text" name="day" value="">
                    <input type="text" name="time" value="">


                </div>
            </div>

            <h5 class="m-2 mt-5 text-center">请选择座位：

                <div class="col-12">

                    <div class="row">
                        <div class="col-1" v-for="seat in seat_list">
                            <button class="btn btn-outline-success m-1 w-100 h-85" @click="showModal(seat.seat_id)">
                                {{ seat.pos }}
                                <br/>
                                {{ seat.state }} <br/> {{ seat.type }}
                            </button>
                        </div>
                    </div>
                </div>

            </h5>
        </div>

    </div>

    <a-modal v-model:visible="visible" title="选择时间" @ok="handleOK">
        <a-range-picker
                :show-time="{ format: 'HH:mm' }"
                format="YYYY-MM-DD HH:mm"
                :placeholder="['开始时间', '结束时间']"
                @ok="onRangeOk"
        />
    </a-modal>

</template>

<script>
import apiClient from '../../axios';
import moment from 'moment';
import axios from "axios";

export default {
    name: "Seat",
    data() {
        return {
            date: '',
            seat_id: 1,
            visible: false,
            pos: [],
            value1: '',
            value2: '',
            options1: [{
                value: 'jack',
                label: 'Jack',
            }, {
                value: 'lucy',
                label: 'Lucy',
            }, {
                value: 'disabled',
                label: 'Disabled',
                disabled: true,
            }, {
                value: 'yiminghe',
                label: 'Yiminghe',
            }],
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
            ]
        }
    },
    async mounted() {
        try {
            console.log("114514")
            console.log(this.$route.params)
            console.log(this.$route.params.id)
            const response = await apiClient.get('/index/seat/', {params: {room_id: parseInt(this.$route.params.id)}});
            console.log(response.data); // 打印响应数据
            this.seat_list = response.data.seat_list
            for (var i = 0; i < this.seat_list.length; i++) {
                this.pos.push({"value": this.seat_list[i].pos, "label": this.seat_list[i].pos})

            }
            console.log(this.pos)
        } catch (error) {
            console.error(error); // 打印请求错误信息
        }
    },
    methods: {
        showModal(seat_id) {
            this.seat_id = seat_id
            this.visible = true;
        },
        async handleOK() {
            const startDateString = moment(this.date[0]).format('YYYY-MM-DD HH:mm:ss');
            const endDateString = moment(this.date[1]).format('YYYY-MM-DD HH:mm:ss');
            const data = {
                room_id: parseInt(this.$route.params.id),
                seat_id: parseInt(this.seat_id),
                start_time: startDateString,
                end_time: endDateString,
                sid:1            //学生的uid（理论上应该用个全局变量，先凑合一下吧，出错就改成测试账号的id）
            };
            console.log(data)
            try {
                //const response = await apiClient.post('/index/reservation/', data);
                //console.log(response.data); // 打印响应数据
                console.log("data:",data)
                //console.log(this.GLOBAL.uid)
                axios.post('http://localhost:8080/index/reservation/', data)      
                    .then(response => {
                        console.log(response.data); // 打印响应数据
                        let zhuangtai = '占用'

                        this.seat_list[this.seat_id-1].state = zhuangtai
                        this.visible = false      //关闭窗口
                        })   
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        },
        onRangeOk(value) {
            this.date = value;
        },
        async handleChange2() {
            try {
                const response = await apiClient.get('/index/seat/', {
                    params: {
                        params: {
                            room_id: parseInt(this.$route.params.id),
                            type: this.value2
                        }
                    }
                });
                console.log(response.data); // 打印响应数据
                this.seat_list = response.data.seat_list
                console.log(this.seat_list)
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        },
        async handleChange1() {
            try {
                const response = await apiClient.get('/index/seat/', {
                    params: {
                        params: {
                            room_id: parseInt(this.$route.params.id),
                            pos: this.value1,
                            type: this.value2,
                        }
                    }
                });
                console.log(response.data); // 打印响应数据
                this.seat_list = response.data.seat_list
                console.log(this.seat_list)
            } catch (error) {
                console.error(error); // 打印请求错误信息
            }
        }
    },
}
</script>

<style scoped>

</style>