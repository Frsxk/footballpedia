from django.urls import path
from main.views import get_username, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, create_product, show_product, login_user, logout_user, register, edit_product, delete_product, add_product_entry_ajax, proxy_image, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-username/', get_username, name='get_username'),
]