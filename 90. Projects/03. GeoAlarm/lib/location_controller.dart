
import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:geo_alarm/location_service.dart';
import 'package:geo_alarm/screen/home_screen.dart';
import 'package:geocoding/geocoding.dart';
import 'package:geolocator/geolocator.dart';
import 'package:get/get.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:google_maps_webservice/src/places.dart';  // Prediction
import 'package:http/http.dart' as http;

class LocationController extends GetxController{
  bool _loading = false; // 어딘가를 고름
  bool get loading => _loading;

  Placemark _pickPlaceMark = Placemark();
  Placemark get pickPlaceMark => _pickPlaceMark;

  LatLng _pickLatLng = LatLng(37.5233273,126.921252);
  LatLng get pickLatLng => _pickLatLng;

  // 검색시 예상 이름 리스트들
  List<Prediction> _predictionList = [];

  Future<List<Prediction>> searchLocation(BuildContext context, String text) async {
    if(text != null && text.isNotEmpty) {
      http.Response response = await getSearchData(text);
      var data = jsonDecode(response.body.toString());

      if (data['status'] == 'OK') {
        _predictionList = [];
        data['predictions'].forEach((prediction)
        => _predictionList.add(Prediction.fromJson(prediction)));
      } else {
        // ApiChecker.checkApi(response);
      }
    }
    return _predictionList;
  }

  // PlaceMarker 설정
  void setLocation (String placeId, String mainText, String description, GoogleMapController? mapController) async {
    _loading = true;

    _pickPlaceMark = Placemark(name: mainText);

    List<Location> location = await locationFromAddress(description);
    _pickLatLng = LatLng(
      location.last.latitude,
      location.last.longitude,
    );

    update();
  }
}