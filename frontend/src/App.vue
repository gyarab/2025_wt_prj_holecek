<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div class="app">
    <header class="app-header">
      <div class="header-content">
        <RouterLink to="/" class="logo">🌮 KebabTracker</RouterLink>
        <nav class="nav-menu">
          <RouterLink to="/" class="nav-link">Domů</RouterLink>
          <a href="http://127.0.0.1:8000/api-playground/" target="_blank" class="nav-link">API Playground</a>
          <a href="http://127.0.0.1:8000/about/" target="_blank" class="nav-link">O Projektu</a>
        </nav>
      </div>
    </header>
    
    <main class="app-main">
      <RouterView />
    </main>
    
    <footer class="app-footer">
      <p>© 2026 KebabTracker - Django + Vue 3 Demo | API: <code>http://127.0.0.1:8000/api/</code></p>
    </footer>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.app-header {
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
  color: white;
  padding: 20px 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.header-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8em;
  font-weight: 700;
  text-decoration: none;
  color: white;
  transition: opacity 0.3s;
}

.logo:hover {
  opacity: 0.9;
}

.nav-menu {
  display: flex;
  gap: 30px;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.3s;
}

.nav-link:hover {
  opacity: 0.8;
}

.app-main {
  flex: 1;
  padding: 40px 20px;
}

.app-footer {
  background: rgba(0, 0, 0, 0.1);
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.app-footer code {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
}
</style>