<template>
  <div class="container">
    <div>
      <v-card class="login-card">
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
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
      username: "",
      password: "",
    };
  },
  methods: {
    onSubmit() {
      console.log("ello");
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
</style>
