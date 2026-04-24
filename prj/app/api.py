from ninja import NinjaAPI

api = NinjaAPI()

class Message:
    title: str

@api.get("/kebab")
def kebab(request):
    kebabs = kebab.objects.all()
    return {"kebabs": kebabs}

@api.get("/kebab/{kebab_id}")
def get_kebab(request, kebab_id: int):
    kebab = kebab.objects.get(id=kebab_id)
    return {"kebab": kebab}
