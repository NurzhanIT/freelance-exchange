from rest_framework import serializers

from marketplace.models import Executor


class ExecutorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = "__all__"

    # def create(self, validated_data):
    #     user = self.context['user']
    #     print(user, 'sssuser')
    #     return Executor.objects.create(user=user, **validated_data)


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = "__all__"
