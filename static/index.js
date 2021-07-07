function submit() {
  var key = document.getElementById("typeURL").value;
  document.getElementById("alert").classList.add("blink_me")
  document.getElementById("alert").style.color = "white"
  if (key == "") {
    var p = document.getElementById("alert");
    p.innerHTML = "⚠️ Please enter a keyword"
    p.style.color = "rgb(194, 35, 35)";
  } else {
    p = document.getElementById("alert");
    p.style.color = "white";
    // check = validateYouTubeUrl(url);
    comments(key);

  }
}

// function validateYouTubeUrl(url) {
//   var matches = url.match(/watch\?v=([a-zA-Z0-9\-_]+)/);
//   if (matches) {
//     return true;
//   } else {
//     return false;
//   }
// }

function comments(key) {
  allVideos = document.getElementsByClassName("allVideos")
  allVideos[0].innerHTML = ""
  document.getElementById("alert").classList.remove("blink_me")
  document.getElementById("alert").innerHTML = "Processing. This will only take few minutes";
  document.getElementById("alert").style.color = "green"
  $.ajax({
    type: "POST",
    url: "/comment/",
    data: { keyword: key },
  }).done(function (o) {
    displayVideos()
    document.getElementById("alert").innerHTML = "Video Comments Scraped!";


  });
}

function displayInfo() {
  alert("done")
}

function displayVideos() {
  var sec = document.getElementById("portfolio")
  sec.removeAttribute("hidden")
  var mainC = document.getElementsByClassName("allVideos")
  for (let i = 0; i < 2; i++) {
    var c = document.createElement("div")
    c.setAttribute("class", "col-lg-12 container videos")
    var imageContainer = document.createElement("div")
    imageContainer.setAttribute("class", "image")
    var image = document.createElement("img")
    image.setAttribute("width", "200")
    image.setAttribute("height", "130")
    image.setAttribute("src", `./static/${i + 1}.jpg`)
    imageContainer.appendChild(image)
    c.appendChild(imageContainer)
    mainC[0].appendChild(c)
    $.ajax({
      type: "GET",
      url: "video_info.csv",
      dataType: "text",
      success: function (data) { console.log(data); }
    });
  }
}