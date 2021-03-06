function autocomplete(inp) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < tramites.length; i++) {
        /*Buscamos si un nombre o descripcion incluye la palabra:*/
        if  (tramites[i].toUpperCase().includes(val.toUpperCase()) || descripciones[i].toUpperCase().includes(val.toUpperCase())){
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = tramites[i];
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + tramites[i] + "' id='" + i +"'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              openInNewTab(links[this.getElementsByTagName("input")[0].id])
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
/*execute a function presses a key on the keyboard:*/
inp.addEventListener("keydown", function(e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      }
    }
});
function addActive(x) {
  /*a function to classify an item as "active":*/
  if (!x) return false;
  /*start by removing the "active" class on all items:*/
  removeActive(x);
  if (currentFocus >= x.length) currentFocus = 0;
  if (currentFocus < 0) currentFocus = (x.length - 1);
  /*add class "autocomplete-active":*/
  x[currentFocus].classList.add("autocomplete-active");
}
function removeActive(x) {
  /*a function to remove the "active" class from all autocomplete items:*/
  for (var i = 0; i < x.length; i++) {
    x[i].classList.remove("autocomplete-active");
  }
}
function closeAllLists(elmnt) {
  /*close all autocomplete lists in the document,
  except the one passed as an argument:*/
  var x = document.getElementsByClassName("autocomplete-items");
  for (var i = 0; i < x.length; i++) {
    if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
    });
}
/* Creamos nuestra funcion para levantar Jsons desde WebService */
var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
    var status = xhr.status;
    if (status === 200) {
      callback(null, xhr.response);
    } else {
      callback(status, xhr.response);
    }
  };
  xhr.send();
};

/* Para abrir nuevas pestañas */
function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}

/* EMPEZAMOS EL PROCESAMIENTO */
/*Instanciamos nuestros 3 arrays*/
var tramites = [];
var descripciones = [];
var links = [];

/*Obtenemos todos los tramites que tiene el sistema desde el web service:*/
getJSON('/ws_tramites',
        function(err, json_tr) 
        {
          for (i = 0; i < json_tr.data.length; i++) 
          {
            tramites[i] = json_tr.data[i].nombre;
            descripciones[i] = json_tr.data[i].descripcion;
            links[i] = json_tr.data[i].link;
          }
        }
      );

/*Obtenemos todos los tramites que tiene el sistema desde el web service:*/
getJSON('/ws_guias',
        function(err, json_gui) 
        {
          for (i = 0; i < json_gui.data.length; i++) 
          {
            tramites[tramites.length] = json_gui.data[i].nombre;
            descripciones[descripciones.length] = json_gui.data[i].descripcion;
            links[links.length] = json_gui.data[i].link;
          }
        }
      );

/*initiate the autocomplete function on the "myInput" element, and pass along the tramites array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"));