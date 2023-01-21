import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class HomeScreen extends StatelessWidget {
  WebViewController? controller;
  final homeUrl = 'https://github.com/k-min9/TIL';

  HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text('TIL K-Min9'),
        centerTitle: true,
        actions: [
          // 자주 쓸 예정
          IconButton(
            onPressed: () {
              // http://
              // https://
              if(controller == null){
                return;
              }

              controller!.loadUrl(homeUrl);
            },
            icon: Icon(
              Icons.home,
            ),
          ),
        ],
      ),
      body: WebView(
        onWebViewCreated: (WebViewController controller) {
          this.controller = controller;
        },
        initialUrl: homeUrl,
        javascriptMode: JavascriptMode.unrestricted,  // javascript 쓰기
      ),
    );
  }
}
