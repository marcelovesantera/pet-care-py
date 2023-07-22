from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import SexChoices
from .models import Pet
from groups.models import Group
from traits.models import Trait
from django.forms.models import model_to_dict
import ipdb


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexChoices.choices,
        default=SexChoices.DEFAULT,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    traits_count = serializers.SerializerMethodField()

    def get_traits_count(self, obj):
        return obj.traits.count()

    def create(self, validated_data: dict) -> Pet:
        group_dict = validated_data.pop("group")
        traits_list = validated_data.pop("traits")

        group_obj = Group.objects.get_or_create(**group_dict)[0]
        pet_obj = Pet.objects.create(**validated_data, group=group_obj)

        for trait_dict in traits_list:
            trait_obj = Trait.objects.get_or_create(**trait_dict)[0]
            pet_obj.traits.add(trait_obj)

        return pet_obj

    def update(self, instance, validated_data: dict):
        group_dict = validated_data.pop("group", None)
        traits_list = validated_data.pop("traits", None)

        if group_dict:
            group_obj = Group.objects.get_or_create(**group_dict)[0]
            instance.group = group_obj

        if traits_list:
            instance.traits.clear()

            for trait_dict in traits_list:
                trait_obj = Trait.objects.get_or_create(**trait_dict)[0]
                instance.traits.add(trait_obj)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
