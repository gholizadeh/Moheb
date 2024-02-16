
document.addEventListener("DOMContentLoaded", function() {
    "use strict";

    /*==================================================================
    [ Focus input ]*/
    var inputs = document.querySelectorAll('.input100');
    inputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            if (this.value.trim() !== "") {
                this.classList.add('has-val');
            } else {
                this.classList.remove('has-val');
            }
        });
    });
    
    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    var showPassButtons = document.querySelectorAll('.btn-show-pass');
    showPassButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var inputField = this.nextElementSibling;
            if (showPass === 0) {
                inputField.type = 'text';
                this.querySelector('i').classList.remove('fa-eye');
                this.querySelector('i').classList.add('fa-eye-slash');
                showPass = 1;
            } else {
                inputField.type = 'password';
                this.querySelector('i').classList.add('fa-eye');
                this.querySelector('i').classList.remove('fa-eye-slash');
                showPass = 0;
            }
        });
    });
});