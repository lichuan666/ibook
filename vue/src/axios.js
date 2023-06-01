import axios from 'axios'
axios.defaults.baseURL = '/api'


let ip = '60.204.152.138';
ip = '127.0.0.1'         //改了试试
let port = '8080';
let baseURL = 'http://' + ip + ':' + port;

console.log('baseURL: ' + baseURL);

const apiClient = axios.create({
  baseURL: baseURL,
});


apiClient.interceptors.request.use(config => {
  config.headers['token'] = localStorage.getItem('token');
  config.headers['username'] = localStorage.getItem('username');
  config.headers['Content-Type'] = 'application/x-www-form-urlencoded';
  return config;
});


export default apiClient
