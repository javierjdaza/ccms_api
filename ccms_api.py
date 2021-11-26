from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from ccms import ccms_auth
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# from magnum import Magnum
app = FastAPI( title="CCMS ID Authentication",
                description="An REST API for CCMS ID Authentication",
                version="0.0.1",
                openapi_tags = [
                                {
                                    "name": "CCMS ID Authentication",
                                    "description": "users endpoint"
                                }]
                )

# handler = Magnum(app)
# GET - Get information
# POST - Create somethin new (for exp, new row)
# PUT - Update
# DELETE - Delete Something

# ===============================
# Running uvicorn web server
# ===============================
# - uvicorn miapi:app --reload
# - miapi -> The name of my python api file (without .py)
# - app -> The name of the instance of FastAPI() Class

# ================
# Documentation
# ================
# - endpoint/docs

# ====================================
# Path description to handle errors
# ====================================
# - name_parameter: type_parameter = Path(None, description = 'Description for the documentation, gt = Greater than, lt = Less Than, get = Greater equals than, let = Less equals than)

# ===================
# Query Parameter
# ===================
# - No recibe nada por parametro, va directo en la url y su separacion es '?'. Ejm: http://127.0.0.1:8000/get-by-name?name=javier

# ===================
# Path Parameter
# ===================
# - SI recibe valor por parametro, su separacion es '/'. Ejm: http://127.0.0.1:8000/get-student/1



# IMPORTANT THINGS
# - "I'd recommend putting any required parameters in the path, and any optional parameters should certainly be query string parameters."
# students = {
#     1: {
#         'name':'javier',
#         'age': 26,d
#         'class': 'year 12'
#     }
# }


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Credentials(BaseModel):
    ccms_id: str
    password: str

@app.get('/')
def home():
    html_content = """
                    
                    <html>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
                        <head>
                            <title>CCMS OAUTH | API</title>
                        </head>
                        <body>
                            <figure class="text-center">
                                <br>
                                <br>
                                <br>
                                <h2>
                                    Welcome to<br><strong>CCMS OAUTH</strong>
                                </h2>
                                <br>
                                <h5>
                                    @Author: Javier Daza - Daniela Giraldo - Jaime Herrera
                                    <br>
                                    Teleperformance
                                    <br>
                                    DSDG Team
                                </h5>
                            </figure>
                        </body>
                    </html>
                    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post('/ccms_auth/',tags=["CCMS ID Authentication"])
async def ccms_authentication(credentials : Credentials):

        return ccms_auth(user_id = credentials.ccms_id,password = credentials.password)

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=80)