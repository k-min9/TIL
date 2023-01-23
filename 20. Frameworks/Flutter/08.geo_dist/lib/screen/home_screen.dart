import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // 구글 맵 컨트롤러 최상단에 생성하고 이벤트 제어
  GoogleMapController? mapController;


  // 카메라 중간위치 : latitude - 위도 , longitude - 경도
  static final LatLng targetLatLng = LatLng(
    37.5233273,
    126.921252,
  );

  static final CameraPosition initialPosition = CameraPosition(
    target: targetLatLng,
    zoom: 15, // 카메라 확대 정도
  );

  // 거리 내 원 만들기
  static final double distRadius = 100;
  static final Circle circleWithIn = Circle(
      circleId: CircleId('circleWithIn'),  // circle간 식별자
      center: targetLatLng,
      fillColor: Colors.red.withOpacity(0.5), // 원 색
      strokeColor: Colors.red, // 테두리 색
      strokeWidth: 1, // 테두리 두께
      radius: distRadius
  );
  static final Circle circleNotWithIn = Circle(
      circleId: CircleId('circleNotWithIn'),  // circle간 식별자
      center: targetLatLng,
      fillColor: Colors.blue.withOpacity(0.5), // 원 색
      strokeColor: Colors.blue, // 테두리 색
      strokeWidth: 1, // 테두리 두께
      radius: distRadius
  );

  // 타겟에 꽂을 마커
  static final Marker targetMarker = Marker(
      markerId: MarkerId('target'),
      position: targetLatLng
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: renderAppBar(),
      // snapshot의 리턴 형태를 generic
      body: FutureBuilder<String>(
        future: checkPermission(), // 이 함수의 return이 snapshot에 담김
        // future가 변경될때마다 builder가 재실행
        builder: (BuildContext context, AsyncSnapshot snapshot) {
          // 로딩 중에 원형 로딩 indicator
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }

          if (snapshot.data == '위치 권한이 허가 되었습니다.') {
            return StreamBuilder<Position>(
              stream: Geolocator.getPositionStream(), // position 값을 받아 snapshot에 넣음
              builder: (context, snapshot) {
                // 범위 안에 있나 체크
                bool isWithinRange = false;

                if (snapshot.hasData) {
                  final start = snapshot.data!;
                  final end = targetLatLng;

                  final distance = Geolocator.distanceBetween(
                    start.latitude,
                    start.longitude,
                    end.latitude,
                    end.longitude,
                  );

                  if (distance < distRadius) {
                    isWithinRange = true;
                  }
                }

                return Column(
                  children: [
                    _CustomGoogleMap(
                      initialPosition: initialPosition,
                      circle: isWithinRange
                              ? circleWithIn
                              : circleNotWithIn,
                      targetMarker: targetMarker,
                      onMapCreated: onMapCreated,
                    ),
                    _MyButton(),
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
    );
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

  // 구글 맵 생성시 GoogleMapController를 state로 저장
  onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  AppBar renderAppBar() {
    return AppBar(
      title: Text(
        'GeoAlarm',
        style: TextStyle(
            color: Colors.blue, fontSize: 26, fontWeight: FontWeight.w900),
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

            final location = await Geolocator.getCurrentPosition();

            // 맵 컨트롤러로 카메라 위치 이동
            mapController!.animateCamera(
              CameraUpdate.newLatLng(
                LatLng(
                  location.latitude,
                  location.longitude,
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
    );
  }
}

class _MyButton extends StatelessWidget {
  const _MyButton({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(child: Text('AAA'));
  }
}

class _CustomGoogleMap extends StatelessWidget {
  final CameraPosition initialPosition;
  final Circle circle;
  final Marker targetMarker;
  final MapCreatedCallback onMapCreated;

  const _CustomGoogleMap({
    required this.initialPosition,
    required this.circle,
    required this.targetMarker,
    required this.onMapCreated,
    Key? key
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      flex: 2,
      child: GoogleMap(
        mapType: MapType.normal,
        initialCameraPosition: initialPosition,
        myLocationEnabled: true,
        myLocationButtonEnabled: true,
        circles: Set.from([circle]),
        markers: Set.from([targetMarker]),
      ),
    );
  }
}
