<template>
       <div class="content">
      <ul class="content-ul">
        <div v-show="!tasks.length" class="no-task">没有任务哦</div>
       <task v-for="task in tasks" 
          :per="task.per"
          :size="task.size"
          :filename="task.filename"
          :filepath="task.filepath"
          :begintime="task.begintime"
          :processtime="task.processtime"
          :id="task.id"
        :key="task.id" @delete="ondelete"></task>
      </ul>
      <div class="panel">
          <div class="tab">
              <div class="close" @click="close"><i class="fa fa-2x fa-window-close"></i></div>
          </div>
          <div class="panel-content">
              
              <input type="text" v-model="taskUrl" class="panel-input"  placeholder="请输入URL地址" value="https://www.baidu.com">
              <input type="text" v-model="taskName" class="panel-input" placeholder="请输入文件名" value="百度首页">
              <input type="text" v-model="taskFilePath" class="panel-input" placeholder="请输入存放地址" value="test_file">
          </div>
          <button class="panel-button" @click="downloadTask">下载</button>
      </div>

      <button @click="createTask" class="content-button">create</button>
    </div>
</template>
<style  scoped>
.panel{
    position: absolute;
    width:80vw;
    max-width: 500px;
    height:20vw;
    min-height: 300px;
    background-color: aliceblue;
    left: 50%;
    top:50%;
    transform: translate(-50%,-50%);
    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
    border-radius: 5px;
    display: none;
}
.tab{
    position: relative;
    width: 100%;
    height: 35px;
    border-bottom: 1px solid rgba(0,0,0,0.5);
}
.close{
    cursor: pointer;
    float:right;
    margin-right: 5px; 
    margin-top: 2px;
}
.panel-label{
    width: 300px;
    height: 30px;
    color: dimgrey;
}
.panel-input{
    display: block;
    width: 200px;
    height: 30px;
    line-height: 30px;
    outline: none;
    margin:10px auto;
    text-indent: 16px;
    border-radius: 5px;
    background-color: #fff;
    border:2px solid transparent;
}
.panel-input:focus{
    border:2px solid rgba(223,244,236);
}
.panel-button{
    width: 200px;
    height: 30px;
    box-shadow: 0px 2px 5px rgb(216, 82, 82);
    margin:20px auto;
    background-color: rgb(216, 82, 82);
    border: none;
    outline: none;
    border-radius: 2px;
    color: #fff;
}
.panel-button:focus{
    color: gray;

}
.close:hover{
    transform: scale(1.1,1.1);
}
.no-task{
    width: 100%;
    height: 80%;
    position: absolute;
    font-size: 40px;
    opacity: 0.8;
    text-align: center;
    left: 50%;
    top:40%;
    margin-left:-50%;
}
.content{
  width: 100%;
  overflow: hidden;
  position: relative;
  height: calc(100vh - 200px);
  
  box-shadow: 0px 0px 10px rgba(255,255,255,0.5);
}
.content-ul{
  width: 100%;
  margin-top:10px;
  height: 85%;
  overflow: scroll;
}
.content-li{
  width: 100%;
  height: 36px;
  list-style: none;
  margin-bottom: 4px;

}
.content-li-block{
  height: 100%;
  background-color: rgba(223,244,236);
  float: left;
  padding: 10px;
  margin-right: 2px;
  margin-left: 2px;
  box-shadow: 0px 0px 10px rgba(223,244,236);
  cursor: pointer;
  max-height: 1em;
  line-height: 1em;
  font-weight: 600;
}
.content-button{
  width: 200px;
  height: 60px;
  position: absolute;
  bottom: 10px;
  background-color: rgba(58,165,109);
  outline: none;
  color: #fff;
  font-size: 1.5em;
  left:50%;
  margin-left: -100px;
  border-radius: 30px;
  box-shadow: 0px 2px 5px rgba(58,165,109);
  border:none;
  cursor: pointer;
}
.content-button:hover{
  box-shadow: 0px 2px 10px 2px rgba(58,165,109);
  font-size: 1.7em;
}
.longger{
  width: calc(100% - 240px);
}
.right{
  float: right;
}
.icon{
  margin-right:5px;
}
</style>
<script>
import task from '@/components/task'
let status = {
          per:100,
          size:"100mb",
          filename:"高等数学资料",
          filepath:"/chengbo/img/",
          begintime:"2020/02/04",
          processtime:368,
          id:0,
      }
let CREATE_TASK = {
    url:"https://www.baidu.com",
    name:"百度",
    path:"test_file",
}
export default {
  name: 'index',
  components:{task},
  data () {
    return {
      title:'downtool server',
      taskNum:0,
      tasks:[],
      taskUrl:"https://www.taobao.com",
      taskName:"淘宝网",
      taskFilePath:"test_file",
    }
  },
  methods:{
      createTask(){
          let curStatus = Object.assign({},status);
          let panel = document.getElementsByClassName("panel")[0];
          panel.style.display="block";
      },
      downloadTask(){
          let that = this;
          let panel = document.getElementsByClassName("panel")[0];
          panel.style.display = "none";
          let task = Object.assign({},CREATE_TASK);
          task.url = this.taskUrl;
          task.name = this.taskName;
          task.path = this.taskFilePath;
          this.$axios.post('http://127.0.0.1:8900/createTask',{
              task:task,
          }).then(function(res){
                    console.log(res)
                    if(res.data==1001){
                        that.$swal({
                        type:'success',
                        text:"请求成功"
                    });
                    }else{
                        that.$swal({
                        type:'warring',
                        text:"服务器出了一点差错"
                    });
                    }
                    
                },function(){
                    that.$swal({
                        type:'error',
                        text:"请求失败"
                    });
                    console.log('请求失败处理');
                });
      },
      update(){

      },
      ondelete(id){
          let task = null;
          for(let i=0;i<this.tasks.length;i++){
              if(this.tasks.id==id)
                tasks = this.tasks[i];
                break;
          }
          this.tasks.splice(this.tasks.indexOf(task),1);
      },
      getTask(){
          var that = this;
          setInterval(()=>{
              this.$axios.get('/getTask').then(function(res){
                    console.log(res)
                    for (let i in res.data){
                        console.log(i)
                        that.tasks = res.data
                    }   
                },function(){
                    console.log('请求失败处理');
                });
          },200000);
           
      },
      close(){
          let panel = document.getElementsByClassName("panel")[0];
          panel.style.display="none";
          console.log(this.$el)
      },
      
  },
  mounted(){
      this.getTask();
      this.$socket.emit('update', {data:this.taskFilePath});
  },
  sockets:{
      connect(data){
          console.log(data);
      },
      response(data){
          console.log(data);
          if(data != "[]"){
              let _tasks = JSON.parse(data.data)
              this.tasks = _tasks
          }
          
          this.$socket.emit('update', {data:this.taskFilePath});
          
      },

  }
}
</script>