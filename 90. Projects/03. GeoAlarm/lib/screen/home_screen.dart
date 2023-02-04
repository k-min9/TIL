import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:geo_alarm/location_controller.dart';
import 'package:geo_alarm/location_search_dialog.dart';
import 'package:geolocator/geolocator.dart';
import 'package:get/get.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:location/location.dart';
import 'package:vibration/vibration.dart';
import 'package:geo_alarm/main.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // 구글 맵 컨트롤러 최상단에 생성하고 이벤트 제어
  GoogleMapController? mapController;
  LocationController? locationController;

  final Location location = new Location();
  static late LocationData myLocationData;

  static bool isAlarmOn = false;
  static bool isAlarmStateChanged = false; // 갱신 flag 용
  static int alarmId = 1;

  // 카메라 중간위치 : latitude - 위도 , longitude - 경도
  static LatLng targetLatLng = LatLng(
    37.5233273,
    126.921252,
  );
  static double _zoom = 15;
  static CameraPosition _cameraPosition = CameraPosition(
    target: targetLatLng,
    zoom: _zoom, // 카메라 확대 정도
  );

  // 구글 맵 상수
  static double distRadius = 100;
  static final Set<Circle> _circles = {}; // 원
  static final Set<Marker> _markers = {}; // 마커

  @override
  Widget build(BuildContext context) {
    return GetBuilder<LocationController>(builder: (locationController) {
      return Scaffold(
          appBar: AppBar(
            title: Text(
              'GeoAlarm',
              style: TextStyle(
                  color: Colors.blue,
                  fontSize: 26,
                  fontWeight: FontWeight.w900),
              textAlign: TextAlign.center,
            ),
            backgroundColor: Colors.white,
            actions: [
              IconButton(
                onPressed: () async {
                  // 아직 구글 맵 생성 안 됨
                  if (mapController == null) {
                    return;
                  }

                  // 초기 세팅
                  myLocationData = await location.getLocation();

                  // 맵 컨트롤러로 카메라 위치 이동
                  mapController!.animateCamera(
                    CameraUpdate.newLatLng(
                      LatLng(
                          myLocationData.latitude!,
                          myLocationData.longitude!
                      ),
                    ),
                  );
                },
                color: Colors.blue,
                icon: Icon(
                  Icons.my_location,
                ),
              ),
            ],
          ),
          // snapshot의 리턴 형태를 generic
          body: Stack(
            children: [
              FutureBuilder<String>(
                future: checkPermission(), // 이 함수의 return이 snapshot에 담김 $$$ location은??
                // future가 변경될때마다 builder가 재실행
                builder: (BuildContext context, AsyncSnapshot snapshot) {
                  // 최초 로딩 중에 원형 로딩 indicator
                  if (!snapshot.hasData) {
                    return Center(
                      child: CircularProgressIndicator(),
                    );
                  }

                  if (snapshot.data == '위치 권한이 허가 되었습니다.') {
                    setLocationController(locationController);
                    return StreamBuilder<LocationData>(
                      stream: location.onLocationChanged, // position 값을 받아 snapshot에 넣음
                      builder: (context, snapshot) {
                        WidgetsBinding.instance.addPostFrameCallback((_) => onAfterStreamBuild(context)); // StreamBuilder 중 setState관련 문제 해결 
                        // 범위 안에 있나 체크
                        bool isWithinRange = false;

                        if (snapshot.hasData) {

                          // 검색으로 타겟을 잡은 경우, 타겟 지점 갱신
                          if(locationController.isSearched == true) {
                            targetLatLng = locationController.pickLatLng;
                            // setMarkerOnPos(targetLatLng);
                          }

                          final start = snapshot.data!; // 내 위치
                          final end = targetLatLng; // 타겟 장소

                          // 알람이 켜져있을때 (나와 대상의 위치를 같이 보여주거나, 처음시작점과 대상의 위치를 같이 보여줌)
                          if (isAlarmOn == true) {

                          // 알람이 꺼져있을때
                          } else {
                            // 검색이나 마킹한 대상이 있으면 타겟을 보여줌
                            if (locationController.isSearched == true || locationController.ismarked == true) {
                              mapController!.animateCamera(
                                CameraUpdate.newLatLngZoom(
                                    LatLng(
                                      end.latitude,
                                      end.longitude,
                                    ),
                                    16
                                ),
                              );
                            // 없으면 현재 위치(자신)을 보여줌
                            } else {
                              mapController?.animateCamera(
                                CameraUpdate.newLatLngZoom(
                                    LatLng(
                                      start.latitude!,
                                      start.longitude!,
                                    ),
                                    16
                                ),
                              );
                            }
                          }

                          final distance = Geolocator.distanceBetween(
                            start.latitude!,
                            start.longitude!,
                            end.latitude,
                            end.longitude,
                          );


                          if (distance < distRadius) {
                            isWithinRange = true;
                          }

                          // 알람이 켜져있으면 발동 (일단 test)
                          if (isWithinRange == true && isAlarmOn == true) {
                            isAlarmOn = false;
                            _circles.clear();
                            _circles.add(Circle(
                                circleId: CircleId('circleNormal'),
                                // circle간 식별자
                                center: targetLatLng,
                                fillColor: Colors.blue.withOpacity(0.5), // 원 색
                                strokeColor: Colors.blue, // 테두리 색
                                strokeWidth: 1,
                                // 테두리 두께
                                radius: distRadius));
                            fireAlarm();
                          }
                        }

                        return Column(
                          children: [
                            Expanded(
                              flex: 2,
                              child: GoogleMap(
                                mapType: MapType.normal,
                                initialCameraPosition: _cameraPosition,
                                myLocationEnabled: true,
                                myLocationButtonEnabled: true,
                                circles: _circles,
                                markers: _markers,
                                onMapCreated: onMapCreated,
                                onTap: setMarkerOnPos, // 지도 선택시 마커 변경
                                // targetLatLng: targetLatLng,
                              ),
                            ),
                            // 버튼 입력
                            Expanded(
                                child: Switch(
                                  value: isAlarmOn,
                                  onChanged: (value) {
                                    setState(() {
                                      isAlarmOn = value;
                                      isAlarmStateChanged = true; // flag
                                    });
                                  },
                                )
                            ),
                          ],
                        );
                      },
                    );
                  }

                  return Center(
                    child: Text(snapshot.data),
                  );
                },
              ),
              Positioned(
                  top: 0,
                  left: 10,
                  right: 20,
                  child: GestureDetector(
                      onTap: () {
                        Vibration.vibrate();
                        Get.dialog(
                            LocationSearchDialog(mapController: mapController));
                      },
                      child: Container(
                          height: 50,
                          padding: EdgeInsets.symmetric(horizontal: 5),
                          decoration: BoxDecoration(
                              color: Theme.of(context).cardColor,
                              borderRadius: BorderRadius.circular(10)),
                          child: Row(
                            children: [
                              Icon(Icons.location_on,
                                  size: 25,
                                  color: Theme.of(context).primaryColor),
                              SizedBox(width: 5),
                              Expanded(
                                child: Text(
                                  '${locationController.pickPlaceMark.name ?? ''} '
                                  '${locationController.pickPlaceMark.locality ?? ''} '
                                  '${locationController.pickPlaceMark.postalCode ?? ''} '
                                  '${locationController.pickPlaceMark.country ?? ''}',
                                  style: TextStyle(fontSize: 20),
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ),
                              SizedBox(width: 10),
                              Icon(Icons.search,
                                  size: 25,
                                  color: Theme.of(context)
                                      .textTheme
                                      .bodyText1!
                                      .color)
                            ],
                          )))),
            ],
          ));
    });
  }

  // StreamBuild의 setState관련
  void onAfterStreamBuild(BuildContext context) {
    // locationController의 검색 갱신을 여기서 확인
    if(locationController?.isSearched == true) {
      setMarkerOnPos(targetLatLng);
    // 알람 관련 체크 : 원 갱신
    } else if(isAlarmStateChanged == true) {
      isAlarmStateChanged = false;
      if (_circles.isNotEmpty) {
        _circles.clear();
      }

      // 알람 켜져있으면 붉게
      if (isAlarmOn == true) {
        _circles.add(Circle(
            circleId: CircleId('circleAlarm'), // circle간 식별자
            center: targetLatLng,
            fillColor: Colors.red.withOpacity(0.5), // 원 색
            strokeColor: Colors.red, // 테두리 색
            strokeWidth: 1, // 테두리 두께
            radius: distRadius));
      } else {
        _circles.add(Circle(
            circleId: CircleId('circleNormal'),
            // circle간 식별자
            center: targetLatLng,
            fillColor: Colors.blue.withOpacity(0.5), // 원 색
            strokeColor: Colors.blue, // 테두리 색
            strokeWidth: 1,
            // 테두리 두께
            radius: distRadius));
      }
      locationController?.updateMap();
    }
  }

  // 권한 관련은 다 여기서 작업. always일때는 background에서도 동작
  Future<String> checkPermission() async {
    final isLocationEnabled = await Geolocator.isLocationServiceEnabled();

    if (!isLocationEnabled) {
      return '위치 서비스를 활성화 해주세요.';
    }

    LocationPermission checkedPermission = await Geolocator.checkPermission();

    if (checkedPermission == LocationPermission.denied) {
      checkedPermission = await Geolocator.requestPermission();

      if (checkedPermission == LocationPermission.denied) {
        return '위치 권한을 허가해주세요.';
      }
    }

    // 영원히 앱에서 요청을 허가할 수 없음. 직접 세팅에서 해야 함
    if (checkedPermission == LocationPermission.deniedForever) {
      return '앱의 위치 권한을 세팅에서 허가해주세요.';
    }

    return '위치 권한이 허가 되었습니다.';
  }

  // tap 한곳에 마커 추가. setState 관련 삭제
  void setMarkerOnPos(LatLng latlang) async {
    targetLatLng = latlang;
    // 마킹 되었다고 체크
    locationController?.setIsMakred();

    // 마커 갱신
    if (_markers.isNotEmpty) {
      _markers.clear();
    }
    _markers.add(Marker(
      draggable: true,
      markerId: MarkerId('target'),
      position: latlang,
      infoWindow: InfoWindow(
        title: '타겟',
        snippet: '스니펫',
      ),
      icon: BitmapDescriptor.defaultMarker,
    ));

    // 원 갱신
    if (_circles.isNotEmpty) {
      _circles.clear();
    }

    // 알람 켜져있으면 붉게
    if (isAlarmOn == true) {
      _circles.add(Circle(
          circleId: CircleId('circleAlarm'), // circle간 식별자
          center: targetLatLng,
          fillColor: Colors.red.withOpacity(0.5), // 원 색
          strokeColor: Colors.red, // 테두리 색
          strokeWidth: 1, // 테두리 두께
          radius: distRadius));
    } else {
      _circles.add(Circle(
          circleId: CircleId('circleNormal'),
          // circle간 식별자
          center: targetLatLng,
          fillColor: Colors.blue.withOpacity(0.5), // 원 색
          strokeColor: Colors.blue, // 테두리 색
          strokeWidth: 1,
          // 테두리 두께
          radius: distRadius));
    }
    locationController?.updateMap();
  }
  
  // 구글 맵 생성시 GoogleMapController를 state로 저장
  onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }
  
  // locationController 세팅
  setLocationController(LocationController controller) {
    locationController = controller;
  }

  void fireAlarm() async {
    print('Test Fired');

    var androidPlatformChannelSpecifics = AndroidNotificationDetails(
      'alarm_notif',
      'alarm_notif',
      channelDescription: 'Channel for Alarm notification',
      icon: 'logo',
      // sound: RawResourceAndroidNotificationSound('bgm1'),
      largeIcon: DrawableResourceAndroidBitmap('logo'),
    );

    var platformChannelSpecifics = NotificationDetails(
        android: androidPlatformChannelSpecifics
    );

    await flutterLocalNotificationsPlugin.show(0, 'title', 'body', platformChannelSpecifics);

  }
}