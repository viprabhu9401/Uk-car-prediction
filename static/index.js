$(document).ready(function () {
  const cars = [
    {
      make: "ford",
      model: ["focus", "fiesta"],
    },
    {
      make: "toyota",
      model: ["corolla", "camry"],
    },
  ];
 
toggleOptions();
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
});
