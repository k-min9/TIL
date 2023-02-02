import 'package:android_alarm_manager_plus/android_alarm_manager_plus.dart';
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:flutter_ringtone_player/flutter_ringtone_player.dart';
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

  final Location location = new Location();
  static late LocationData myLocationData;

  static bool isAlarmOn = false;
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

  // 거리 내 원 만들기
  static Set<Circle> _circles = {};
  static double distRadius = 100;
  static Circle circleWithIn = Circle(
      circleId: CircleId('circleWithIn'), // circle간 식별자
      center: targetLatLng,
      fillColor: Colors.red.withOpacity(0.5), // 원 색
      strokeColor: Colors.red, // 테두리 색
      strokeWidth: 1, // 테두리 두께
      radius: distRadius);
  static Circle circleNotWithIn = Circle(
      circleId: CircleId('circleNotWithIn'), // circle간 식별자
      center: targetLatLng,
      fillColor: Colors.blue.withOpacity(0.5), // 원 색
      strokeColor: Colors.blue, // 테두리 색
      strokeWidth: 1, // 테두리 두께
      radius: distRadius);

  // 타겟에 꽂을 마커
  static final Set<Marker> _markers = {};

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
                future: checkPermission(), // 이 함수의 return이 snapshot에 담김
                // future가 변경될때마다 builder가 재실행
                builder: (BuildContext context, AsyncSnapshot snapshot) {
                  // 최초 로딩 중에 원형 로딩 indicator
                  // if (snapshot.connectionState == ConnectionState.waiting) {
                  if (!snapshot.hasData) {
                    return Center(
                      child: CircularProgressIndicator(),
                    );
                  }

                  if (snapshot.data == '위치 권한이 허가 되었습니다.') {
                    return StreamBuilder<LocationData>(
                      stream: location.onLocationChanged, // position 값을 받아 snapshot에 넣음
                      builder: (context, snapshot) {
                        // 범위 안에 있나 체크
                        bool isWithinRange = false;

                        if (snapshot.hasData) {

                          targetLatLng = locationController.pickLatLng;
                          final start = snapshot.data!;
                          final end = targetLatLng;

                          // 맵 컨트롤러로 카메라 위치 이동
                          if (locationController.loading == true){
                            // 마커 만들기
                            if (locationController.ismarked == false){
                              setMarkerOnPos(end);
                              locationController.setIsMakred();
                            }
                            // 선택된 장소가 있음
                            mapController!.animateCamera(
                              CameraUpdate.newLatLngZoom(
                                LatLng(
                                  end.latitude,
                                  end.longitude,
                                ),
                                16
                              ),
                            );
                          } else if (isAlarmOn == false) {
                            // 고른것도 없으면, 일단 현재 위치로
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

                          final distance = Geolocator.distanceBetween(
                            start.latitude!,
                            start.longitude!,
                            end.latitude,
                            end.longitude,
                          );

                          if (distance < distRadius) {
                            isWithinRange = true;
                          }
                          // 원 설정
                          // _circles.clear();
                          // if (isWithinRange == true) {
                          //   _circles = Set.from([circleWithIn]);
                          // } else {
                          //   _circles = Set.from([circleNotWithIn]);
                          // }

                          // 알람이 켜져있으면 발동 (일단 test)
                          // print('alarm');
                          // print(isWithinRange);
                          if (isWithinRange == true && isAlarmOn == true) {
                            isAlarmOn = false;
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
                                // circles: setCircleOnPos(isWithinRange),
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


    // 알람 await 5초마다 확인
    // await AndroidAlarmManager.periodic(
    //     const Duration(seconds: 1),
    //     998,
    //     fireAlarm,
    //     // startAt: DateTime.now(),
    //     allowWhileIdle: true,
    //     wakeup: true);

    return '위치 권한이 허가 되었습니다.';
  }

  // tap 한곳에 마커 추가
  void setMarkerOnPos(LatLng latlang) async {
    setState(() {
      // Position과 마커 갱신
      targetLatLng = latlang;
      _cameraPosition = CameraPosition(
        target: targetLatLng,
        zoom: _zoom, // 카메라 확대 정도
      );
      circleWithIn = Circle(
          circleId: CircleId('circleWithIn'), // circle간 식별자
          center: targetLatLng,
          fillColor: Colors.red.withOpacity(0.5), // 원 색
          strokeColor: Colors.red, // 테두리 색
          strokeWidth: 1, // 테두리 두께
          radius: distRadius);
      circleNotWithIn = Circle(
          circleId: CircleId('circleNotWithIn'), // circle간 식별자
          center: targetLatLng,
          fillColor: Colors.green.withOpacity(0.5), // 원 색
          strokeColor: Colors.blue, // 테두리 색
          strokeWidth: 1, // 테두리 두께
          radius: distRadius);

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
    });

    // 원 갱신
    if (_circles.isNotEmpty) {
      _circles.clear();
    }
    _circles.add(circleWithIn);

    fireAlarm();

    // AndroidAlarmManager.oneShot(Duration(seconds: 3), alarmId, fireAlarm);
  }

  Set<Circle> setCircleOnPos(bool isWithin) {
    // circleWithIn = Circle(
    //     circleId: CircleId('circleWithIn'), // circle간 식별자
    //     center: targetLatLng,
    //     fillColor: Colors.red.withOpacity(0.5), // 원 색
    //     strokeColor: Colors.red, // 테두리 색
    //     strokeWidth: 1, // 테두리 두께
    //     radius: distRadius);
    // circleNotWithIn = Circle(
    //     circleId: CircleId('circleNotWithIn'), // circle간 식별자
    //     center: targetLatLng,
    //     fillColor: Colors.blue.withOpacity(0.5), // 원 색
    //     strokeColor: Colors.blue, // 테두리 색
    //     strokeWidth: 1, // 테두리 두께
    //     radius: distRadius);

    if (isWithin == true) {
      return Set.from([circleWithIn]);
    } else {
      return Set.from([circleNotWithIn]);
    }
  }

  // 구글 맵 생성시 GoogleMapController를 state로 저장
  onMapCreated(GoogleMapController controller) {
    mapController = controller;
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


