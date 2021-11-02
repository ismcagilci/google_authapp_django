from django.apps import AppConfig
import requests
import xmltodict


class UserappConfig(AppConfig):
    name = 'userapp'
    def ready(self):
        print("XML file is checking...")
        response = requests.get("https://www.w3schools.com/xml/plant_catalog.xml")
        plant_catalog = xmltodict.parse(response.content)
        all_plants = plant_catalog.get("CATALOG").get("PLANT")
        from .models import plantModel
        change_status = 0
        for plant in all_plants:
            check_plant = plantModel.objects.filter(common = plant.get("COMMON"))
            if len(check_plant) != 0:
                pass
            else:
                plant_model = plantModel(common = plant.get("COMMON"),botanical=plant.get("BOTANICAL"),zone=plant.get("ZONE"),
                ligth=plant.get("LIGHT"),price = plant.get("PRICE"),availability=plant.get("AVAILABILITY"))
                plant_model.save()
                change_status = 1
        if change_status == 1:
            print("There is change in xml file, database is updating...")
        else:
            print("There is no change in xml file")

