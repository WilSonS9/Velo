<template>
  <div class="home">
    <Chart />
    <div class="container">
      <h1>Current Voltage: {{ latest }}V</h1>
      <h1>Generator Usage: {{ ((latest / 24) * 100).toFixed(2) }}%</h1>
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

  async mounted() {
    window.setInterval(() => {
      this.fetchData();
    }, 5000);
  },
  methods: {
    async fetchData() {
      const res = await axios.get(
        "https://8fbddwr1ga.execute-api.us-east-1.amazonaws.com/fetchPower?BicycleID=2"
      );

      this.latest = res.data[0][res.data[0].length - 1][1];

      // console.log(res.data[0][res.data[0].length - 1]);
      // console.log(res.data[0]);
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
