<template>
  <div class="home">
    <Chart />
    <div class="container">
      <h1>Exerted Power: 3kW</h1>
      <h1>Generator Usage: 200%</h1>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Chart from "@/components/chart.vue";

export default {
  name: "Home",
  components: {
    Chart,
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1rem;
}
h1 {
  text-align: center;
  margin: auto;
}
</style>
