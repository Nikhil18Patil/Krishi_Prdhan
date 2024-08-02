from rest_framework import serializers
from mydata.models  import mynews

class serializations(serializers.ModelSerializer):
    class Meta:
        model=mynews()
        fields='__all__'