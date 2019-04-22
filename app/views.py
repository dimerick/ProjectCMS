from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Group
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.db import connection #para ejecutar RAW queries

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at ElAtlas App.")


def update_location_groups(request):
	grupos = Group.objects.all()
	for grupo in grupos:
		wkt = 'POINT(' + grupo.lon + ' ' + grupo.lat + ')'
		grupo.location = GEOSGeometry(wkt, srid=4326)
		grupo.save()
	return HttpResponse("Se ha actualizado la ubicacion de los grupos exitosamente")

def groups(request):
	grupos = Group.objects.all().order_by('name').filter(is_active=True)
	fc = {"type":"FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": []}
	for grupo in grupos:
		image = None
		if grupo.image != None:
			image = grupo.image.url
		#s.point.transform(3116)
		coords = (grupo.location.coords[0], grupo.location.coords[1])
		f = {"type": "Feature", "geometry": {"type": "Point", "coordinates": coords}, "properties": {"name": grupo.name, "email": grupo.email, "description": grupo.description, "image": image}}
		fc['features'].append(f)
	return JsonResponse(fc, safe=False)