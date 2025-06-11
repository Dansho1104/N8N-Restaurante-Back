from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from app.api import dishes
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                await self.disconnect(connection)

manager = ConnectionManager()

app = FastAPI()
app.include_router(dishes.router)
app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

@app.websocket("/ws/orders")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Opcional: puedes procesar los datos recibidos aquí
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        manager.disconnect(websocket)
        print(f"Error en WebSocket: {str(e)}")

@app.post("/dishes")
async def create_dish(request: Request):
    data = await request.json()
    if 'id' in data:
        del data['id']
    # Asegurar que productos sea siempre una lista de strings individuales
    if 'productos' in data:
        if not isinstance(data['productos'], list):
            if data['productos'] is None:
                data['productos'] = []
            else:
                data['productos'] = [data['productos']]
        # Si la lista tiene un solo string con comas, dividirlo
        productos_limpios = []
        for item in data['productos']:
            if isinstance(item, str) and ',' in item:
                productos_limpios.extend([p.strip() for p in item.split(',') if p.strip()])
            elif isinstance(item, str):
                productos_limpios.append(item.strip())
        data['productos'] = productos_limpios
    print("[WEBHOOK] Pedido recibido:", data)
    await manager.broadcast({"new_order": data})
    return {"received_data": data}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Restaurant API"}