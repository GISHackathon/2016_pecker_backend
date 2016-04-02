var pckr =  pckr || {};

// TODO: get user details from database/twitter
pckr.User =  function(email, name) {

    this._email = email;

    this._name = name;

};

// user mail
pckr.User.prototype._email;

// user name
pckr.User.prototype._name;

// array of object
pckr.User.prototype._corrections = [];


pckr.User.prototype.setCorections = function(crs){
    this._corrections = crs
};

pckr.User.prototype.getCorections = function(){
    return this._corrections;
};