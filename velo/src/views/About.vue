<template>
  <div class="container">
    <h1 style=" margin-bottom: 0.5rem">About</h1>
    <h2 class="text">
      Velo is about making money, gib money
    </h2>

    <h1 style="margin-top: 2rem; margin-bottom: 0.5rem">FAQ</h1>
    <ul class="list">
      <li>
        <h2>Q: Do you like the environment?</h2>
        <h2>A: Yes very much so</h2>
      </li>

      <li>
        <h2>Q: Are you quirky?</h2>
        <h2>A: Yes very much so</h2>
      </li>
    </ul>
  </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
  max-width: 100vw;
  align-items: center;
}
.text {
  font-size: 1rem;
}
.list {
  list-style: none; /* Remove default bullets */
  margin-left: 1rem;
}
.list h2 {
  font-size: 1.35rem;
}
.list li::before {
  content: "\2022"; /* Add content: \2022 is the CSS Code/unicode for a bullet */
  color: rgb(103, 209, 99); /* Change the color */
  font-weight: bold; /* If you want it to be bold */
  display: inline-block; /* Needed to add space between the bullet and the text */
  width: 1em; /* Also needed for space (tweak if needed) */
  font-size: 2rem;
  margin-top: -0.3rem;
  margin-left: -1rem; /* Also needed for space (tweak if needed) */
  position: absolute;
}
.list li:nth-child(2) {
  margin-top: 2rem;
}
</style>
