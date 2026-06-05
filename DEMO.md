# 🌮 KebabTracker - Demo Website

Kompletní Django + Vue 3 aplikace pro správu a recenzování kebabáren.

## ✨ Features

### Backend (Django)
- ✅ **REST API** s Django Ninja
- ✅ **CORS** povoleno pro frontend
- ✅ **4 DB modely**: KebabShop, User, Recenze, Fotografie
- ✅ **Responsive HTML templates** s moderním designem
- ✅ **API Playground** - interaktivní testování API

### Frontend (Vue 3)
- ✅ **SPA (Single Page Application)** s Vue Router
- ✅ **Async/Await** + Fetch API pro API volání
- ✅ **Responsive Grid Layout** na mobily
- ✅ **Moderní CSS styling** s gradientem
- ✅ **Komponenty**: KebabList, KebabDetail

## 🚀 Quick Start

### 1. Backend Setup (Django)

```powershell
# Nainstaluj dependencies
pip install -r requirements.txt

# Spusť migraci databáze
python prj/manage.py migrate

# Nahraj testovací data
python prj/manage.py loaddata kebabshops app_users recenze fotografie users

# Spusť server
python prj/manage.py runserver
```

Server běží na: **http://127.0.0.1:8000**

### 2. Frontend Setup (Vue 3)

```powershell
cd frontend

# Nainstaluj Node dependences
npm install

# Spusť dev server
npm run dev
```

Frontend běží na: **http://localhost:5174** (nebo http://localhost:5173)

## 📍 URLs

### Django Backend (http://127.0.0.1:8000)
- **/** - Domovská stránka se seznamem kebabáren
- **/detail/{id}/** - Detail konkrétní kebabárny
- **/about/** - O projektu
- **/api-playground/** - Interaktivní testování API
- **/login/** - Přihlášení (demo)
- **/admin/** - Django admin

### Vue Frontend (http://localhost:5174)
- **/** - Domovská stránka se seznamem kebabáren
- **/kebab/{id}** - Detail konkrétní kebabárny

## 🔌 REST API Endpoints

```
GET    /api/kebabshop           - Seznam všech kebabáren
GET    /api/kebabshop/{id}      - Detail kebabárny
POST   /api/kebabshop           - Vytvoř novou kebabárnu
PUT    /api/kebabshop/{id}      - Uprav existující kebabárnu
```

### Příklad GET request:
```bash
curl http://127.0.0.1:8000/api/kebabshop
```

### Příklad POST request:
```bash
curl -X POST http://127.0.0.1:8000/api/kebabshop \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Kebab",
    "address": "Street 1",
    "city": "Prague",
    "opening_hours": "10-22",
    "email": "info@kebab.com",
    "meat_type": "lamb"
  }'
```

## 📊 Databáze Models

```python
# KebabShop - Hlavní model
- name: CharField(200)
- address: CharField(255)
- city: CharField(100)
- opening_hours: CharField(100)
- email: EmailField()
- meat_type: CharField(100)

# User - Uživatelé
- username: CharField(100)
- password_hash: CharField(255)
- role: CharField(50)  # 'customer', 'owner'
- avatar_url: URLField()
- favorite_kebab_shop: ForeignKey(KebabShop)

# Recenze - Recenze kebabáren
- uzivatel: ForeignKey(User)
- kebabarna: ForeignKey(KebabShop)
- hodnoceni_celkove: IntegerField()
- hodnoceni_maso: IntegerField()
- komentar: TextField()
- datum_vytvoreni: DateTimeField()

# Fotografie - Fotky k recenzím
- recenze: ForeignKey(Recenze)
- url_odkaz: URLField()
```

## 🧪 Testovací Data

Aplikace přichází s 5 přednastavenými kebabárnami:
1. **U Zlateho Oboji** - Praha (lamb)
2. **Kebab Express** - Brno (beef)
3. **Noční Šunka** - Ostrava (chicken)
4. **Veggie Delight** - Praha (vegetarian)
5. **Big Kebab Central** - Brno (mixed)

Plus 5 uživatelů a recenzí.

## 🛠️ Technologie

| Komponenta | Technologie |
|-----------|------------|
| Backend | Django 6.0, Django Ninja, Django CORS Headers |
| Frontend | Vue 3, Vite, Vue Router |
| Databáze | SQLite |
| API | REST (JSON) |
| Styling | Pure CSS (bez frameworku) |

## 📝 Jak Funguje CORS

Frontend na `localhost:5174` se připojuje k API na `127.0.0.1:8000`. 

**Django CORS settings** (`prj/settings.py`):
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:5174',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:5174',
]
```

## 🎓 Edukační Obsah

Projekt demonstruje:
- ✅ **Asynchronní JavaScript** - async/await, Promise, fetch()
- ✅ **REST API Design** - GET, POST, PUT operace
- ✅ **Vue 3 Components** - list, detail, router
- ✅ **Django ORM** - modely, relace, migracje
- ✅ **CORS bezpečnost** - cross-origin requests
- ✅ **Responsive Design** - CSS Grid, mobily

## 📞 Support

Pokud se cokoliv nepovedlo:
1. Ujistěte se, že Django server běží: `python prj/manage.py runserver`
2. Ujistěte se, že Vue dev server běží: `cd frontend && npm run dev`
3. Zkontrolujte browser console (F12) pro JavaScript chyby
4. Zkontrolujte Django logs v terminálu

---

**Vytvořeno jako školský projekt pro Web Development 2025** 🎓
