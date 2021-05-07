function initMap() {
    
    const ysjbc = { lat: 53.961118, lng: -1.090317 };
    
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 18,
      center: ysjbc,
    });
    
    const marker = new google.maps.Marker({
      position: ysjbc,
      map: map,
    });
  }