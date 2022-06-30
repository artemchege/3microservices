import uvicorn
from fastapi import FastAPI, status

from schemas import Email
from service import send_email_async

app = FastAPI(
    docs_url='/notification/docs',
    openapi_url="/notification/openapi.json"
)


@app.post('/notification/notify/', status_code=status.HTTP_200_OK, tags=['auth'])
async def email_notify(email_request: Email):
    await send_email_async(subject='For nothing', email_to=email_request.email, body='Hope my microservice project '
                                                                                     'satisfies you')
    return {"Notified": True}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5002)
