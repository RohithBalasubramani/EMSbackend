from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("PEPPL_DATA.urls")),
    path("mod1/", include("MOD_SEC_1.urls")),
    path("anomaly/", include("Anomalydb.urls")),
    path("pcc1/", include("PCC_SEC_1.urls")),
    path("cell1/", include("CELL_SEC_1.urls")),
]
