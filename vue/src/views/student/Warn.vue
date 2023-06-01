<template>
    <main class="container">
        <div class="bg-danger p-5 rounded mt-3 text-white" v-for="warn in warn_list">
            <p class="lead">{{ warn.title }}</p>
            <p class="lead">{{ warn.text }}</p>
            <p class="lead">{{ warn.time }}</p>
            <p class="lead">{{ warn.is_active }}</p>
        </div>
    </main>
</template>

<script>
import apiClient from "../../axios";

export default {
    name: "warn",
    data() {
        return {
            warn_list: [
                {
                    "title": "Behavior Warning",
                    "text": "Your behavior in class has been unacceptable. Please meet with me to discuss ways to improve.",
                    "time": "2023-04-15T20:19:56.854695",
                    "is_active": true
                },
                {
                    "title": "Behavior Warning",
                    "text": "Your behavior in class has been unacceptable. Please meet with me to discuss ways to improve.",
                    "time": "2023-04-15T20:19:56.854695",
                    "is_active": true
                }
            ]
        }
    },
    async mounted() {
        try {
            const response = await apiClient.get('/index/warn/', {});
            console.log(response.data); // 打印响应数据
            this.warn_list = response.data.warn_list
            console.log(this.warn_list)
        } catch (error) {
            console.error(error); // 打印请求错误信息
        }
    },

}
</script>

<style scoped>

</style>