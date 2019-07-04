from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(["POST"])
if (!$(“input”).val()) {
search = “jaws”;
} else {
search = $(“input”).val();
$(“input”).val(“”);
    }

const api = “&api_key=feb6f0eeaa0a72662967d77079850353”;
const endpoint = "https://api.themoviedb.org/3/search/movie?query=${search}${api}";
const poster = “https://image.tmdb.org/t/p/w600/";

$.getJSON(endpoint, function(data) {
}

let index = $(“li”).index(this);
let selected = data.results[index];

if (data.results.length == 0) {
 $(“.error”).html(“No data found, search again.”);
 }

