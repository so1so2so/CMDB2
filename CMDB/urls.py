from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from app.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^$',login),
    url(r'^login/$',login),
    url(r'^idc/$',idc),
    url(r'^addidc/$',addidc),
    url(r'^idc/idc_delete/$',idc_delete),
    url(r'^mac/$',mac),
    url(r'^addmac/$',addmac),
    url(r'^mac/mac_delete/$',mac_delete),
    url(r'^mac/mac_edit/$',mac_edit),
    url(r'^macresult/$',macresult),
    url(r'^group/$',group),
    url(r'^group_result/$',group_result),
    url(r'^group/group_delete/$',group_delete),
    url(r'^group_manage/$',group_manage),
    url(r'^group_manage/group_manage_delete/$',group_manage_delete),
    url(r'addgroup_host/$',addgroup_host),
    url(r'^file/$',file),
    url(r'^file_result',file_result),
    url(r'^command/$',command),
    url(r'^command_group/$',command_group),
    url(r'^command_group/check_result/$',check_result),
    url(r'^command_group_result/$',command_group_result),
    url(r'^command_result/$',command_result),
    url(r'^job/$',job),
    url(r'^asset/$',asset),
    url(r'^asset_auto/$',asset_auto),
    url(r'^asset_auto_result/$',asset_auto_result),
    url(r'asset/asset_delete/$',asset_delete),
    url(r'^authin/$',authin),
    # url(r'accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^monitor/$',monitor),
    url(r'^data/$',getdata),
    url(r'monitor_result/$',monitor_result),
    url(r'monitor_data/$',monitor_data),
]
