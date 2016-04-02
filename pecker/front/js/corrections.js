var pckr =  pckr || {};

pckr.Corrections =  function(data) {


    pckr.Corrections._corrections = data;




    pckr.Corrections.createLayer();

};

pckr.Corrections._corrections = [];

pckr.Corrections.createLayer = function() {


    L.geoJson(pckr.Corrections._corrections, {
        onEachFeature: pckr.Corrections.onEachFeature
    }).addTo(pckr.Map._map);

};

pckr.Corrections.onEachFeature = function(feature, layer) {

    layer.setIcon(L.icon.mapkey({icon:"flag",background:"#41ad2b",size:40}));

    var wrapper = $('<div>');

    var properties = feature.properties;

    var wrapperImg = $('<div>',{class: 'pckr-feature-wrapperImg'})
    .appendTo(wrapper);

    var img = $('<img>',{src:properties.img_url, class: 'pckr-feature-img'})
        .appendTo(wrapperImg)
        .on('click',function(){console.log('ahoj')});

    var desc = $('<div>',{class: 'pckr-feature-desc'})
        .html(properties.text)
        .appendTo(wrapper)
        .on('click',function(){console.log('ahoj')});

    var pnrm = $('<a>',{class: 'pckr-feature-panoramaLink'})
        .html('MAPY.CZ PANORAMA')
        .appendTo(wrapper)
        .on('click',function(){pckr.Corrections.createPanorama(feature)});

    var user = $('<a>',{href:'https://twitter.com/intent/user?user_id='+properties.user_id, target:'blanc_', class: 'pckr-feature-userLink'})
        .html('USER')
        .appendTo(wrapper);

    var ruian = $('<a>',{href:'http://reklamace.cuzk.cz/formular/index.php?logged=-3', target:'blanc_', class: 'pckr-feature-userLink'})
        .html('RIUAN')
        .appendTo(wrapper);

    layer.bindPopup(wrapper[0]);

};

pckr.Corrections.createPanorama = function(feature){


    var coors = feature.geometry.coordinates

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