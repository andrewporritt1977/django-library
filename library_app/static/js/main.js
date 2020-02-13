// nav functions

// nav menu toggle
function navUp() {

    var navState = document.getElementById("popNav")
    var searchState = document.getElementById("popSearch")
    var hideSearchIcon = document.getElementById("searchicon")
    
    if (navState.style.height == "0%" || navState.style.height == "") {
        navState.style.height = "45%";
        searchState.style.height = "0%";
        hideSearchIcon.style.display = "none";
    } else {
        navState.style.height = "0%";
        hideSearchIcon.style.display = "block";
    }

}


// search filter toggle
function searchUp() {

    var searchState = document.getElementById("popSearch")
    var navState = document.getElementById("popNav")
    var hideNavIcon = document.getElementById("navicon")
    if (searchState.style.height == "0%" || searchState.style.height == "") {
        searchState.style.height = "45%";
        navState.style.height = "0%";
        hideNavIcon.style.display = "none";
    } else {
        searchState.style.height = "0%";
        hideNavIcon.style.display = "none";
    }
}
