import 'dart:convert';
import 'package:geo_alarm/app_constant.dart';
import 'package:http/http.dart' as http;

Future<http.Response> getSearchData(String text) async {
  http.Response response;
  
  response = await http.get(
    // Uri.parse("http://mvs.bslmeiyu.com/api/v1/config/place-api-autocomplete?search_text=$text"),
    Uri.parse("https://maps.googleapis.com/maps/api/place/autocomplete/json?input=${text}&key="+AppConstants.APIKEY2),
    headers: {"Context-Type": "application/json"}
  );

  return response;
}

Future<http.Response> getLocDataFromPlaceId(String placeId) async {
  http.Response response;

  response = await http.get(
    // Uri.parse("http://mvs.bslmeiyu.com/api/v1/config/place-api-autocomplete?search_text=$text"),
      Uri.parse("https://maps.googleapis.com/maps/api/place/details/json?place_id=${placeId}&key="+AppConstants.APIKEY2),
      headers: {"Context-Type": "application/json"}
  );

  return response;
}