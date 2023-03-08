<script setup>
import {  RouterView } from 'vue-router'



const showMobileMenu = false;


</script>

<template>
  <div class="is-wrapped">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>DJACKETS</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu !== showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>

      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-link">Summer</router-link>
          <router-link to="/winter" class="navbar-link">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fa fa-shopping-cart"></i> </span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </nav>
    <section class="section">
      <RouterView />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>

  </div>



</template>

<style >
@import '../node_modules/bulma/css/bulma.min.css';

</style>
