window.onload = function(){
    lastModified('modifiedOn');
};

function lastModified(id){
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var d = new Date(document.lastModified);
    var sModified = [months[d.getMonth()], d.getDate() + ',' , d.getFullYear()].join(' ');
    var inner = document.getElementById(id).innerHTML += sModified
};
