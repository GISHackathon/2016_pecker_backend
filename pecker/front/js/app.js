
var pMap = new pckr.Map('map', { center: new L.LatLng(49.211, 16.615), zoom: 16} );

var map =  pMap.getMap();

var layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {}).addTo(map);


var win =  L.control.window(map,{title:'Twitter login',content:'ahoj'})
    .prompt({callback:function(){alert('This is called after OK click!')}});

$('#loginBtn').on('click',function () {
    win.show()
});

pckr.Xhr.doGet('corrections/all','').then(
    function(data) {
       pckr.Corrections(data)
    }, function() {
       alert('Vyskytla se chyba pri nacitani dat!');

    }
);

pckr.Xhr.doGet('errors/all','').then(
    function(data) {
        pckr.Errors(data)
    }, function() {
        alert('Vyskytla se chyba pri nacitani dat!');

    }
);

var sidebar = L.control.sidebar('sidebar', {
    position: 'right'
});
map.addControl(sidebar);

var twitter = L.easyButton( 'fa fa-twitter', function(){
    alert('twitter login');
}).addTo(map);