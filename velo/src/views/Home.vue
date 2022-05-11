<template>
  <div class="home">
    <Chart />
    <div class="container">
      <h1>Exerted Power: {{ latest }}W</h1>
      <h1>Generator Usage: {{ latest / 500 }}%</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Chart from "@/components/chart.vue";

export default {
  name: "Home",
  components: {
    Chart,
  },
  data() {
    return { latest: "" };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      const res = await axios.get(
        "https://8fbddwr1ga.execute-api.us-east-1.amazonaws.com/fetchPower?BicycleID=2"
      );

      this.latest = res.data[0].slice(-1)[0][1];
    },
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
