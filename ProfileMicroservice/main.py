import uvicorn
from fastapi import FastAPI, status, Depends, HTTPException
from crud import get_profile_by_user_id, create_profile_in_db, create_subscription_in_db
from schemas import TokenData, CreateProfile, CreatedProfile, CreatedSubscription, CreateSubscription
from jwt import get_current_user

app = FastAPI(
    docs_url='/profile/docs',
    openapi_url="/profile/openapi.json"
)


@app.post('/profile/get_or_create_subscription/', status_code=status.HTTP_200_OK, response_model=CreatedSubscription)
async def subscribe(create_subscription: CreateSubscription, user: TokenData = Depends(get_current_user)):
    profile = await get_profile_by_user_id(user.id)
    if not profile:
        raise HTTPException(status_code=400, detail="Authorized user does not have profile")
    else:
        subscription = await create_subscription_in_db(create_subscription=create_subscription, profile=profile)
    return subscription


@app.post('/profile/get_or_create_profile/', status_code=status.HTTP_200_OK, response_model=CreatedProfile)
async def get_or_create_profile(create_profile: CreateProfile, user: TokenData = Depends(get_current_user)):
    profile = await get_profile_by_user_id(user.id)
    if not profile:
        profile = await create_profile_in_db(user_id=user.id, create_profile=create_profile)
    return profile


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5003)
