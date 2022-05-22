<template>
  <div class="container">
    <div class="stats stats--user">
      <h1 class="text-main">User Stats</h1>
      <h2>You have generated enough energy to:</h2>

      <ul class="list">
        <li>Mine 8.6 Bitcoin</li>
        <li>Power a household for 1.6 hours</li>
      </ul>
    </div>
    <div class="stats stats--velo">
      <h1 class="text-main">VELO Stats</h1>
      <h2>
        The VELO community has generated 100kJ of energy, enough to:
      </h2>
      <ul class="list">
        <li>
          Toast 12.4 slices of bread
        </li>
        <li>Charge a tesla for 1.2 hours</li>
      </ul>
      <!-- <ul class="list">
        <li v-for="(nrg, i) in active" :key="i">
          {{
            reqEn[nrg].message.replace(
              "$(amount)",
              replaceEnergy(reqEn[nrg].energy, allTime)
            )
          }}
        </li>
      </ul> -->
    </div>

    <img class="stats" src="../assets/greenplanet.jpg" alt="" />
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      active: [],
      userActive: [],
      userAllTime: [],
      allTime: 0,
      reqEn: {
        BTC: {
          name: "BTC",
          energy: 6199200000,
          message: "Mine $(amount) BTC",
          mod: 0,
        },
        Toast: {
          name: "Toast",
          energy: 72000,
          message: "Toast $(amount) bread",
          mod: 0,
        },
        Tesla: {
          name: "Tesla",
          energy: 360000000,
          message: "Charge $(amount) teslas",
          mod: 0,
        },
        Household: {
          name: "Household",
          energy: 32400000000,
          message: "Power $(amount) households for 1 hour",
          mod: 0,
        },
      },
    };
  },
  methods: {
    async fetchData() {
      const res = await axios.get(
        "https://8fbddwr1ga.execute-api.us-east-1.amazonaws.com/getIt"
      );
      this.allTime = res.data;
      for (let i in this.reqEn) {
        this.reqEn[i]["mod"] =
          this.reqEn[i]["energy"] - (res.data % this.reqEn[i]["energy"]);
      }
      this.findNearest();
    },
    findNearest() {
      let temp = [];
      for (let i in this.reqEn) {
        temp.push([i, this.reqEn[i]["mod"]]);
      }
      temp.sort(function(a, b) {
        return a[1] - b[1];
      });
      this.active.push(temp[0][0]);
      this.active.push(temp[1][0]);
    },
    replaceEnergy(energy, allTime) {
      return (allTime / energy).toFixed(2);
    },
  },
  async mounted() {
    await this.fetchData();
  },
};
</script>
<style>
li {
  font-size: 1.2rem;
}
.container {
  display: flex;
  flex-direction: column;
  max-width: 100vw;
  align-items: center;
}
.text-main {
  font-size: 2rem;
  margin-bottom: 0.3rem;
}

.stats {
  margin-bottom: 2rem;
  width: 25%;
  text-align: center;
}
.list {
  margin: 1rem;
  text-align: center;
  list-style: none;
}
img {
  max-width: 100%;
  height: auto;
}
@media only screen and (max-width: 800px) {
  .stats {
    width: 100%;
  }
}
</style>
