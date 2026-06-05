<template>
  <div class="kebab-detail-container">
    <header class="header">
      <div class="header-nav">
        <router-link to="/" class="back-link">← Zpět na seznam</router-link>
      </div>
    </header>

    <main class="main-content">
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Načítám detaily…</p>
      </div>

      <div v-if="error" class="error-box">
        <span class="error-icon">⚠️</span>
        <p>{{ error }}</p>
        <router-link to="/" class="back-link">Zpět na seznam</router-link>
      </div>

      <div v-if="!loading && kebab" class="detail-card">
        <div class="detail-header">
          <div>
            <h1>{{ kebab.name }}</h1>
            <span class="meat-badge">{{ kebab.meat_type }}</span>
          </div>
          <span class="id-badge">ID: {{ kebab.id }}</span>
        </div>

        <div class="detail-grid">
          <div class="detail-section">
            <h2>📍 Lokace</h2>
            <div class="section-content">
              <div class="detail-row">
                <span class="key">Město:</span>
                <span class="value">{{ kebab.city }}</span>
              </div>
              <div class="detail-row">
                <span class="key">Ulice:</span>
                <span class="value">{{ kebab.address }}</span>
              </div>
            </div>
          </div>

          <div class="detail-section">
            <h2>🕐 Provozní informace</h2>
            <div class="section-content">
              <div class="detail-row">
                <span class="key">Otevírací doba:</span>
                <span class="value">{{ kebab.opening_hours }}</span>
              </div>
              <div class="detail-row">
                <span class="key">Email:</span>
                <span class="value">
                  <a :href="`mailto:${kebab.email}`">{{ kebab.email }}</a>
                </span>
              </div>
            </div>
          </div>

          <div class="detail-section full-width">
            <h2>🍖 Specialita</h2>
            <div class="specialty-box">
              <p>Tato kebabárna se specializuje na maso typu:</p>
              <div class="specialty-highlight">{{ kebab.meat_type }}</div>
            </div>
          </div>
        </div>

        <div class="action-buttons">
          <router-link to="/" class="btn btn-secondary">← Zpět na seznam</router-link>
          <a :href="`mailto:${kebab.email}?subject=Dotaz k ${kebab.name}`" class="btn btn-primary">
            📧 Napsat email
          </a>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { API_BASE_URL } from '../config'

export default {
  name: 'KebabDetail',
  data() {
    return {
      kebab: null,
      loading: true,
      error: null
    }
  },
  mounted() {
    this.fetchDetail()
  },
  methods: {
    async fetchDetail() {
      this.loading = true
      this.error = null
      const id = this.$route.params.id
      try {
        const url = `${API_BASE_URL}/api/kebabshop/${encodeURIComponent(id)}`
        console.log('Fetching from:', url)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`Chyba ${res.status}: Kebabárna nebyla nalezena`)
        this.kebab = await res.json()
      } catch (err) {
        this.error = err.message
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

.kebab-detail-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
  color: white;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header-nav {
  max-width: 1000px;
  margin: 0 auto;
}

.back-link {
  display: inline-block;
  color: white;
  text-decoration: none;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 6px;
  transition: all 0.3s;
  border: 2px solid white;
}

.back-link:hover {
  background: white;
  color: #d32f2f;
}

.main-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
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
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.error-icon {
  font-size: 3em;
  display: block;
  margin-bottom: 10px;
}

.error-box p {
  color: #d32f2f;
  font-weight: 500;
  margin: 10px 0 20px 0;
  font-size: 1.1em;
}

.detail-card {
  background: white;
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 40px;
  padding-bottom: 30px;
  border-bottom: 3px solid #f0f0f0;
}

.detail-header h1 {
  font-size: 2.5em;
  color: #333;
  margin-bottom: 12px;
}

.detail-header > div {
  flex: 1;
}

.meat-badge {
  display: inline-block;
  background: #d32f2f;
  color: white;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
}

.id-badge {
  background: #f0f0f0;
  color: #666;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.95em;
  font-weight: 500;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.detail-section {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #d32f2f;
}

.detail-section.full-width {
  grid-column: 1 / -1;
}

.detail-section h2 {
  font-size: 1.2em;
  color: #333;
  margin-bottom: 15px;
}

.section-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.detail-row {
  display: flex;
  gap: 15px;
  padding: 8px 0;
}

.key {
  font-weight: 600;
  color: #666;
  min-width: 120px;
}

.value {
  color: #333;
  flex: 1;
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

.specialty-box {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.specialty-box p {
  color: #666;
  margin-bottom: 15px;
}

.specialty-highlight {
  font-size: 1.8em;
  font-weight: 700;
  color: #d32f2f;
  padding: 20px;
  background: #fff3e0;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.action-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-top: 40px;
}

.btn {
  display: inline-block;
  padding: 14px 28px;
  border-radius: 6px;
  font-weight: 600;
  text-decoration: none;
  text-align: center;
  transition: all 0.3s;
  font-size: 1em;
}

.btn-primary {
  background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
  color: white;
  border: 2px solid transparent;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(211, 47, 47, 0.3);
}

.btn-secondary {
  background: white;
  color: #d32f2f;
  border: 2px solid #d32f2f;
}

.btn-secondary:hover {
  background: #d32f2f;
  color: white;
}

@media (max-width: 768px) {
  .detail-header {
    flex-direction: column;
  }

  .detail-header h1 {
    font-size: 1.8em;
  }

  .id-badge {
    margin-top: 10px;
  }

  .action-buttons {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }

  .detail-card {
    padding: 20px;
  }
}
</style>
