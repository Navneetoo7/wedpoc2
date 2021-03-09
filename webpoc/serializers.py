from django.db.models import fields
from rest_framework  import serializers
from .models import Login, Customer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        #fields = ['transaction_id', 'transdate', 'cfname', 'clname', 'country', 'ccity', 'ptype', 'product', 'qty', 'amount']


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email_id', 'password')