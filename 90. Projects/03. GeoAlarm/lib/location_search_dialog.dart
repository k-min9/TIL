import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:geo_alarm/location_controller.dart';
import 'package:geo_alarm/screen/home_screen.dart';
import 'package:get/get.dart';
import 'package:flutter_typeahead/flutter_typeahead.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:google_maps_webservice/places.dart';

class LocationSearchDialog extends StatelessWidget {
  final GoogleMapController? mapController;
  const LocationSearchDialog({required this.mapController});

  @override
  Widget build(BuildContext context) {
    final TextEditingController _controller = TextEditingController();

    return Container(
      margin: EdgeInsets.only(top : 20),
      padding: EdgeInsets.all(5),
      alignment: Alignment.topCenter,
      child: Material(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
        child: SizedBox(width: 350, child: TypeAheadField(
          textFieldConfiguration: TextFieldConfiguration(
            controller: _controller,
            textInputAction: TextInputAction.search,
            autofocus: true,
            textCapitalization: TextCapitalization.words,
            keyboardType: TextInputType.streetAddress,
            decoration: InputDecoration(
              hintText: 'search_location',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: BorderSide(style: BorderStyle.none, width: 0),
              ),
              hintStyle: Theme.of(context).textTheme.headline2?.copyWith(
                fontSize: 16, color: Theme.of(context).disabledColor,
              ),
              filled: true, fillColor: Theme.of(context).cardColor,
            ),
            style: Theme.of(context).textTheme.headline2?.copyWith(
              color: Theme.of(context).textTheme.bodyText1?.color, fontSize: 20,
            ),
          ),
          suggestionsCallback: (pattern) async {
            return await Get.find<LocationController>().searchLocation(context, pattern);
          },
          itemBuilder: (context, Prediction suggestion) {
            return Padding(
              padding: EdgeInsets.all(10),
              child: Row(children: [
                Icon(Icons.location_on),
                // 검색 내용
                Expanded(
                  child: Text(suggestion.structuredFormatting!.mainText,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: Theme.of(context).textTheme.headline2?.copyWith(
                    color: Theme.of(context).textTheme.bodyText1?.color, fontSize: 20,
                  )),
                ),
              ]),
            );
          },
          onSuggestionSelected: (Prediction suggestion) {
            // print("여기 고름 : "+suggestion.structuredFormatting!.mainText);
            print("여기 고름 : "+suggestion.placeId!);
            print(suggestion.toJson().toString());
            print(suggestion.structuredFormatting!.toJson().toString());
            print(suggestion.terms[0]!.toJson().toString());
            Get.find<LocationController>().setLocation(suggestion.placeId!, suggestion.structuredFormatting!.mainText, suggestion.description!, mapController);
            Get.back();
          },
        )),
      ),
    );
  }
}