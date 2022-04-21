from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Out
from .serializers import OutSerializer
from .data.algo import get_related_adj
from .data.algo import get_related_edge

import json

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/el/',
            'method': 'GET',
            'body': None,
            'description': 'Returns el timer and data'
        },
                {
            'Endpoint': '/al/',
            'method': 'GET',
            'body': None,
            'description': 'Returns al timer and data'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getOut(request):
    out = Out.objects.all()
    serializer = OutSerializer(out,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOut(request,_ctry, _city, _state, _mfr_, _make, _type_):
    obj = (get_related_adj(ctry=_ctry, city=_city, state=_state, mfr_=_mfr_, make=_make, type_=_type_))
    return Response(json.dumps(obj,indent=3,sort_keys=True))

@api_view(['GET'])
def getOut2(request,_ctry, _city, _state, _mfr_, _make, _type_):
    obj = (get_related_edge(ctry=_ctry, city=_city, state=_state, mfr_=_mfr_, make=_make, type_=_type_))
    return Response(json.dumps(obj,indent=3,sort_keys=True))

#JAPAN TSUTSUMI AICHI TOYOTA MOTOR CORPORATION TOYOTA PASSENGER CAR
#pprint(get_related(ctry=pctry, state=pstate, city=pcity, mfr_=pmfr, make=pmake, type=ptype))
