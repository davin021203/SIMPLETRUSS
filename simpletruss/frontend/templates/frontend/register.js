function register() {
    const username = document.getElementById("regUsername").value;
    const password = document.getElementById("regPassword").value;

    if (username && password) {
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        document.getElementById("regMessage").innerText = "Registration successful!";
    } else {
        document.getElementById("regMessage").innerText = "Please fill both fields.";
    }
}