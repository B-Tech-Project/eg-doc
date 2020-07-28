$(document).ready(function(){
    $('select').formSelect();
});
// Input fields

const name = document.getElementById('id_name');
name.setAttribute("oninput","validateName()");

const password = document.getElementById('id_password1');
password.setAttribute("oninput","validatePassword()");

const confirmPassword = document.getElementById('id_password2');
confirmPassword.setAttribute("oninput","validateConfirmPassword()");

const email = document.getElementById('id_email');
email.setAttribute("oninput","validateEmail()");

const address = document.getElementById('id_address');
address.setAttribute("oninput","validateAddress()");

const city = document.getElementById('id_city');
city.setAttribute("oninput","validateCity()");

const pin = document.getElementById('id_pin');
pin.setAttribute("oninput","validatePin()");

const state = document.getElementById('id_state');
state.setAttribute("oninput","validateState()");
// Form

const form = document.getElementById('RegistrationForm');
// Validation colors
const green = '#4CAF50';
const red = '#F44336';

// Handle form
form.addEventListener('submit', function(event) {
  // Prevent default behaviour

  if (
    validateName() &&
    validatePassword() &&
    validateConfirmPassword() &&
    validateEmail() &&

    validateAddress() &&
    validateState() &&
    validateCity() &&
    validatePin()
  ) {

    return true;

  }
  else{
    event.preventDefault();
    return false;
   }
});

// Validators
function validateName() {
  // check if is empty
  if (checkIfEmpty(name)) return;
  // is if it has only letters
  if (!checkIfOnlyLetters(name)) return;
   if (!meetLength(name, 4, 20)) return;
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
function validateConfirmPassword() {
  if (password.className !== 'valid') {
    setInvalid(confirmPassword, 'Password must be valid');
    return;
  }
  // If they match
  if (password.value !== confirmPassword.value) {
    setInvalid(confirmPassword, 'Passwords must match');
    return;
  } else {
    setValid(confirmPassword);
  }
  return true;
}
//validate email
function validateEmail() {
  if (checkIfEmpty(email)) return;
  if (!containsCharacters(email, 5)) return;
  return true;
}

//validate address
function validateAddress() {
  if (meetLength(address,3, 200, ))
  if(checkIfEmpty(address)) return;
  return true;
}
//validate state
function validateState() {
  if(checkIfEmpty(state)) return;
  return true;
}
//validate city
function validateCity(){
  if(meetLength(city,2, 20))
  if(checkIfEmpty(city)) return;
  return true;
}
//validate pin
function validatePin(){
  if(checkIfEmpty(pin)) return;
  if(pin.value.length == 6){
    setValid(pin);
    return true;
  }
  setInvalid(pin, `Pin should be of six digits`);
  return false;
}

// Utility functions
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

//check for letter only field
function checkIfOnlyLetters(field) {
  if (/^(?!\.)[A-Za-z. ]+$/.test(field.value)) {
    setValid(field);
    return true;
  } else {
    setInvalid(field, `${field.name} must contain only letters and .`);
    return false;
  }
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

//check for characters
function containsCharacters(field, code) {
  let regEx;
  switch (code) {
    case 1:
      // letters
      regEx = /(?=.*[a-zA-Z])/;
      return matchWithRegEx(regEx, field, 'Must contain at least one letter');
    case 2:
      // letter and numbers
      regEx = /(?=.*\d)(?=.*[a-zA-Z])/;
      return matchWithRegEx(
        regEx,
        field,
        'Must contain at least one letter and one number'
      );
    case 3:
      // uppercase, lowercase and number
      regEx = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])/;
      return matchWithRegEx(
        regEx,
        field,
        'Must contain at least one uppercase, one lowercase letter and one number'
      );
    case 4:
      // uppercase, lowercase, number and special char
      regEx = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)/;
      return matchWithRegEx(
        regEx,
        field,
        'Must contain at least one uppercase, one lowercase letter, one number and one special character'
      );
    case 5:
      // Email pattern
      regEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return matchWithRegEx(regEx, field, 'Must be a valid email address');
    default:
      return false;
  }
}
function matchWithRegEx(regEx, field, message) {
  if (field.value.match(regEx)) {
    setValid(field);
    return true;
  } else {
    setInvalid(field, message);
    return false;
  }
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
