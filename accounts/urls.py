from django.urls import path, re_path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('subscriber/', views.subscriber, name='subscriber'),
    path('news/', views.news, name='news'),

    path('product/', views.product, name='product'),
    path('subproduct/<int:id>', views.subproduct, name='subproduct'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('quote/', views.quote, name='quote'),

    path('orders/', views.orders, name='orders'),
    path('customerquote/', views.customerquote, name='customerquote'),
    path('customerquotedelete/<int:id>', views.customerquotedelete, name='customerquotedelete'),
    path('editprofiledetails/', views.editprofiledetails, name='editprofiledetails'),


    path('checkout/', views.checkout, name='checkout'),
    # path('payment/<int:id>', views.call_back_url, name='payment'),
    re_path(r'^payment/$', views.call_back_url, name='payment'),
    path('offlinepayment/', views.offlinepayment, name='offlinepayment'),
    # path('paymentsuccess/', views.paymentSuccess, name='paymentsuccess'),
    # path('paymentcancel/', views.paymentCancel, name='paymentcancel'),
    # path('webhook/stripe/', views.my_webhook_view, name='webhook-stripe'),

    path('signup', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),


    ###### devadmin URL  ########

    path('devadmin/', views.dev, name='dev'),
    path('devadmin/addadmin/', views.addadmin, name='addadmin'),
    path('devadmin/adminlist/', views.adminlist, name='adminlist'),
    path('devadmin/admindelete/<int:id>', views.admindelete, name='admindelete'),  
    path('devadmin/adminchangepass/<int:id>', views.adminchangepass, name='adminchangepass'),      
    path('devadmin/admindedit/<int:id>', views.adminedit, name='adminedit'),      
    path('devadmin/logout/', views.adminlogout, name='adminlogout'),

    path('devadmin/dashboard/', views.dashboard, name='dashboard'),
    path('devadmin/monthlyfilter/', views.monthlyfilter, name='monthlyfilter'),

    path('devadmin/contactlist/', views.admincontactlist, name='admincontactlist'),
    path('devadmin/contact/<int:id>', views.admincontact, name='admincontact'),

    path('devadmin/subscriberlist/', views.adminsubscriberlist, name='adminsubscriberlist'),

    path('devadmin/addproduct/', views.adminaddproduct, name='adminaddproduct'),
    path('devadmin/addsubproduct/', views.adminaddsubproduct, name='adminaddsubproduct'),
    path('devadmin/productlist/', views.adminproductlist, name='adminproductlist'),
    path('devadmin/subproductlist/', views.adminsubproductlist, name='adminsubproductlist'),

    path('devadmin/admineditproduct/<int:id>', views.admineditproduct, name='admineditproduct'),    
    path('devadmin/admindeleteproduct/<int:id>', views.admindeleteproduct, name='admindeleteproduct'),    

    path('devadmin/admineditsubproduct/<int:id>', views.admineditsubproduct, name='admineditsubproduct'),    
    path('devadmin/admindeletesubproduct/<int:id>', views.admindeletesubproduct, name='admindeletesubproduct'),      
    
    path('devadmin/news/', views.adminaddnews, name='adminaddnews'),
    path('devadmin/newslist/', views.adminnewslist, name='adminnewslist'),
    path('devadmin/admineditnews/<int:id>', views.admineditnews, name='admineditnews'),    
    path('devadmin/admindeletenews/<int:id>', views.admindeletenews, name='admindeletenews'), 


    path('devadmin/buserlist/', views.adminabusinessusers, name='adminabusinessusers'),
    path('devadmin/buserextradetails/<int:id>', views.buserextradetails, name='buserextradetials'),
    path('devadmin/iuserlist/', views.adminaindividualusers, name='adminaindividualusers'),
    path('devadmin/iuserextradetails/<int:id>', views.iuserextradetails, name='iuserextradetails'),
    path('devadmin/ijuserlist/', views.adminaindividualjointusers, name='adminaindividualjointusers'),
    path('devadmin/ijuserextradetails/<int:id>', views.ijuserextradetails, name='ijuserextradetails'),
    path('devadmin/customers/', views.admincustomers, name='admincustomers'),

    path('devadmin/transaction/', views.transaction, name='transaction'),
    path('devadmin/transactionupdate/<int:id>', views.transactionupdate, name='transactionupdate'),
    path('devadmin/quote/', views.adminquote, name='adminquote'),


    path('devadmin/homebanner/', views.homebanner, name='homebanner'),
    path('devadmin/addhomebanner/', views.addhomebanner, name='addhomebanner'),
    path('devadmin/edithomebanner/<int:id>', views.edithomebanner, name='edithomebanner'),
    path('devadmin/deletehomebanner/<int:id>', views.deletehomebanner, name='deletehomebanner'),

    path('devadmin/homexploreproducts/', views.homexploreproducts, name='homexploreproducts'),
    path('devadmin/addexploreproduct/', views.addexploreproduct, name='addexploreproduct'),
    path('devadmin/editexploreproduct/<int:id>', views.editexploreproduct, name='editexploreproduct'),
    path('devadmin/deleteexploreproduct/<int:id>', views.deleteexploreproduct, name='deleteexploreproduct'),

    path('devadmin/hometestinomials/', views.hometestinomials, name='hometestinomials'),
    path('devadmin/addhometestinomials/', views.addhometestinomials, name='addhometestinomials'),
    path('devadmin/edithometestinomials/<int:id>', views.edithometestinomials, name='edithometestinomials'),
    path('devadmin/deletehometestinomials/<int:id>', views.deletehometestinomials, name='deletehometestinomials'),

    path('devadmin/homewhatwedo/', views.homewhatwedo, name='homewhatwedo'),
    path('devadmin/addhomewhatwedo/', views.addhomewhatwedo, name='addhomewhatwedo'),
    path('devadmin/edithomewhatwedo/<int:id>', views.edithomewhatwedo, name='edithomewhatwedo'),
    path('devadmin/deletehomewhatwedo/<int:id>', views.deletehomewhatwedo, name='deletehomewhatwedo'),

    path('devadmin/homeinfosection/', views.homeinfosection, name='homeinfosection'),
    path('devadmin/aboutinfosection/', views.aboutinfosection, name='aboutinfosection'),



    path('devadmin/abouttestinomials/', views.abouttestinomials, name='abouttestinomials'),
    path('devadmin/addabouttestinomials/', views.addabouttestinomials, name='addabouttestinomials'),
    path('devadmin/editabouttestinomials/<int:id>', views.editabouttestinomials, name='editabouttestinomials'),
    path('devadmin/deleteabouttestinomials/<int:id>', views.deleteabouttestinomials, name='deleteabouttestinomials'),


    path('devadmin/aboutcompanycore/', views.aboutcompanycore, name='aboutcompanycore'),
    path('devadmin/addaboutcompanycore/', views.addaboutcompanycore, name='addaboutcompanycore'),
    path('devadmin/editaboutcompanycore/<int:id>', views.editaboutcompanycore, name='editaboutcompanycore'),
    path('devadmin/deleteaboutcompanycore/<int:id>', views.deleteaboutcompanycore, name='deleteaboutcompanycore'),

    path('devadmin/aboutteammember/', views.aboutteammember, name='aboutteammember'),
    path('devadmin/addaboutteammember/', views.addaboutteammember, name='addaboutteammember'),
    path('devadmin/editaboutteammember/<int:id>', views.editaboutteammember, name='editaboutteammember'),
    path('devadmin/deleteaboutteammember/<int:id>', views.deleteaboutteammember, name='deleteaboutteammember'),


    re_path(r'^validate_username/$', views.validate_username, name='validate_username'),
    
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)