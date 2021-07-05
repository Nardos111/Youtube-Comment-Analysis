function submit() {
  var key = document.getElementById("typeURL").value;
  document.getElementById("alert").classList.add("blink_me")
  document.getElementById("alert").style.color = "white"
  if (key == "") {
    var p = document.getElementById("alert");
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    // check = validateYouTubeUrl(url);
    comments(key);
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

function comments(key) {
  document.getElementById("alert").classList.remove("blink_me")
  document.getElementById("alert").innerHTML = "Processing. This will only take few minutes";
  document.getElementById("alert").style.color = "green"
  $.ajax({
    type: "POST",
    url: "/comment",
    data: { keyword: key },
  }).done(function (o) {
    document.getElementById("alert").innerHTML = "Video Comments Scraped!";
    displayInfo()

  });
}

function displayInfo() {
  alert("done")
}
