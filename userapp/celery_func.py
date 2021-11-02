from celery import shared_task
import requests
import xmltodict
from .models import plantModel
from django.contrib.auth.models import User
from django.core.mail import send_mail


@shared_task
def check_xml_file(file_adress,username):
    response = requests.get(file_adress)
    user = User.objects.get(username=username)
    try:
        plant_catalog = xmltodict.parse(response.content)
        all_plants = plant_catalog.get("CATALOG").get("PLANT")
        for plant in all_plants:
            plant_model = plantModel(common = plant.get("COMMON"),botanical=plant.get("BOTANICAL"),zone=plant.get("ZONE"),
            ligth=plant.get("LIGHT"),price = plant.get("PRICE"),availability=plant.get("AVAILABILITY"))
            plant_model.save()
        plants = plantModel.objects.filter(zone = "Annual")
        for plant in plants:
            plant.zone = "new_zone"
            plant.save()
        send_mail("These words was changed", "Hi i changed "+str(len(plants))+" fields word 'Annual' changed with word 'new_zone'", "37usta37@gmail.com", [user.email])
    except:
        send_mail("xml_file_error","there is a error xml file you sent","37usta37@gmail.com",[user.email]) 
   

