function register() {
    const username = document.getElementById("regUsername").value;
    const password = document.getElementById("regPassword").value;
    const email = document.getElementById("regEmail").value;

    if (username && password) {
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        document.getElementById("regMessage").innerText = "Registration successful!";
    } else {
        document.getElementById("regMessage").innerText = "Please fill both fields.";
    }
    console.log(username, password, email)

    fetch("/api/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
            'username': username, 
            'password': password, 
            'email': email})
    }).then(result => {
        if (result.ok) {
            window.location.href = "/";
        } else {
            alert("Registration failed. Please try again.");
        }
    })
}