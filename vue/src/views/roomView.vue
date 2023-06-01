<template>
  <div>
    <!-- 表单 -->
    <form @submit.prevent="submitForm">

      <div>
        <label>return the session</label>
        <input type="text" v-model="stu">
      </div>
      <button type="submit">Submit</button>
    </form>
    <button @click="room">Request for room list</button>
    <button @click="warn">Request for my warning list</button>
    <button @click="reversation">Request for my reversation list</button>
  </div>
</template>

<script>
import axios from 'axios';




export default {

  data() {
    return {
      name: '',
      password: '',
      stu: ''
    }
  },


  // localStorage.clear(); 注销时清除本地存储

  methods: {
    submitForm() {
      console.log("room here")
      axios.post('http://127.0.0.1:8080/log/index/room/', {}, {        //改了
        headers: {
          'token': localStorage.getItem('token'),
          'username': localStorage.getItem('username'),
        }
      }).then(res => {
        console.log(res.data);

      }).catch(err => {
        console.log(err);
      })
    },

    async room() {
      console.log('in room')
      try {
        const response = await apiClient.post('/index/room/', { /* 请求体数据 */ });
        console.log(response.data); // 打印响应数据
      } catch (error) {
        console.error(error); // 打印请求错误信息
      }
    },

    async warn() {
      try {
        const response = await apiClient.get('/index/warn/', { /* 请求体数据 */ });
        console.log(response.data); // 打印响应数据
      } catch (error) {
        console.error(error); // 打印请求错误信息
      }
    },

    async reversation() {
      try {
        const response = await apiClient.get('/index/view_reservation/', { /* 请求体数据 */ });
        console.log(response.data); // 打印响应数据
      } catch (error) {
        console.error(error); // 打印请求错误信息
      }
    }


  }
}

</script>
