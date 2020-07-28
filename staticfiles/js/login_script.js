const username = document.getElementById('emailLog');
username.setAttribute("oninput","validateUsername()");

const password = document.getElementById('passwordLog');
password.setAttribute("oninput","validatePassword()");

const loginform = document.getElementById('loginForm');

const green = '#4CAF50';
const red = '#F44336';

loginForm.addEventListener('submit', function(event) {
  if(validateUsername() && validatePassword()){
    return true;
  }
  else{
    event.preventDefault();
    return false;
  };
});


// Validators
function validateUsername() {
  // check if is empty
  if (checkIfEmpty(username)) return;
  return true;
}
function validatePassword() {
  // Empty check
  if (checkIfEmpty(password)) return;

  // Must of in certain length
  if (!meetLength(password, 8, 12)) return;

  // check password against our character set
  // 1- a
  // 2- a 1
  // 3- A a 1
  // 4- A a 1 @
  //   if (!containsCharacters(password, 4)) return;
  return true;
}

//check for max and min length of field
function meetLength(field, minLength, maxLength) {
  if (field.value.length >= minLength && field.value.length < maxLength) {
    setValid(field);
    return true;
  } else if (field.value.length < minLength) {
    setInvalid(
      field,
      `${field.name} must be at least ${minLength} characters long`
    );
    return false;
  } else {
    setInvalid(
      field,
      `${field.name} must be shorter than ${maxLength} characters`
    );
    return false;
  }
}

//check for empty field
function checkIfEmpty(field) {
  if (isEmpty(field.value.trim())) {
    // set field invalid
    setInvalid(field, `${field.name} must not be empty`);
    return true;
  } else {
    // set field valid
    setValid(field);
    return false;
  }
}
function isEmpty(value) {
  if (value === '') return true;
  return false;
}

//setting up the output
function setInvalid(field, message) {
  field.className = 'invalid';
  field.nextElementSibling.innerHTML = message;
  field.nextElementSibling.style.color = red;
}
function setValid(field) {
  field.className = 'valid';
  field.nextElementSibling.innerHTML = '';
  //field.nextElementSibling.style.color = green;
}

