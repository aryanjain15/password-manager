var passwordRaw = document.getElementById("password");


function generatePassword() {
    var pass = '';
    var str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$';

    for (i = 1; i <= 20; i++) {
        var char = Math.floor(Math.random()
            * str.length + 1);
// Charat is a method to get a index of a string in Js
        pass += str.charAt(char)
    }

    return pass;
}

function passwordOutput() {
    passwordRaw.innerHTML = generatePassword();
}

