$(document).ready(function () {
  const cars = [
    {
      make: "ford",
      model: ["Fiesta", "Focus", "Puma", "Kuga", "EcoSport", "C-MAX", "Mondeo",
      "Ka+", "Tourneo Custom", "S-MAX", "B-MAX", "Edge",
      "Tourneo Connect", "Grand C-MAX", "KA", "Galaxy", "Mustang",
      "Grand Tourneo Connect", "Fusion", "Ranger", "Streetka", "Escort",
      "Transit Tourneo"],
    },
    {
      make: "toyota",
      model: ["GT86", "Corolla", "RAV4", "Yaris", "Auris", "Aygo", "C-HR",
      "Prius", "Avensis", "Verso", "Hilux", "PROACE VERSO",
      "Land Cruiser", "Supra", "Camry", "Verso-S", "IQ", "Urban Cruiser"],
    },
    {
      make: "hyundai",
      model: ["I20", "Tucson", "I10", "IX35", "I30", "I40", "Ioniq", "Kona",
      "Veloster", "I800", "IX20", "Santa Fe", "Accent", "Terracan",
      "Getz", "Amica"],
    },
    {
      make: "vw",
      model: ["T-Roc", "Golf", "Passat", "T-Cross", "Polo", "Tiguan", "Sharan",
       "Up", "Scirocco", "Beetle", "Caddy Maxi Life", "Caravelle",
       "Touareg", "Arteon", "Touran", "Golf SV", "Amarok",
       "Tiguan Allspace", "Shuttle", "Jetta", "CC", "California",
       "Caddy Life", "Caddy", "Caddy Maxi", "Eos", "Fox"],
    },
    {
      make: "vx",
      model: ["Corsa", "Astra", "Viva", "Mokka", "Mokka X", "Crossland X",
      "Zafira", "Meriva", "Zafira Tourer", "Adam", "Grandland X",
      "Antara", "Insignia", "Ampera", "GTC", "Combo Life", "Vivaro",
      "Cascada", "Kadjar", "Agila", "Tigra", "Vectra"],
    },
    {
      make: "skoda",
      model: ["Octavia", "Citigo", "Yeti Outdoor", "Superb", "Kodiaq", "Rapid",
      "Karoq", "Fabia", "Yeti", "Scala", "Roomster", "Kamiq"],
    }
  ];
 
toggleOptions();
incrementYear();
 // function to change the model options based on make input selection
  function toggleOptions() {
     $("#make").on("change", () => {
      $('#model').empty();
      cars.forEach((car) => {
        if ($("#make").val().toLowerCase() === car.make) {
          car.model.forEach((m) => {
            $("#model").append(`<option value ="${m}">${m}</option>`);
          });
        }
      });
    });
}
function incrementYear(){
    const year = $('#year')
    const currentYear =(new Date()).getFullYear()
    for(i=1990; i<=currentYear; i++){
      const option = $("<option></option>");
      option.html(i);
      option.val(i);
      year.append(option);
    }
}
});
