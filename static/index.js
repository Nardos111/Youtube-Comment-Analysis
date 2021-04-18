function submit() {
  var url = document.getElementById("typeURL").value;
  if (url == "") {
    var p = document.getElementById("alert");
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    check = validateYouTubeUrl(url);
    if (check) {
    comments(url);
    }
    else {
      document.getElementById("alert").innerHTML = "⚠️ Invalid URL";
      var pa = document.getElementById("alert")
      pa.style.color = "rgb(194, 35, 35)"
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

function comments(url) {
  console.log(url)
  $.ajax({
    type: "POST",
    url: "/comment",
    data: { url_link: url},
  }).done(function (o) {
    alert("Done");
  });
}
