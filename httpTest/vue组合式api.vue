<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>

<script>
import {ref, onMounted} from './vue.global'

//响应式状态
const count = ref(0)

//用来修改状态、触发更新的函数
function increment(){
  count.value++
}

//生命周期钩子
onMounted(()=>{
  console.log(`The iinitial count is ${count.value}.`)
})
</script>

<style scoped>

</style>