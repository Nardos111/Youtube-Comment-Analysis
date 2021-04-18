function submit() {
  var url = document.getElementById("typeURL").value;
  console.log(url);
  if (url == "") {
    p = document.getElementById("alert");
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    check = validateYouTubeUrl(url);
    if (check) {
      //comments(url);
      console.log(url);
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

// function comments(url) {
//   $.ajax({
//     type: "POST",
//     url: "/comment/",
//     data: { param: url },
//   }).done(function (o) {
//     alert("Done");
//   });
// }
