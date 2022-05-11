<template>
  <div id="app">
    <div id="nav">
      <Navbar />
    </div>
    <router-view />
  </div>
</template>
<script>
import Navbar from "./components/navbar.vue";
export default {
  components: { Navbar },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #8da4ce;
}
html {
  background-color: #24252a;
}
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background-color: #24252a;
  border-radius: 100px;
}

::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 6px solid rgba(0, 0, 0, 0.18);
  border-left: 0;
  border-right: 0;
  background-color: #67d163;
}
</style>
