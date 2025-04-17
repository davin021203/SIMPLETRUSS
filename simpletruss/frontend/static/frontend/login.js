function login() {
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    const storedUsername = localStorage.getItem("username");
    const storedPassword = localStorage.getItem("password");

    if (username === storedUsername && password === storedPassword) {
        document.getElementById("loginMessage").innerText = "Login successful!";
    } else {
        document.getElementById("loginMessage").innerText = "Invalid credentials.";
    }
}