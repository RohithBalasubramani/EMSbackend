from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from django.apps import apps
from rest_framework import viewsets, filters
import pandas as pd
from django.core.cache import cache
from django.utils.dateparse import parse_datetime

class CustomDateTimeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_date_time = request.query_params.get("start_date_time")
        end_date_time = request.query_params.get("end_date_time")
        resample_period = request.query_params.get("resample_period")

        if start_date_time and end_date_time:
            start_date_time = parse_datetime(start_date_time)
            end_date_time = parse_datetime(end_date_time)
            if start_date_time and end_date_time:
                queryset = queryset.filter(date_time__range=(start_date_time, end_date_time))
                print(f"Queryset filtered for date range: {start_date_time} to {end_date_time}")

        if resample_period:
            queryset = view.resample_data(queryset, resample_period, start_date_time, end_date_time)

        return queryset

class CustomPagination(PageNumberPagination):
    page_size = 2000
    page_size_query_param = "page_size"
    max_page_size = None

app_models = apps.get_app_config("PCC_SEC_1").get_models()

for model in app_models:
    class_name = f"{model.__name__}ViewSet"
    queryset = model.objects.order_by("-date_time")
    serializer_class = globals()[f"{model.__name__}Serializer"]

    class DynamicViewSet(ReadOnlyModelViewSet):
        queryset = queryset
        serializer_class = serializer_class
        pagination_class = CustomPagination
        filter_backends = [CustomDateTimeFilter]

        def get_object(self):
            queryset = self.get_queryset()
            pk = self.kwargs.get("pk")
            return get_object_or_404(queryset, pk=pk)

        def resample_data(self, queryset, resample_period, start, end):
            cache_key = f"resampled_{resample_period}_{start}_{end}"
            cached_data = cache.get(cache_key)
            if cached_data:
                print(f"Using cached data for key: {cache_key}")
                return cached_data

            # Convert queryset to DataFrame
            df = pd.DataFrame(list(queryset.values()))
            if df.empty:
                print("Dataframe is empty after query.")
                return queryset

            df['date_time'] = pd.to_datetime(df['date_time'])
            df.set_index('date_time', inplace=True)

            # Resample the DataFrame
            resampled_df = df.resample(resample_period).sum()
            resampled_df.reset_index(inplace=True)

            resampled_queryset = [dict(row) for _, row in resampled_df.iterrows()]
            cache.set(cache_key, resampled_queryset, timeout=None)
            print(f"Data resampled and cached for key: {cache_key}")

            return resampled_queryset

    locals()[class_name] = DynamicViewSet
