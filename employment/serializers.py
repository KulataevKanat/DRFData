from rest_framework import serializers

from employment.models import Employment, Users


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('url', 'id', 'created', 'name', 'surname', 'age')


class CreateEmploymentSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employment
        fields = ('id', 'created', 'name', 'user', 'barcode')


class EmploymentSerializers(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employment
        fields = '__all__'
