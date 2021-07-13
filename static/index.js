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
  var ar = []
  $.ajax({
    type: "GET",
    url: "/video_info.csv/",
    dataType: "text",
    success: function (data) {
      arr = data.split('\n')
      for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].trim('"\\')
        arr[i] = arr[i].trim('\\r"')
        arr[i] = arr[i].replace('""', '')
      }
      ar = Object.assign([], arr)
      var sec = document.getElementById("portfolio")
      sec.removeAttribute("hidden")
      var mainC = document.getElementsByClassName("allVideos")
      console.log(ar)
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
        var contentContainer = document.createElement("div")
        contentContainer.setAttribute("class", "content")
        var title = document.createElement("h5")
        title.textContent = ar[(i * 8) + 1]
        contentContainer.appendChild(title)
        var details = document.createElement("h6")
        details.textContent = "Video Uploaded by " + ar[(i * 8) + 3] + ".        " + ar[(i * 8) + 4] + " views"
        var info = document.createElement("p")
        info.textContent = ar[(i * 8) + 2]
        contentContainer.appendChild(info)
        var source = document.createElement("h6")
        source.textContent = "Views: " + ar[(i * 8) + 4] + ", Likes: " + ar[(i * 8) + 6] + ", Dislikes: " + ar[(i * 8) + 7]
        contentContainer.appendChild(source)
        c.appendChild(contentContainer)

        $.ajax({
          type: "POST",
          url: "/clean/"
        }).done(function (o) {
          $.ajax({
            type: "POST",
            url: "/analyze/"
          }).done(function (o) {
            console.log("done")
            console.log(o)
          })
        })
        var c2 = document.createElement("div")
        c2.setAttribute("class", "col-lg-6 offset-lg-3")
        var imageContainer = document.createElement("div")
        imageContainer.setAttribute("class", "image2")
        var image = document.createElement("img")
        image.setAttribute("width", "500")
        image.setAttribute("height", "350")
        image.setAttribute("src", `./static/${i + 1}plot.jpg`)
        imageContainer.appendChild(image)
        c2.appendChild(imageContainer)
        mainC[0].appendChild(c2)

        // .done(function (o) {
        //   console.log(o)
        //   $.ajax({
        //     type: "POST",
        //     url: "/clean/",
        //     data: { param: o }
        //   })
        // });
      }
    }
  })


}