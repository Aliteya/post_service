from .posts_controller import post_router
from .users_controller import user_router
from .votes_controller import vote_router

__all__= ["post_router", "user_router", "vote_router"]