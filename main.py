# define core engine
from fastapi import FastAPI
from starlette import applications
from starlette.middleware.cors import CORSMiddleware

# import controller
from apps.routes import excel_router, csv_router
from connection import Connection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# register routes
app.include_router(excel_router)
app.include_router(csv_router)


@app.on_event("startup")
def startup():
    applications.conf = dict()
    # define connection
    conn = Connection()
    # get config
    applications.conf['config'] = conn.get_config
    applications.conf['cache'] = conn.cache_conn()


@app.on_event("shutdown")
def shutdown():
    print("[Execute value when shutdown]")
