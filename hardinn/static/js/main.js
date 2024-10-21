var filter, divPesquisa, itemPesquisa;

filter = document.querySelector(".search")

window.addEventListener("scroll", () => {

    $(function() {
        $(window).on("scroll", function() {
          if($(window).scrollTop() > 500) {
            $(".navbar").addClass("sombra-nav");
            $("nav a").addClass("link-menu-descer");
          } else {
            $(".navbar").removeClass("sombra-nav");
            $("nav a").removeClass("link-menu-descer");
          }
        });
      });

    
})

function um(){
  var card = document.querySelectorAll(".card")
  for (let i = 0; i < card.length; i++) {
    card[i].style.width = "100%"
    card[i].style.height = "200px"
  }
}

function dois(){
  var card = document.querySelectorAll(".card")
  for (let i = 0; i < card.length; i++) {
    card[i].style.width = "45%"
    card[i].style.height = "100px"
  }

};


function pesquisar() {
  var filter, card, w, txtValue, cardCell, wCell;

  filter = document.getElementById("search").value.toUpperCase();
  card = document.querySelectorAll(".card");
  cardCell = document.querySelectorAll(".card-cell");

  for (i = 0; i < card.length; i++) {
      w = card[i].getElementsByTagName("w")[0];
      txtValue = w.textContent;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        card[i].style.display = "";
      } else {
        card[i].style.display = "none";
      }
  }

  for (a = 0; a < cardCell.length; a++) {
    wCell = cardCell[a].getElementsByTagName("w")[0];
    txtValue = wCell.textContent;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      cardCell[a].style.display = "";
    } else {
      cardCell[a].style.display = "none";
    }
}
}
