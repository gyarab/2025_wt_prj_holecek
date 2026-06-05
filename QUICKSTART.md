# ⚡ Quick Start - 2 Minutes

## Start Backend

```powershell
# Terminal 1
cd c:\Users\krystof.holecek.s\Desktop\2025_wt_prj_holecek
pip install -r requirements.txt
python prj/manage.py migrate
python prj/manage.py loaddata kebabshops app_users recenze fotografie users
python prj/manage.py runserver
```

✅ Django runs at **http://127.0.0.1:8000**

## Start Frontend

```powershell
# Terminal 2
cd c:\Users\krystof.holecek.s\Desktop\2025_wt_prj_holecek\frontend
npm install
npm run dev
```

✅ Vue app runs at **http://localhost:5174**

## Visit Websites

| URL | Type | Features |
|-----|------|----------|
| http://127.0.0.1:8000 | Django HTML | List, detail, API playground |
| http://localhost:5174 | Vue SPA | Modern async list, detail |
| http://127.0.0.1:8000/api-playground | Interactive | Test API endpoints live |
| http://127.0.0.1:8000/admin | Admin | Django admin panel |

## API Examples

```bash
# Get all kebabs
curl http://127.0.0.1:8000/api/kebabshop | jq

# Get one kebab (id=1)
curl http://127.0.0.1:8000/api/kebabshop/1 | jq

# Create new (PowerShell)
$body = @{name="New";address="St";city="Prague";opening_hours="10-22";email="x@x.com";meat_type="lamb"} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/kebabshop" -Body $body -ContentType "application/json"
```

## Demo Data

5 kebab shops pre-loaded:
- U Zlateho Oboji (Prague, lamb)
- Kebab Express (Brno, beef)  
- Noční Šunka (Ostrava, chicken)
- Veggie Delight (Prague, vegetarian)
- Big Kebab Central (Brno, mixed)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: ninja` | Run `pip install -r requirements.txt` |
| `Port 8000 in use` | Change to `python prj/manage.py runserver 8001` |
| `Port 5174 in use` | Vite auto-tries 5175, 5176, etc. |
| `NetworkError when attempting fetch` | Check Django server is running |
| `Cannot GET /` | Make sure you're on http://127.0.0.1:8000 not localhost:8000 |

## Files to Know

- `prj/app/api.py` - REST API endpoints
- `prj/app/models.py` - Database models
- `prj/app/views.py` - Django views
- `frontend/src/config.js` - API URL config
- `frontend/src/views/kebablist.vue` - List component
- `frontend/src/views/kebabdetail.vue` - Detail component

---

That's it! You now have a fully functional Django + Vue 3 web app! 🌮
