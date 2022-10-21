import java.lang.reflect.Type;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.google.gson.reflect.TypeToken;

/**
 * Dynamic Json without DTO
 * DTO 없이 Json -> Gson 순으로 Parsing하고 내용물 꺼내기
 * 출처 : <https://ashishontech.xyz/read-dynamic-object-from-json-using-gson/>
 * 
 * 대상 JSON
 {
    "Sample_01": {
        "class": "Tenant",
        "A1": {
            "class": "Application",
            "template": "http",
            "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [
                    "10.0.1.10"
                ],
                "pool": "web_poolddd"
            },
            "web_poolddd": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                        "servicePort": 80,
                        "serverAddresses": [
                            "192.0.13.10",
                            "192.0.14.11"
                        ]
                    }
                ]
            }
        }
    },
    "Sample_20": {
        "class": "Tenant",
        "A1": {
            "class": "Application",
            "template": "http",
            "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [
                    "10.2.2.2"
                ],
                "pool": "web_pool_data"
            },
            "web_pool_data": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                        "servicePort": 80,
                        "serverAddresses": [
                            "192.0.10.10",
                            "192.0.10.11"
                        ]
                    }
                ]
            }
        }
    }
}
 */
public class DynamicJsonwithoutDTO {

  public static void main(String[] args) {
        
    String json = "{\"Sample_01\":{\"class\":\"Tenant\",\"A1\":{\"class\":\"Application\",\"template\":\"http\",\"serviceMain\":{\"class\":\"Service_HTTP\",\"virtualAddresses\":[\"10.0.1.10\"],\"pool\":\"web_poolddd\"},\"web_poolddd\":{\"class\":\"Pool\",\"monitors\":[\"http\"],\"members\":[{\"servicePort\":80,\"serverAddresses\":[\"192.0.13.10\",\"192.0.14.11\"]}]}}},\"Sample_20\":{\"class\":\"Tenant\",\"A1\":{\"class\":\"Application\",\"template\":\"http\",\"serviceMain\":{\"class\":\"Service_HTTP\",\"virtualAddresses\":[\"10.2.2.2\"],\"pool\":\"web_pool_data\"},\"web_pool_data\":{\"class\":\"Pool\",\"monitors\":[\"http\"],\"members\":[{\"servicePort\":80,\"serverAddresses\":[\"192.0.10.10\",\"192.0.10.11\"]}]}}}}";
    
    Type listType = new TypeToken<Map<String, Object>>(){}.getType();
    Gson gson = new Gson();
    Map<String,Object> myList = gson.fromJson(json, listType);

    JsonParser parser = new JsonParser();

    for (Map.Entry<String,Object> m : myList.entrySet())
    {
        System.out.println("==============");
        if(m.getValue() instanceof String){
			// get String value
        }else{ // if value is an Object
            
			System.out.println("VIP Sec: Name: "+m.getKey());
            Map<String,Object> myList1 = gson.fromJson(m.getValue().toString(), listType);
            for (Map.Entry<String,Object> m1 : myList1.entrySet())
            {
                if(!( m1.getValue() instanceof String)){
                    Map<String,Object> myList2 = gson.fromJson(m1.getValue().toString(), listType);
                    for (Map.Entry<String,Object> m2 : myList2.entrySet())
                    {
                         if(!( m2.getValue() instanceof String)){
                            Map<String,Object> myList3 = gson.fromJson(m2.getValue().toString(), listType);
                            for (Map.Entry<String,Object> m3 : myList3.entrySet())
                            {
                                if(m3.getKey().equals("virtualAddresses")){
                                    System.out.println("VIP Sec: IP Address: "+m3.getValue());
                                }
                                else if(m3.getKey().equals("pool")){
                                    System.out.println("Pool Sec: Name: "+m3.getValue());
                                }else if(m3.getKey().equals("monitors")){
                                    JsonArray monitors = parser.parse(m3.getValue().toString()).getAsJsonArray();
                                    int count = 0;
                                    while(count < monitors.size()){
                                        String monitor = monitors.get(count).getAsString();
                                        System.out.println("Monitor: "+monitor);
                                        count++;
                                    }
                                }else if(m3.getKey().equals("members")){
                                    JsonArray members = parser.parse(m3.getValue().toString()).getAsJsonArray();
                                    int count = 0;
                                    while(count < members.size()){
										                    // Parsing as Object to key values by key directly
                                        JsonObject mem = members.get(count).getAsJsonObject();
                                        String port = mem.get("servicePort").getAsString();
                                        System.out.println("Port: "+port);
                                        JsonElement ipAddrs = mem.get("serverAddresses");
                                        if(ipAddrs.isJsonArray()){
                                            JsonArray ips = ipAddrs.getAsJsonArray();
                                            int c = 0;
                                            while(c < ips.size()){
                                                String ip = ips.get(c).getAsString();
                                                System.out.println("IP: "+ip);
                                                c++;
                                            }
                                        }
                                        count++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
  }
}
