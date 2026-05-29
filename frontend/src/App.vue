<script setup>
import { RouterLink, RouterView } from 'vue-router';


</script>

<template>
    <header>
        <h1>Kebab App</h1>
        <RouterLink to="/">Homepage</RouterLink>
    </header>
    <main>
        <RouterView />
    </main>
</template>