/*
 *  CHALLENGE 2
 */

// logic for the first person
let firstPerson = () => {
  for (n = 2; n <= 100; n += 2) {
    console.log(`switching on bulb ${n}`);
  }
}
firstPerson();

// logic for second person
let secondPerson = () => {
  for (n = 3; n <= 100; n += 3) {
    console.log(`switching on bulb ${n}`);
  }
}
secondPerson();

// logic for third person
let thirdPerson = () => {
  for (n = 4; n <= 100; n += 4) {
    console.log(`switching on bulb ${n}`);
  }
}
thirdPerson();

function numberOfLights(n, bulbs = 100){ // the hallway has 100 bulbs, with undefinded number of people(n)
  // an empty array to store every bulb that gets lit
  let bulbsLit = [];
  for(i = n; i <= bulbs; i += n){
  // as we loop, we store every bulb we light into the empty list
  bulbsLit.push(i);
  }
  /*
   * After we are done looping and storing,
   * we return the number of lights in the array
   */
  console.log(`${bulbsLit.length} bulbs have been switched`) 
  return bulbsLit.length;
}

// call function and pass any arument to test
numberOfLights(2)
