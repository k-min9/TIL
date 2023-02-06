
import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:geo_alarm/location_service.dart';
import 'package:geocoding/geocoding.dart';
import 'package:get/get.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:google_maps_webservice/src/places.dart';  // Prediction
import 'package:http/http.dart' as http;

class LocationController extends GetxController{
  bool _isSearched = false; // 검색으로 타겟 선정 후 flag로 사용하여 homeController 쪽에서 마커 세팅
  bool get isSearched => _isSearched;

  bool _ismarked = false;  // 탭으로 타겟 선정
  bool get ismarked => _ismarked;

  bool _shouldCameraMove = true; // 검색 또는 마킹으로 인한 카메라 이동 필요. true면 초기위치도 잡아줌
  bool get shouldCameraMove => _shouldCameraMove;

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
    _shouldCameraMove = true;
    _isSearched = true;
    _ismarked = false;

    _pickPlaceMark = Placemark(name: mainText);

    List<Location> location = await locationFromAddress(description);
    _pickLatLng = LatLng(
      location.last.latitude,
      location.last.longitude,
    );
    update();
  }

  // 마킹 완료 후 flag 끄고 보고
  void setIsMakred () {
    _isSearched = false;
    _ismarked = true;
  }

  void setInitialize() {
    _isSearched = false;
    _ismarked = false;
    _shouldCameraMove = true;
    _pickPlaceMark = Placemark();
  }

  // 카메라 초기 설정
  void setShouldCameraMove (bool value) {
    _shouldCameraMove = value;
  }

  // 화면 갱신
  void updateMap() {
    update();
  }

}