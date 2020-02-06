<template>
     <li class="content-li">
          <div class="content-li-block">
              <i v-if="per===0" class="fa fa-cloud-download" aria-hidden="true"></i>
              <i v-else-if="per===100" class="fa fa-check-circle" aria-hidden="true"></i>
              <i v-else class="fa fa-stop-circle" aria-hidden="true"></i>
              </div>
          <div class="content-li-block longger">
              <span class="solid-bar" :style="{width:'calc('+per+'% - 50px)'}"></span>
              <span class="progress-bar-per " >{{per+"%"}}</span>
          </div>
          <div class="content-li-block file">{{filename}}</div>
          <div class="content-li-block" @click="refresh"><i class="fa fa-refresh" aria-hidden="true"></i></div>
          <div class="content-li-block right" @click="close"><i class="fa fa-window-close" aria-hidden="true"></i></div>
        </li>
</template>
<style scoped>

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
  overflow: hidden;
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
  box-shadow: 0px 0px 5px rgba(58,165,109);
  border:none;
  cursor: pointer;
}
.content-button:hover{
  box-shadow: 0px 0px 10px rgba(58,165,109);
  font-size: 1.7em;
}
.solid-bar{
    display: inline-block;
    width: calc(100% - 50px);
    height: 100%;
    background-color: rgb(95, 155, 95);
    border-radius: 5px;
    float: left;
}
.progress-bar-per{
    width: 50px;
    float: right;
    
}
.right{
  float: right;
}
.file{
    max-width: 150px;
}
.longger{
  width: calc(100% - 280px);
}
</style>
<script>
export default {
  props:{
          id:Number,
          per:Number,
          size:String,
          filename:String,
          filepath:String,
          begintime:String,
          processtime:Number,
  },
  data () {
    return {
      title:'a task bar',
      
    }
  },
  methods:{
      close(){
           this.$swal({
            type:'error',
            text: '你确定要删除'+this.name+'任务吗?',
            confirmButtonText: '是滴！！',
            cancelButtonText: '不要！'
        }).then((res) => {
            if (res.value) {
            this.$emit("delete",this.id);
            }
        })
          
      },
      refresh(){
          this.$swal({
            text: '你确定要刷新'+this.name+'任务吗?',
            confirmButtonText: '是滴！！',
            cancelButtonText: '不要！'
        }).then((res) => {
            if (res.value) {
            this.$emit("refresh",this.name);
            }
        })
      }
  }
}
</script>