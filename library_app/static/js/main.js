// nav functions

// function navDown() {
//     document.getElementById("popNav").style.height= "0%";
//     document.getElementById("navLink").style.width= "0%";
// }

function navUp() {

    var navState = document.getElementById("popNav")
    if (navState.style.height == "0%") {
        navState.style.height = "45%";
    } else {
        navState.style.height = "0%"
    }
    // document.getElementById("popNav").style.height = "45%";
    // document.getElementById("navLink").style.width= "100%";
}