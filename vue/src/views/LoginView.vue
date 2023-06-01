<template>
  <div>
    <!-- 表单 -->
    <form @submit.prevent="submitForm">
      <div>
        <label>Name:</label>
        <input type="text" v-model="name">
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password">
      </div>
      <div>
        <label>return the session</label>
        <input type="text" v-model="stu">
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';



axios.defaults.withCredentials = true;

  export default {
    data() {
      return {
        name: '',
        password: '',
        stu: ''
      }
    },
    methods: {
      submitForm() {
        // 创建要发送的数据对象
        const data = {
          name: this.name,
          password: this.password,
        };

        const params = qs.stringify(data);

        // 发送POST请求
        axios.post('http://127.0.0.1:8080/log/login/', params)
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
          }
          )
          .catch(error => {
            console.log(error);
          }); 
      }
    }
  }
  
</script>
