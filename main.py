import uvicorn
from app.api import app

#http://127.0.0.1:8000 и http://127.0.0.1:8000/items
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')

