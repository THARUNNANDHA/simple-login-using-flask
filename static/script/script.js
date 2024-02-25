
function validateForm() {
    var name = document.getElementById("uname").value;
    var pass = document.getElementById("psw").value;
    if (name.length <= 3) {
        alert("Username must be greater than 3 characters");
        return false;
    } else if (pass.length <= 4) {
        alert("Password must be greater than 4 characters");
        return false;
    }
    // AJAX request to submit form data
    var formData = new FormData(document.getElementById("loginForm"));
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/check_data", true);
    xhr.onload = function() {
        if (xhr.status == 200) {
            document.getElementById("result").innerHTML = xhr.responseText;
        }
    };
    xhr.send(formData);
    return false; // Prevent form submission
}