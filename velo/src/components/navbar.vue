<template>
  <div>
    <header>
      <a class="logo" href="/"
        ><img class="logo--img" src="../assets/logo.png" alt="logo"
      /></a>
      <nav>
        <ul class="nav__links">
          <li><a href="/stats">Stats</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/login">Login</a></li>
        </ul>
      </nav>
      <!-- <a class="cta" href="#">Contact</a> -->
      <p class="menu cta" @click="isActive = true">Menu</p>
    </header>
    <div id="mobile__menu" class="overlay" :class="{ overlayActive: isActive }">
      <a class="close" @click="isActive = false">&times;</a>
      <div class="overlay__content">
        <a href="/stats">Stats</a>
        <a href="/about">About</a>
        <a href="/login">Login</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    };
  },
  watch: {
    isActive(val) {
      let el = document.getElementsByClassName("apexcharts-toolbar");

      for (let i = 0; i < el.length; i++) {
        el[i].style.display = val ? "none" : "flex";
      }
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

header {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 30px 10%;
  background-color: #24252a;
}

.logo {
  margin-right: auto;
}
.logo--img {
  height: 60px;
  width: auto;
}

.nav__links {
  list-style: none;
  display: flex;
}

.nav__links a,
.cta,
.overlay__content a {
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  color: #edf0f1;
  text-decoration: none;
}

.nav__links li {
  padding: 0px 20px;
}

.nav__links li a {
  transition: all 0.3s ease 0s;
}

.nav__links li a:hover {
  color: #0088a9;
}

.cta {
  margin-left: 20px;
  padding: 9px 25px;
  background-color: rgba(0, 136, 169, 1);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease 0s;
}

.cta:hover {
  background-color: rgba(0, 136, 169, 0.8);
}

/* Mobile Nav */

.menu {
  display: none;
}

.overlay {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  background-color: #24252a;
  overflow-x: hidden;
  transition: all 0.5s ease 0s;
}

.overlayActive {
  width: 100%;
}

.overlay__content {
  display: flex;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.overlay a {
  padding: 15px;
  font-size: 36px;
  display: block;
  transition: all 0.3s ease 0s;
}

.overlay a:hover,
.overlay a:focus {
  color: #0088a9;
}
.overlay .close {
  position: absolute;
  top: 20px;
  right: 45px;
  font-size: 60px;
  color: #edf0f1;
  cursor: pointer;
}

@media screen and (max-height: 450px) {
  .overlay a {
    font-size: 20px;
  }
  .overlay .close {
    font-size: 40px;
    top: 15px;
    right: 35px;
  }
}

@media only screen and (max-width: 800px) {
  .nav__links,
  .cta {
    display: none;
  }
  .menu {
    display: initial;
  }
}
</style>
