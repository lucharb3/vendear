console.log("test 2 ");

function menuButton(x) { //Change la Classe du bouton menu à la classe menuClose (le x au lieux des 3 lignes).
    x.classList.toggle("menuClose"); 
  }
  function openNav() { //Ouvre le overlayNav.
    document.getElementById("myNav").style.height = "100%";
  }
  
  function closeNav() { //Ferme le overlayNav.
    document.getElementById("myNav").style.height = "0%";
  }

function toggleNav() { //Bascule le overlayNav.
  console.log("active"); //Pour tester si la fonction a été activé.
  var toggleNav = document.getElementById("myNav").style.height;

  if (toggleNav < "10%") {
      openNav(); 
      console.log("open"); //Pour tester si le fonction openNav a été activé.
  } else {
      closeNav()
      console.log("closed"); //Pour tester si le fonction closeNav a été activé.
  }
}