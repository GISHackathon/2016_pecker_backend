var pckr =  pckr || {};

pckr.Errors =  function(data) {


    pckr.Errors._data = data;

    pckr.Errors.createLayer();

};

pckr.Errors._data = [];

pckr.Errors.createLayer = function() {

    L.geoJson(pckr.Errors._data, {
        onEachFeature: pckr.Errors.onEachFeature
    }).addTo(pckr.Map._map);

};

pckr.Errors.onEachFeature = function(feature, layer) {

    layer.setIcon(L.icon.mapkey({icon:"flag",background:"#ef0000",size:32}));

    var wrapper = $('<div>');

    var properties = feature.properties;


    var pnrm = $('<div>',{class: 'pckr-feature-panoramaLink'})
        .html('id: '+ properties.id)
        .appendTo(wrapper)


    layer.bindPopup(wrapper[0]);

};

pckr.Errors.createPanorama = function(feature){


    var coors = feature.geometry.coordinates;

    var options = {
        nav: false, // skryjeme navigaci
        pitchRange: [0, 0] // zakazeme vertikalni rozhled
    };

    var panoramaScene = new SMap.Pano.Scene(document.querySelector(".panorama"), options);

// kolem teto pozice chceme nejblizsi panorama

    var lon = coors[0];
    var lat = coors[1];
    var position = SMap.Coords.fromWGS84(lon, lat);

    // hledame s toleranci 50m
    SMap.Pano.getBest(position, 50).then(function(place) {

        var data = place.getData();

        window.open('https://mapy.cz/zakladni?z=18&pid='+data.pid + '&source=coor&id='+lon+'%2C'+lat)
        panoramaScene.show(place);

    }, function() {
        alert("Panorama se nepodařilo zobrazit!");
    });



};