# global-redirect

Basically just had to check the source code for a path:
```js
function loginAuthenticate(){
  var password = document.getElementById("password");
  var hash = sjcl.hash.sha256.hash(password);
  var hexRepresentation = sjcl.codec.hex.fromBits(hash);
  if (hexRepresentation == "2a70282a868c0ca9e6fe5bb5cf2ac2ea6b523062102bada26fb87091d511e3f1"){
    alert("welcome Home Admin");
    window.location = "./0078f62f00305b73de6ccace8f9fc1f68a8f1dcec865d33fcacbaf255ddefaa7";
  }else{
    alert("Incorrect Password. Please Try Again");
  }
  alert(hash);
} 
```

Then when you went to that path you got the flag.

Flag: `BCCTF{T1ck3t_t0_0wn3rsh1p!}`