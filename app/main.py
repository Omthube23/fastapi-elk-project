from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import json
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI ELK Demo", version="1.0.0")

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

# In-memory storage
items_db = []

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {
        "message": "Welcome to FastAPI with ELK Stack",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/items/")
async def create_item(item: Item):
    logger.info(f"Creating new item: {item.name}")
    item_dict = item.dict()
    item_dict["id"] = len(items_db) + 1
    item_dict["created_at"] = datetime.now().isoformat()
    items_db.append(item_dict)
    logger.info(f"Item created successfully: {item_dict}")
    return item_dict

@app.get("/items/")
async def list_items():
    logger.info(f"Listing all items. Total count: {len(items_db)}")
    return {"items": items_db, "count": len(items_db)}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    logger.info(f"Fetching item with ID: {item_id}")
    for item in items_db:
        if item["id"] == item_id:
            logger.info(f"Item found: {item}")
            return item
    logger.warning(f"Item not found: {item_id}")
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Attempting to delete item: {item_id}")
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(i)
            logger.info(f"Item deleted: {deleted_item}")
            return {"message": "Item deleted", "item": deleted_item}
    logger.error(f"Delete failed - Item not found: {item_id}")
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/logs/test")
async def test_logs():
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    return {"message": "Various log levels generated"}
