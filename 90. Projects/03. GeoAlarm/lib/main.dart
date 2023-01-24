import 'package:flutter/material.dart';
import 'package:geo_alarm/location_controller.dart';
import 'package:geo_alarm/screen/home_screen.dart';
import 'package:get/get.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    Get.put(LocationController());
    return const GetMaterialApp(
        debugShowCheckedModeBanner: false,
        home: HomeScreen()
    );
  }
}
