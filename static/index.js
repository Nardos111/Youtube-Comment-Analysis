function submit() {
  var url = document.getElementById("typeURL").value;
  if (url == "") {
    p = document.getElementById("alert");
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    check = validateYouTubeUrl(url);
    if (check) {
      analyse(url);
    }
  }
}

function validateYouTubeUrl(url) {
  var matches = url.match(/watch\?v=([a-zA-Z0-9\-_]+)/);
  if (matches) {
    return true;
  } else {
    return false;
  }
}

function analyse(url) {
  $.ajax({
    type: "POST",
    url: "/comment/",
    data: { param: url },
  }).done(function (o) {
    alert("Done");
  });
}
