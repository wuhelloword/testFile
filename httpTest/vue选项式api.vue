<template>
  <div>
    <button @click="Increment">Count is:{{ count }}</button>
  </div>
</template>

<script>
export default {
  //data()返回的属性将会成为响应式的状态
  //并且暴露在‘this‘上
  data(){
    return {
      count:0
    }
  },

  //methods是一些用来更改状态与触发更新的函数
  //它们可以在模板中作为事件监听器绑定
  methods:{
    increment(){
      //this指向当前组件实例，数据属性可以被修改
      this.count++
    }
  },

  //生命周期钩子会在组件生命的各个不同阶段被调用
  //例如这个函数就会在组件挂载完成后被调用
  mounted(){
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<style scoped>

</style>