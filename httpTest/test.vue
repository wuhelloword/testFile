<template>
<!--  计算属性的测试 -->
<p>Has publish books:</p>
  <span>{{publishedBooksMessage}}</span>

<!--  计算属性缓存vs方法-->
  <p>{{calculateBooksMessage()}}</p>
</template>

<script>


//有状态方法代码，创建一个预置防抖的事件处理器
import { debounce} from 'lodash-es'

export default {
  data(){
    return {
      obj: {
        nested:{count: 0},
        arr: ['foo', 'bar']
      },
      author:{
        name:'John Doe',
        books:[
            'Vue 2 -Advanced Guide',
            'Vue 3 - Basic Guide',
            'Vue 4 - The Mystery'
        ]
      },
      firstName: 'John',
      lastName: 'Doe'
    }
  },

  methods:{
    increment(){
      this.count++;
      nextTick(()=>{
      //  访问更新后的DOM
      })
    },
    mutateDeeply(){
    //  以下都会按照期望工作
      this.obj.nested.count++;
      this.obj.arr.push('baz');
    },
    click:debounce(function (){
    //  对点击的响应
    }, 500),
    calculateBooksMessage(){
      return this.author.books.length > 0 ? 'Yes' : 'No'
    //  如果没有用计算属性，而是定义成一个方法，结果上时完全相同，不同在于，计算属性值会基于其响应式依赖被缓存，也就是计算属性仅会在其响应式依赖更新时才重新计算。
    //  这意味着，只要author.books不改变，无论多少次访问，publishedBooksMessage都会立即返回先前的计算结果，而不重复执行getter函数
    }
  },

  mounted(){
  //  在其他方法或是生命周期中也可以调用方法
    this.increment()
  },

  created(){
  //  每个实例都有了自己的预置防抖的处理函数
    this.debouncedClick = _.debounce(this.click, 500)
  },

  unmounted(){
  //  最好是在组件卸载时
  //  清除掉防抖计时器
    this.debouncedClick.cancel()
  },

  computed: {
  //  在这里定义了一个计算属性publishedBooksMessage       更改此应用中的data中 books数组的值后，publishedBooksMessage也会随之改变
    publishedBooksMessage(){
    //  this 指向当前组件实例
      return this.author.books.length >0 ?'Yes':'No'
    //  在模板中使用计算属性的方式和一般的属性并无二致，vue会检测到this.publishedBooksMessage依赖于this.author.books,所以当this.author.books改变时，任何依赖于this.publishedBooksMessage的绑定都将同时更新
    },
    now(){
      return Date.now()
    //  Data.now()不是一个响应式依赖

    },
    fullName:{
    //  getter
      get(){
        return this.firstName + '' + this.lastName
      },
    //  setter
      set(){
        [this.firstName, this.lastName] = newValue.split(' ')
      }
    }
  }
}

</script>

<style scoped>

</style>