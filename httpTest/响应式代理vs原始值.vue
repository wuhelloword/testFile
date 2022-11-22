<template>

</template>

<script>
export default {
  data(){
    return{
      someObject:{}
    }
  },
  mounted(){
    const newObject = {}
    this.someObject = newObject

    //赋值后再访问this.someObject,此值已经是原来的newObject的一个响应式代理。
    // 与vue2不同的是，这里原始的newObject不会变为响应式，需要确保始终通过this来访问响应式状态

    console.log(newObject === this.someObject)  //false
  }
}
</script>

<style scoped>

</style>