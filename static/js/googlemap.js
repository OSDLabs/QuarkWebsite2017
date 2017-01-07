function initMap() {
    var bpgc = { lat: 15.3900, lng: 73.8773 };
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
        zoom: 14,
        center: bpgc
    });
    var marker = new google.maps.Marker({
        position: bpgc,
        map: map
    });
}
