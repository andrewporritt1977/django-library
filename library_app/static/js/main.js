// nav functions

function navUp() {

    var navState = document.getElementById("popNav")
    if (navState.style.height == "0%") {
        navState.style.height = "45%";
    } else {
        navState.style.height = "0%"
    }

}

