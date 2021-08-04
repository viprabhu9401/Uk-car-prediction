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
