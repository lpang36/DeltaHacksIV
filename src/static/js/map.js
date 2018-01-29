
      // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.
      var map;
      var pos, pos2;
      function initMap() {
        map = new google.maps.Map(document.getElementById('googleMap'), {
                    zoom: 12,
          center: {lat: 37.7749, lng: -122.4194}
            });

        // Create the search box and link it to the UI element.
       var input = document.getElementById('from');
       var searchBox = new google.maps.places.SearchBox(input);
       var input2 = document.getElementById('to');
       var searchBox2 = new google.maps.places.SearchBox(input2);
       //map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

       // Bias the SearchBox results towards current map's viewport.
       map.addListener('bounds_changed', function() {
         searchBox.setBounds(map.getBounds());
         searchBox2.setBounds(map.getBounds());
       });

       var markers = [];
       // Listen for the event fired when the user selects a prediction and retrieve
       // more details for that place.
       searchBox.addListener('places_changed', function() {
           if (document.getElementById('from').value==='') {
              if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
             pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            var marker = new google.maps.Marker({position:pos});
            marker.setMap(map);
            map.setCenter(pos);
            marker.addListener('click', function() {

            });
          });
           }
           }
           else {
             var places = searchBox.getPlaces();

             if (places.length == 0) {
               return;
             }

             // Clear out the old markers.
             markers.forEach(function(marker) {
               marker.setMap(null);
             });
             markers = [];

             // For each place, get the icon, name and location.
             var bounds = new google.maps.LatLngBounds();
             places.forEach(function(place) {
               if (!place.geometry) {
                 console.log("Returned place contains no geometry");
                 return;
               }



               // Create a marker for each place.
               markers.push(new google.maps.Marker({
                 map: map,
                 //icon: icon,
                 title: place.name,
                 position: place.geometry.location
               }));


               if (place.geometry.viewport) {
                 // Only geocodes have viewport.
                 bounds.union(place.geometry.viewport);
                  pos = place.geometry.location;
               } else {
                 bounds.extend(place.geometry.location);
                  pos = place.geometry.location;
               }
             });
                                       pos = places[0].geometry.location;
           map.fitBounds(bounds);
           }
           });
           
         searchBox2.addListener('places_changed', function() {
           var places = searchBox2.getPlaces();

           if (places.length == 0) {
             return;
           }

           // Clear out the old markers.
           markers.forEach(function(marker) {
             marker.setMap(null);
           });
           markers = [];

           // For each place, get the icon, name and location.
           var bounds = new google.maps.LatLngBounds();
           places.forEach(function(place) {
             if (!place.geometry) {
               console.log("Returned place contains no geometry");
               return;
             }



             // Create a marker for each place.
             markers.push(new google.maps.Marker({
               map: map,
               //icon: icon,
               title: place.name,
               position: place.geometry.location
             }));


             if (place.geometry.viewport) {
               // Only geocodes have viewport.
               bounds.union(place.geometry.viewport);
                pos2 = place.geometry.location;
             } else {
               bounds.extend(place.geometry.location);
                pos2 = place.geometry.location;
             }
                        pos2 = places[0].geometry.location;
           map.fitBounds(bounds);
           });

           //pass in 2d array of coordinates from python backend, call it coords
           calculateAndDisplayRoute(pos,pos2,pos.lat(),pos.lng(),pos2.lat(),pos2.lng());
         });
             
        /*
        // map.fitBounds(bounds);


         //pass in 2d array of coordinates from python backend, call it coords

         var xmlhttp = new XMLHttpRequest();
         var myArr;
         xmlhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            myArr = JSON.parse(this.responseText);
            document.getElementById("demo").innerHTML = myArr[0];
            window.alert(myArr[1]);
          }
        };
        xmlhttp.open("GET", "json_file.txt", true);
        xmlhttp.send();
        calculateAndDisplayRoute(directionsService, directionsDisplay, myArr);
>>>>>>> 079bed039a534e2b86bcea88b5f89253bea65a16:site/index.html
*/


  }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }

     function calculateAndDisplayRoute(pos1,pos2,lat1,lng1,lat2,lng2) {
       var xhr = new XMLHttpRequest();
       var weight = document.getElementById('myRange').value
       xhr.open('GET','api/'+lng1+'/'+lat1+'/'+lng2+'/'+lat2+'/'+weight*0.000001);
       xhr.onload = function(data) {
         coords = JSON.parse(data.currentTarget.response).path
         console.log(coords)
          var waypts = [];
          var otherpts = [];
          var geocoder = new google.maps.Geocoder;
          for (var i = 0; i < coords.length; i++) {
              var curPos = {
               lat: coords[i][1],
               lng: coords[i][0]
             };
            console.log(curPos)
             otherpts.push({location: $.extend({},curPos), stopover: true})
          }
          setTimeout(function() {  
            if (weight<100)
              otherpts = []
            console.log(otherpts)
            var directionsService = new google.maps.DirectionsService();
            var directionsDisplay = new google.maps.DirectionsRenderer;
            directionsDisplay.setMap(map)
            console.log($("mode").find("option:selected").val())
            directionsService.route({
              origin: pos1,
              destination: pos2,
              waypoints: otherpts,
              optimizeWaypoints: true,
              travelMode: 'DRIVING',
              provideRouteAlternatives: true
            }, function(response, status) {
              if (status === 'OK') {
                console.log(response)
                directionsDisplay.setDirections(response);
                var route = response.routes[0];
                var summaryPanel = document.getElementById('dir');
                summaryPanel.innerHTML = '';
                // For each route, display summary information.
                for (var i = 0; i < route.legs.length; i++) {
                  var routeSegment = i + 1;
                  summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
                      '</b><br>';
                  summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
                  summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
                  summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
                }
              } else {
                window.alert('Directions request failed due to ' + status);
              }
            });
             },500);
        }
       xhr.send();
      }
