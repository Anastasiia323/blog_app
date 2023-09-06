from django.urls import path
from .presentation.views.twits import (
    add_twit,
    twit_list,
    tags_controller,
    get_twit_controller,
    delete_twit_controller,
    edit_twit_controller,
    get_posts_by_tag_controller
)
from .presentation.views.account import (
    account_controller,
    account_edit_controller,
    account_add_controller,
    change_email_controller,
    change_email_confirm_controller,
    change_photo_controller,
    get_account_by_id_controller,
    follow_unfollow_controller
)
from .presentation.views.login import login_user
from .presentation.views.notifications import notifications_controller
from .presentation.views.add_user import (
    confirmation_user,
    registrate_user,
    email_notification_controller,
    registration_confirm_controller
)
from .presentation.views.trends import trends_in_your_country_controller
from .presentation.views.home import home_controller
from .presentation.views.logout import logout_controller
from .presentation.views.account import change_email_confirm_controller
from .presentation.views.comments import create_comment_controller


urlpatterns = [
    path('', home_controller, name='home'),
    path('account/<int:account_id>/', get_account_by_id_controller, name='account-id'),
    path('subscription/<int:account_id>/', follow_unfollow_controller, name='subscription'),
    path('<int:tag_id>/posts_by_tag', get_posts_by_tag_controller, name='tags-posts'),
    path('tags/', tags_controller, name='tags'),
    path('post/add/', add_twit, name='add-twit'),
    path('twit/<int:twit_id>/', get_twit_controller, name='twit'),
    path('<int:twit_id>/delete/', delete_twit_controller, name='delete-twit'),
    path('<int:twit_id>/edit/', edit_twit_controller, name='edit-twit'),
    path('<int:twit_id>/comment/', create_comment_controller, name='create-comment'),
    path('trends/', trends_in_your_country_controller, name='trends'),
    path('account/', account_controller, name='account'),
    path('account/add/', account_add_controller, name='account-add'),
    path('account/edit', account_edit_controller, name='account-edit'),
    path('account/edit/change_email/', change_email_controller, name='change-email'),
    path('change_email_confirmation/', change_email_confirm_controller, name='confirm-email'),
    path('change_photo/', change_photo_controller, name='change-photo'),
    path('notifications/', notifications_controller, name='notifications'),
    path('signup/', registrate_user, name='signup'),
    path('login/', login_user, name='login'),
    path('confirm/', registration_confirm_controller, name='confirm'),
    path('notification/', email_notification_controller, name='message'),
    path('logout/', logout_controller, name='logout'),
    path('account/add_twit', add_twit, name='add-twit')
]
