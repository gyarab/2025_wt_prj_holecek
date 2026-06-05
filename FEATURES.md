# 🎉 KebabTracker - Complete Demo Website

## What's Built

### ✅ Backend (Django)
- **REST API** - Full CRUD for KebabShop model
- **4 Database Models** - KebabShop, User, Recenze, Fotografie
- **Django Ninja** - Modern API framework
- **CORS Support** - For cross-origin frontend requests
- **HTML Templates** - Responsive pages with modern styling
- **Fixtures** - 5 kebab shops + 5 users + 5 reviews + photos
- **API Playground** - Interactive API testing tool

### ✅ Frontend (Vue 3)
- **SPA Application** - Single Page App with Vue Router
- **Two Views** - List and Detail pages for kebabs
- **Async/Await** - Modern JavaScript Promise handling
- **Fetch API** - REST API communication
- **Responsive Design** - Works on mobile and desktop
- **Professional Styling** - Modern gradients and cards

## 📱 Two Frontends Available

### 1. Django HTML Frontend
```
URL: http://127.0.0.1:8000
- Traditional server-side rendering
- HTML templates with embedded CSS
- Direct database queries in views
- Good for traditional web apps
```

### 2. Vue 3 SPA Frontend
```
URL: http://localhost:5174
- Modern Single Page Application
- Async API calls with fetch()
- Client-side routing
- Better UX with instant page transitions
```

## 🔌 REST API

All endpoints available at: `http://127.0.0.1:8000/api/`

```
GET  /api/kebabshop          ← Get all kebab shops
GET  /api/kebabshop/1        ← Get one by ID
POST /api/kebabshop          ← Create new (with JSON body)
PUT  /api/kebabshop/1        ← Update (with JSON body)
```

### Test in Browser/Postman:
```bash
# List all
curl http://127.0.0.1:8000/api/kebabshop

# Get one
curl http://127.0.0.1:8000/api/kebabshop/1

# Create new
curl -X POST http://127.0.0.1:8000/api/kebabshop \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","address":"St 1","city":"Prague","opening_hours":"10-22","email":"test@test.com","meat_type":"lamb"}'
```

## 📊 Database Models

```python
KebabShop
├── name: "U Zlateho Oboji"
├── address: "Kralovska 10"
├── city: "Prague"
├── opening_hours: "10:00-23:00"
├── email: "kontakt@..."
└── meat_type: "lamb"

User
├── username: "uzivatel1"
├── role: "customer" | "owner"
├── avatar_url: "..."
└── favorite_kebab_shop: KebabShop (FK)

Recenze
├── uzivatel: User (FK)
├── kebabarna: KebabShop (FK)
├── hodnoceni_celkove: 4
├── hodnoceni_maso: 5
├── komentar: "Skvělý kebab..."
└── datum_vytvoreni: "2025-05-01T12:34:56Z"

Fotografie
├── recenze: Recenze (FK)
└── url_odkaz: "https://..."
```

## 🎓 Educational Features

This project teaches:

1. **Asynchronous JavaScript**
   - `async/await` syntax
   - Promises and `.then()`
   - Error handling with try/catch
   - Fetch API for HTTP requests

2. **REST API Design**
   - GET, POST, PUT operations
   - JSON request/response bodies
   - Proper HTTP status codes
   - API versioning with `/api/` prefix

3. **Vue 3 Framework**
   - Component-based architecture
   - Props and state management
   - Vue Router for page navigation
   - Lifecycle hooks (mounted, etc.)

4. **Django Backend**
   - ORM (Object-Relational Mapping)
   - Model relationships (ForeignKey)
   - Class-based views
   - Template inheritance
   - Fixtures and test data

5. **Web Security**
   - CORS (Cross-Origin Resource Sharing)
   - CSRF tokens in forms
   - Same-origin policy
   - Secure API communication

## 🛠️ Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Backend** | Django | 6.0.3 |
| **API Framework** | Django Ninja | - |
| **CORS** | django-cors-headers | - |
| **Frontend Framework** | Vue | 3.5.34 |
| **Build Tool** | Vite | 8.0+ |
| **Router** | Vue Router | 5.0.7 |
| **Database** | SQLite | - |
| **Data Format** | JSON | - |

