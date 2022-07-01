from sqlalchemy.future import select

from models import Profile, Subscription
from schemas import CreateProfile, CreateSubscription
from database import async_session_local


async def create_profile_in_db(create_profile: CreateProfile, user_id: int):
    async with async_session_local() as session:
        async with session.begin():
            profile = Profile(user_id=user_id, city=create_profile.city)
            session.add(profile)
            await session.flush()
            return profile


async def get_profile_by_user_id(user_id: int):
    async with async_session_local() as session:
        async with session.begin():
            db_request = await session.execute(select(Profile).where(Profile.user_id == user_id))
            profile = db_request.one_or_none()
            if profile is not None:
                (profile,) = profile
            return profile


async def create_subscription_in_db(create_subscription: CreateSubscription, profile):
    async with async_session_local() as session:
        async with session.begin():
            sub = Subscription(profile_id=profile.id, name=create_subscription.name)
            session.add(sub)
            await session.flush()
            return sub
