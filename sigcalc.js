$(document).ready(function() {
  function sig_calc() {
    jsSHA = require("jssha");
    var api_id = "31d4d730-1aad-0136-9a37-0abfe2d6609e";
    var secret = "zq9EcsMxT2Y4tQwU9hQVJ3GIkNuAUnaF1XQWcJcFY";
    var timestamp = Date.now();
    var data = "";
    var nonce = "OetR6gkPEu";
    var shaObj = new jsSHA("SHA-1", "TEXT");
    shaObj.setHMACKey(secret, "TEXT");
    shaObj.update(api_id+timestamp+nonce+data);
    var hmac = shaObj.getHMAC("HEX");
    $('#signature').val(str(hmac));
    $('#nonce').val(str(nonce));
    $('#timestamp').val(str(timestamp)); 
  }
});
