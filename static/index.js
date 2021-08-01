$(document).ready(function () {
  const arr = [
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

  function toggleOptions() {
    $("#make").on("change", () => {
      $('#model').empty();
      arr.forEach((a) => {
        if ($("#make").val().toLowerCase() === a.make) {
          a.model.forEach((i) => {
            console.log(i);
            $("#model").append(`<option value ="${i}">${i}</option>`);
          });
        }
      });
    });

    $("#model").empty();
  }
});
