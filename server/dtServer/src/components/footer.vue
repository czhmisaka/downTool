<template>
     <div class="footer">
      <ul class="fotter-ul">
        <li class="footer-li date"><i class="fa fa-clock-o icon" aria-hidden="true"></i>已运行：200秒</li>
        <li class="footer-li">状态<i class="fa fa- icon" aria-hidden="true"></i></li>
         <li class="footer-li right" style="margin-right:20px;"><i class="fa fa-refresh icon"  aria-hidden="true"></i></li>
      </ul>
    </div>
</template>
<style scoped>
.footer{
  position: absolute;
  bottom: 0px;
  width: 100%;
  height: 50px;
  box-shadow: 0px 0px 20px rgba(0,0,0,0.1);
}
.footer-ul{
  width: 100%;
  overflow: hidden;
  height: 50px;
  line-height: 50px;
}
.footer-li{
  float: left;
  list-style: none;
  margin-left: 10px;
  height: 50px;
  line-height: 50px;
}

.right{
  float: right;
}
.icon{
  margin-right:5px;
}
</style>
<script>
import Vue from 'vue'
export default {
  name: 'footer',
  data () {
    return {
      title:'a footer component',
      serverStatus:1,
      serverRunningDate:'未启动'
    }
  },
  methods:{
      getServerStatus(){
          this.$axios.get('/getServerStatus').then(function(res){
                    console.log(res)
                    for (let i in res.data){
                        if(res.data==1){
                            this.serverStatus=2;
                        }else{
                            this.serverStatus=1;
                        }
                        
                    }   
                },function(){
                    console.log('请求失败处理');
                    this.serverStatus=0;
                });
      },
      getServerDate(){
            
      },
  },
    sockets:{
      connect(data){
          console.log(data);
      },
      getServerDate(data){
          console.log(data);
      },

  }
}
</script>>