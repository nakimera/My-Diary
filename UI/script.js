var modal = document.getElementById('modal');

var signup = document.getElementById('signup');

var close = document.getElementsByClassName("close")[0];

signup.onclick = function() {
    modal.style.display = "block";
}

close.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}