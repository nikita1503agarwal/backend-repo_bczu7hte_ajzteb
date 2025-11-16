import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Photo Gallery API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PHOTOS: List[dict] = [
    {
        "id": 1,
        "title": "Misty Mountain Sunrise",
        "imageUrl": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=400&q=60&auto=format&fit=crop",
        "category": "Nature",
        "tags": ["mountains", "sunrise", "nature", "mist"],
        "location": "Banff, Canada",
        "camera": "Nikon D850",
        "settings": "35mm • f/8 • 1/200s • ISO 200",
        "dateTaken": "2023-04-12"
    },
    {
        "id": 2,
        "title": "City Lights at Dusk",
        "imageUrl": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=400&q=60&auto=format&fit=crop",
        "category": "City",
        "tags": ["city", "night", "lights", "skyline"],
        "location": "Tokyo, Japan",
        "camera": "Sony A7 III",
        "settings": "24mm • f/4 • 1/60s • ISO 800",
        "dateTaken": "2022-11-05"
    },
    {
        "id": 3,
        "title": "Portrait in Golden Hour",
        "imageUrl": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&q=60&auto=format&fit=crop",
        "category": "Portrait",
        "tags": ["portrait", "golden hour", "bokeh"],
        "location": "Los Angeles, USA",
        "camera": "Canon EOS R6",
        "settings": "50mm • f/1.8 • 1/400s • ISO 100",
        "dateTaken": "2023-07-19"
    },
    {
        "id": 4,
        "title": "Desert Dune Curves",
        "imageUrl": "https://images.unsplash.com/photo-1501785888041-5a08a7c06a4d?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1501785888041-5a08a7c06a4d?w=400&q=60&auto=format&fit=crop",
        "category": "Nature",
        "tags": ["desert", "dunes", "sand", "patterns"],
        "location": "Merzouga, Morocco",
        "camera": "Fujifilm X-T4",
        "settings": "35mm • f/9 • 1/250s • ISO 160",
        "dateTaken": "2021-09-02"
    },
    {
        "id": 5,
        "title": "Arctic Aurora",
        "imageUrl": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=400&q=60&auto=format&fit=crop",
        "category": "Nature",
        "tags": ["aurora", "northern lights", "arctic", "night"],
        "location": "Tromsø, Norway",
        "camera": "Nikon Z6",
        "settings": "20mm • f/2.8 • 5s • ISO 1600",
        "dateTaken": "2020-02-14"
    },
    {
        "id": 6,
        "title": "Wildlife: The Stare",
        "imageUrl": "https://images.unsplash.com/photo-1501706362039-c06b2d715385?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1501706362039-c06b2d715385?w=400&q=60&auto=format&fit=crop",
        "category": "Wildlife",
        "tags": ["lion", "wildlife", "safari"],
        "location": "Maasai Mara, Kenya",
        "camera": "Canon 5D Mark IV",
        "settings": "200mm • f/4 • 1/1000s • ISO 400",
        "dateTaken": "2019-08-21"
    },
    {
        "id": 7,
        "title": "Rainy Street Reflections",
        "imageUrl": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=400&q=60&auto=format&fit=crop",
        "category": "City",
        "tags": ["rain", "street", "reflections", "neon"],
        "location": "Seoul, South Korea",
        "camera": "Sony A7C",
        "settings": "35mm • f/2 • 1/125s • ISO 1600",
        "dateTaken": "2023-03-03"
    },
    {
        "id": 8,
        "title": "Minimalist Architecture",
        "imageUrl": "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?w=400&q=60&auto=format&fit=crop",
        "category": "Architecture",
        "tags": ["architecture", "minimal", "geometry"],
        "location": "Valencia, Spain",
        "camera": "Leica Q2",
        "settings": "28mm • f/5.6 • 1/320s • ISO 100",
        "dateTaken": "2022-05-28"
    },
    {
        "id": 9,
        "title": "Forest Trail",
        "imageUrl": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=400&q=60&auto=format&fit=crop",
        "category": "Nature",
        "tags": ["forest", "trail", "green", "hike"],
        "location": "Black Forest, Germany",
        "camera": "Nikon D750",
        "settings": "24mm • f/5 • 1/160s • ISO 320",
        "dateTaken": "2021-06-17"
    },
    {
        "id": 10,
        "title": "Seaside Long Exposure",
        "imageUrl": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=80&auto=format&fit=crop",
        "thumbnailUrl": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400&q=60&auto=format&fit=crop",
        "category": "Seascape",
        "tags": ["sea", "long exposure", "waves", "blue"],
        "location": "Big Sur, USA",
        "camera": "Sony A7R IV",
        "settings": "24mm • f/11 • 15s • ISO 100",
        "dateTaken": "2018-10-09"
    },
]

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/photos")
def list_photos():
    return PHOTOS

@app.get("/photos/{photo_id}")
def get_photo(photo_id: int):
    photo = next((p for p in PHOTOS if p["id"] == photo_id), None)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo

@app.get("/test")
def test_database():
    return {
        "backend": "✅ Running",
        "database": "❌ Not Used",
        "database_url": "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set",
        "database_name": "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set",
        "connection_status": "N/A",
        "collections": []
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
