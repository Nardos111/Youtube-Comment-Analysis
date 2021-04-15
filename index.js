function submit() {
  var url = document.getElementById("typeURL").value;
  if (url == "") {
    p = document.getElementById("alert");
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    check = validateYouTubeUrl(url);
    window.alert(check);
  }
}

function validateYouTubeUrl(url) {
  if (url != undefined || url != "") {
    var regExp = /^.*(youtu.be/|v/|u/w/|embed/|watch?v=|&v=|?v=)([^#&?]*).*/;
    var match = url.match(regExp);
    if (match && match[2].length == 11) {
      return True;
    } else {
      return False;
    }
  }
}
