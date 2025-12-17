function togglePassword() {
    var passwordInput = document.getElementById("password");
    var eyeOpen = document.getElementById("eye-open");
    var eyeClosed = document.getElementById("eye-closed");
    if (passwordInput.type === "password")  {
        passwordInput.type = "text";
        eyeOpen.style.display = "block";
        eyeClosed.style.display = "none";
    } else {
        passwordInput.type = "password";
        eyeOpen.style.display = "none";
        eyeClosed.style.display = "block";
    }

}