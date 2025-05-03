function toggleFullscreen(id) {
    const elem = document.getElementById(id);
    if (!document.fullscreenElement) {
      elem.requestFullscreen().catch((err) => {
        alert(`Gagal masuk fullscreen: ${err.message}`);
      });
    } else {
      document.exitFullscreen();
    }
  }
  