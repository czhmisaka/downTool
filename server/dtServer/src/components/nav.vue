<template>
    <div class="header">
      <span class="header-title">DownTool Server</span>
    <ul class="header-ul">
      <li class="header-li" @click="focus"><i class="fa fa-check-circle" aria-hidden="true" style="margin-right:10px"></i><router-link class="link" :to="'/'">projects</router-link> </li>
      <li class="header-li" @click="focus"><i class="fa fa-plus" aria-hidden="true" style="margin-right:10px"></i><router-link class="link" :to="'/aaa'">create</router-link> </li>
      <li class="header-li" @click="focus"><i class="fa fa-paper-plane" aria-hidden="true" style="margin-right:10px"></i><router-link class="link" :to="'/bbb'">projects</router-link> </li>
    </ul>
    </div>
</template>
<style scoped>
.header{
  width: 100%;
  height: 120px;
  background-color:rgba(223,244,236);
  padding: 10px;

}
.header-title{
  font-size: 30px;
  font-weight: 600;
}
.header-ul{
  max-width: 500px;
  height: 50px;
  margin: 0 auto;
  padding: 10px;
  margin-top: 20px;
}
.header-li{
  float: left;
  width: 30%;
  height: 50px;
  font-size: 20px;
  list-style: none;
  line-height: 50px;
  transition: box-shadow 0.5s ease;
  cursor: pointer;
  border-radius: 15px;
  margin-left: 5px;
  margin-right: 5px;
}
.header-li:hover{
  box-shadow: 0px 2px 3px 2px rgb(113, 88, 136);
}
.check{
  box-shadow: 0px 2px 3px 2px rgb(113, 88, 136);
  
}
.link{
   text-decoration: none;
}
</style>
<script>
import Vue from 'vue'
export default {
  name: 'nav',
  data () {
    return {
      title:'a nav component',
      id:0,
    }
  },
  methods:{
      focus(){
        let path = this.$route.path;
        let _class = this.$el.getElementsByClassName("header-li");
        _class[this.id].classList.remove("check");
        if(path==='/')
            this.id=0;
        else if(path=="/aaa")
            this.id = 1;
        else if(path=="/bbb")
            this.id = 2;
        _class[this.id].classList.add("check");
  }
  },
  mounted(){
      this.focus();
  }
}
</script>>