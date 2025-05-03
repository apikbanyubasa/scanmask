let isCameraOn = true;

function toggleCamera() {
  const img = document.querySelector('#camera-frame img');
  const switchBox = document.getElementById('toggle-switch');

  if (isCameraOn) {
    img.src = "";
    switchBox.classList.remove("bg-green-500");
    switchBox.classList.add("bg-red-500");
    switchBox.children[0].classList.add("translate-x-full");
  } else {
    img.src = "/video";
    switchBox.classList.remove("bg-red-500");
    switchBox.classList.add("bg-[#05465D]");
    switchBox.children[0].classList.remove("translate-x-full");
  }

  isCameraOn = !isCameraOn;
}
