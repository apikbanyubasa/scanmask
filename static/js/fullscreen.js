function toggleFullscreen(id) {
  const elem = document.getElementById(id);
  if (!document.fullscreenElement) {
    elem.requestFullscreen().then(() => {
      elem.classList.add("fullscreen-mode");
    }).catch((err) => {
      alert(`Gagal masuk fullscreen: ${err.message}`);
    });
  } else {
    document.exitFullscreen();
    elem.classList.remove("fullscreen-mode");
  }
}
