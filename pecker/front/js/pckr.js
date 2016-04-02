var pckr = {
    version: '0.1.0'
};

// MAP object
pckr.Map = function(querySelector,options) {
    pckr.Map._map = new L.Map(querySelector, options);
};

// leaflet map
pckr.Map._map;

pckr.Map.prototype.getMap = function(){
    return pckr.Map._map
};

// configuration
pckr.setConfig = function(conf) {

    this.config = conf;
};

// api baseurl
pckr.config = {
    server : "http://pecker4.azurewebsites.net/"
};

// XHR
pckr.Xhr = function() {

};

// XHR
pckr.Xhr.doPost = function(route,requestData) {
    return $.ajax({
        type: "POST",
        url: pckr.config['server']+'/'+route,
        data: requestData
    });
};

pckr.Xhr.doGet = function(route,requestData){
    return $.ajax({
        type: "GET",
        url: pckr.config['server']+'/'+route,
        data: requestData
    });
};