"""TensorMSA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
Multi Relational service (not need for now )
    ex: #url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
"""
from django.conf.urls import url
from django.contrib import admin
from tfmsarest import views as rest_view
from tfmsaview import views as ui_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', csrf_exempt(admin.site.urls)),
    # network info
    url(r'^api/v1/type/common/nninfo/(?P<nnid>.*)/category/(?P<cate>.*)/subcate/(?P<sub>.*)/',
        csrf_exempt(rest_view.CommonNetInfo.as_view())),
    url(r'^api/v1/type/common/nninfo/$',
        csrf_exempt(rest_view.CommonNetInfo.as_view())),

    # pre process for dataframe data
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/(?P<tb>.*)/pre/(?P<nnid>.*)/',
        csrf_exempt(rest_view.DataFramePre.as_view())),

    #data upload, search
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/(?P<tb>.*)/data/(?P<args>.*)/',
        csrf_exempt(rest_view.DataFrameData.as_view())),
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/(?P<tb>.*)/data/',
        csrf_exempt(rest_view.DataFrameData.as_view())),

    #manage column data types
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/(?P<tb>.*)/format/(?P<nnid>.*)/',
        csrf_exempt(rest_view.DataFrameFormat.as_view())),

    #manage table
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/(?P<tb>.*)/',
        csrf_exempt(rest_view.DataFrameTable.as_view())),
    url(r'^api/v1/type/dataframe/base/(?P<baseid>.*)/table/',
        csrf_exempt(rest_view.DataFrameTable.as_view())),

    #manage data frame
    url(r'^api/v1/type/dataframe/base/(?P<baseid>\w+:?(?=/))/',
        csrf_exempt(rest_view.DataFrameSchema.as_view())),
    url(r'^api/v1/type/dataframe/base/',
        csrf_exempt(rest_view.DataFrameSchema.as_view())),

    # CNN config data manage
     url(r'^api/v1/type/cnn/conf/(?P<nnid>.*)/',
         csrf_exempt(rest_view.ConvNeuralNetConfig.as_view())),

    # CNN training
     url(r'^api/v1/type/cnn/train/(?P<nnid>.*)/',
         csrf_exempt(rest_view.ConvNeuralNetTrain.as_view())),

    # CNN predict
     url(r'^api/v1/type/cnn/predict/(?P<nnid>.*)/',
         csrf_exempt(rest_view.ConvNeuralNetPredict.as_view())),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)