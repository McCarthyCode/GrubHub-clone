var geocoder;
var map;

function codeAddresses(addresses) {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644);
    var mapOptions = {
        zoom: 8,
        center: latlng
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    for (var i = 0; i < addresses.length; i++) {
        geocoder.geocode({ 'address': addresses[i] }, function (results, status) {
            if (status == 'OK') {
                map.setCenter(results[0].geometry.location);
                map.setZoom(13)
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location
                });
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
}