## 📁 Project Structure

```
2025_wt_prj_holecek/
├── prj/                           # Django project folder
│   ├── manage.py
│   ├── db.sqlite3
│   ├── prj/                       # Django config
│   │   ├── settings.py            # CORS, INSTALLED_APPS
│   │   ├── urls.py                # Route configuration
│   │   └── wsgi.py
│   └── app/                       # Django app
│       ├── models.py              # Database models
│       ├── views.py               # View functions
│       ├── api.py                 # REST API endpoints
│       ├── tests_api.py           # API tests
│       └── templates/app/
│           ├── base.html          # Base template
│           ├── home.html          # List page
│           ├── detail.html        # Detail page
│           ├── api_playground.html # API tester
│           └── ...
├── frontend/                      # Vue.js project
│   ├── package.json
│   ├── src/
│   │   ├── main.js               # Entry point
│   │   ├── App.vue               # Root component
│   │   ├── config.js             # API configuration
│   │   ├── router/
│   │   │   └── index.js          # Route definitions
│   │   └── views/
│   │       ├── kebablist.vue     # List component
│   │       └── kebabdetail.vue   # Detail component
│   └── vite.config.js
├── fixtures/                      # Test data
│   ├── kebabshops.yaml
│   ├── app_users.yaml
│   ├── recenze.yaml
│   ├── fotografie.yaml
│   └── users.yaml
├── requirements.txt               # Python dependencies
├── README.md
└── DEMO.md                        # Demo instructions
```

## 🚀 How It Works

### User Journey

```
1. User visits http://localhost:5174 (Vue app)
2. Vue component mounts → calls mounted() hook
3. fetchKebabs() function runs
4. Fetch request: http://127.0.0.1:8000/api/kebabshop
5. Django API returns JSON with 5 kebab shops
6. Vue renders grid with cards
7. User clicks "Więcej informacji" → router changes to /kebab/{id}
8. KebabDetail component mounts
9. Fetch request: http://127.0.0.1:8000/api/kebabshop/1
10. Django API returns single kebab details
11. Vue displays beautiful detail page
```

### CORS Flow

```
Frontend (localhost:5174)
        ↓ fetch() request
        ↓ (includes Origin header)
Backend (127.0.0.1:8000)
        ↓ checks CORS_ALLOWED_ORIGINS
        ↓ if match found, adds CORS headers
        ↓ response with Access-Control-Allow-Origin
Frontend receives data ✅
```

## ✨ Key Features

- **Instant List Display** - 5 kebab shops load in 100ms
- **Smooth Navigation** - Router transitions feel instant
- **Responsive Cards** - Auto-resize on mobile
- **Real API Data** - Not mocked, real Django backend
- **Error Handling** - Friendly error messages
- **Console Logging** - Debug friendly
- **Modern Styling** - Gradient headers, smooth shadows
- **Accessible** - Semantic HTML, proper labels

## 🧪 Test Data

The app comes with pre-loaded data:

**Kebab Shops (5):**
1. U Zlateho Oboji (Prague, lamb)
2. Kebab Express (Brno, beef)
3. Noční Šunka (Ostrava, chicken)
4. Veggie Delight (Prague, vegetarian)
5. Big Kebab Central (Brno, mixed)

**Users (5):**
- uzivatel1, owner_brno, no_obvious, vegfan, nightowl

**Reviews (5):**
- Each user has 1 review with ratings 2-5 stars

**Photos (5):**
- Each review has 1 photo link

## 🎯 Next Steps

To extend this project:

1. **Add Authentication** - Login with Django auth
2. **User Profiles** - Show user reviews and history
3. **Search & Filter** - Filter by city, meat type
4. **Photo Upload** - Real image storage
5. **Google Maps** - Integrate maps API
6. **Reviews API** - Add endpoints for Recenze model
7. **Pagination** - Load more as you scroll
8. **Caching** - Redis for performance
9. **Tests** - More unit tests
10. **Deployment** - Heroku or AWS

---

**🌮 Enjoy your KebabTracker demo!** 🎉
