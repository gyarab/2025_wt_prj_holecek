<template>
  <div class="kebab-list-container">
    <header class="header">
      <div class="header-content">
        <h1>🌮 Kebabárny</h1>
        <p class="subtitle">Najděte vaši oblíbenou kebabárnu</p>
      </div>
    </header>

    <main class="main-content">
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Načítám kebabárny…</p>
      </div>

      <div v-if="error" class="error-box">
        <span class="error-icon">⚠️</span>
        <p>{{ error }}</p>
        <button @click="fetchKebabs" class="retry-btn">Zkusit znovu</button>
      </div>

      <div v-if="!loading && kebabs.length === 0" class="no-data">
        <p>Žádné kebabárny k dispozici</p>
      </div>

      <div v-if="!loading && kebabs.length > 0" class="kebab-grid">
        <div v-for="kebab in kebabs" :key="kebab.id" class="kebab-card">
          <div class="kebab-header">
            <h2>{{ kebab.name }}</h2>
            <span class="meat-badge">{{ kebab.meat_type }}</span>
          </div>

          <div class="kebab-info">
            <div class="info-item">
              <span class="icon">📍</span>
              <div>
                <p class="label">Město</p>
                <p class="value">{{ kebab.city }}</p>
              </div>
            </div>

            <div class="info-item">
              <span class="icon">🏠</span>
              <div>
                <p class="label">Adresa</p>
                <p class="value">{{ kebab.address }}</p>
              </div>
            </div>

            <div class="info-item">
              <span class="icon">🕐</span>
              <div>
                <p class="label">Otevírací doba</p>
                <p class="value">{{ kebab.opening_hours }}</p>
              </div>
            </div>

            <div class="info-item">
              <span class="icon">📧</span>
              <div>
                <p class="label">Email</p>
                <p class="value">
                  <a :href="`mailto:${kebab.email}`">{{ kebab.email }}</a>
                </p>
              </div>
            </div>
          </div>

          <router-link :to="{ name: 'kebab-detail', params: { id: kebab.id } }" class="detail-btn">
            Zobrazit detaily →
          </router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { API_BASE_URL } from '../config'

export default {
  name: 'Kebabarna',
  data() {
    return {
      kebabs: [],
      loading: true,
      error: null
    }
  },
  mounted() {
    this.fetchKebabs()
  },
  methods: {
    async fetchKebabs() {
      this.loading = true
      this.error = null
      try {
        const url = `${API_BASE_URL}/api/kebabshop`
        console.log('Fetching from:', url)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`Chyba ${res.status}: ${res.statusText}`)
        this.kebabs = await res.json()
        console.log('Data loaded:', this.kebabs)
      } catch (err) {
        console.error('Fetch error:', err)
        this.error = `Chyba: ${err.message} - Ujistěte se, že je Django server spuštěn na http://localhost:8000`
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.kebab-list-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
  color: white;
  padding: 60px 20px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header-content h1 {
  font-size: 3em;
  margin-bottom: 10px;
  font-weight: 700;
}

.subtitle {
  font-size: 1.2em;
  opacity: 0.9;
}

.main-content {
  max-width: 1400px;
  margin: -30px auto 40px;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

.loading {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #d32f2f;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading p {
  font-size: 1.1em;
  color: #666;
}

.error-box {
  background: white;
  border-left: 5px solid #d32f2f;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.error-icon {
  font-size: 2em;
  margin-right: 10px;
}

.error-box p {
  color: #d32f2f;
  font-weight: 500;
  margin: 10px 0;
}

.retry-btn {
  margin-top: 15px;
  padding: 10px 20px;
  background: #d32f2f;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.3s;
}

.retry-btn:hover {
  background: #b71c1c;
}

.no-data {
  background: white;
  padding: 60px 20px;
  text-align: center;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  color: #999;
  font-size: 1.2em;
}

.kebab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 25px;
  margin-top: 20px;
}

.kebab-card {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.kebab-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 20px rgba(211, 47, 47, 0.15);
}

.kebab-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 15px;
}

.kebab-header h2 {
  font-size: 1.5em;
  color: #333;
  flex: 1;
}

.meat-badge {
  background: #d32f2f;
  color: white;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.85em;
  font-weight: 600;
  white-space: nowrap;
  margin-left: 10px;
}

.kebab-info {
  flex: 1;
  margin-bottom: 20px;
}

.info-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 15px;
}

.icon {
  font-size: 1.5em;
  margin-right: 12px;
  min-width: 30px;
}

.info-item div {
  flex: 1;
}

.label {
  font-size: 0.85em;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 2px;
}

.value {
  color: #333;
  font-weight: 500;
}

.value a {
  color: #d32f2f;
  text-decoration: none;
  transition: color 0.3s;
}

.value a:hover {
  color: #b71c1c;
  text-decoration: underline;
}

.detail-btn {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
  text-align: center;
  transition: all 0.3s;
  border: 2px solid transparent;
}

.detail-btn:hover {
  border-color: #d32f2f;
  background: white;
  color: #d32f2f;
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .header-content h1 {
    font-size: 2em;
  }

  .subtitle {
    font-size: 1em;
  }

  .kebab-grid {
    grid-template-columns: 1fr;
  }

  .kebab-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .meat-badge {
    margin-left: 0;
    margin-top: 10px;
  }
}
</style>
