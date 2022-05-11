<template>
  <div class="container">
    <v-form v-model="valid" @submit.prevent="onSubmit">
      <v-text-field
        v-model="username"
        :counter="10"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
        :counter="10"
        label="Password"
        required
      ></v-text-field>
      <v-card-actions>
        <v-btn type="submit" color="#67d163" :disabled="!valid">
          Save
        </v-btn>
      </v-card-actions>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";
const { createHash } = require("crypto");

export default {
  data() {
    return {
      valid: false,
      username: "",
      password: "",
    };
  },
  methods: {
    async onSubmit() {
      await axios
        .post(
          "https://8fbddwr1ga.execute-api.us-east-1.amazonaws.com/onLogIn?username=" +
            this.hash(this.username) +
            "&pass=" +
            this.hash(this.password)
        )
        .then((data) => console.log(data))
        .catch((error) => console.log(error));
    },
    hash(string) {
      return createHash("sha256")
        .update(string)
        .digest("hex");
    },
  },
};
</script>
<style>
.login-card {
  padding: 2rem;
}
.container {
  display: flex;
  flex-direction: column;
  max-width: 100vw;
  align-items: center;
}
v-text-field {
  background-color: red;
}
</style>
