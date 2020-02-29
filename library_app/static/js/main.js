// nav functions

// nav menu toggle
// function also hides add book icon
function navUp() {

    var navState = document.getElementById("popNav")
    var searchState = document.getElementById("popSearch")
    var hideAddIcon = document.getElementById("addBookIcon")
    
    if (navState.style.height == "0%" || navState.style.height == "") {
        navState.style.height = "45%";
        searchState.style.height = "0%";
        hideAddIcon.style.display = "none";
    } else {
        navState.style.height = "0%";
        hideAddIcon.style.display = "block";
    }

}


// search filter toggle
// function also hides add book icon
function searchUp() {

    var searchState = document.getElementById("popSearch")
    var navState = document.getElementById("popNav")
    var hideAddIcon = document.getElementById("addBookIcon")
    if (searchState.style.height == "0%" || searchState.style.height == "") {
        searchState.style.height = "45%";
        navState.style.height = "0%";
        hideAddIcon.style.display = "none";
    } else {
        searchState.style.height = "0%";
        hideAddIcon.style.display = "block";
    }
}
