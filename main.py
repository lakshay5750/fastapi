from fastapi import FastAPI,HTTPException,Query
from models import MenuItem,MenuResponse
from data import items

app=FastAPI(
    title="Chai point menu api",
    description="Read only menu API for Kiosk display and mobile app"
)

@app.get("/")
def root():
    return "welcome to the chai_aur_code"


#/menu ->path
#/menu?category=chai

@app.get("/menu",response_model=MenuResponse)
def get_menu(category:str|None=Query(None,description="Filter by chai,snack or combo")):
    if category:
        filtered=[item for item in items if item['category'].lower()==category.lower()]
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No item found in category: {category}")
        return MenuResponse(count=len(filtered),items=filtered)
    
    return MenuResponse(count=len(items),items=items)

@app.get("/menu/{item_id}",response_model=MenuItem)
def get_item(item_id:int)->MenuItem:
    for item in items:
        if item['id']==item_id:
            return item
    raise HTTPException(status_code=404,detail=f"Menu item with id: {item_id} not found")
    
    