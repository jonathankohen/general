const nums = [1, 2, 3, 4, 5];

// "=>" is short for return statement
// n reps each number
// i reps index for keys

const doubles = nums.map((n, i) => {
    console.log(i);
    return n * 2;
});

const odds = nums.filter((n) => n % 2 !== 0);
console.log(odds);

const names = [
    { first: 'Adrien', last: 'Dion' },
    { first: 'Yoni', last: 'Kohen' },
    { first: 'Neal', last: 'Goldman' },
    { first: 'Drew', last: 'Schnieder' },
    { first: 'Neal', last: 'Goldman' },
    { first: 'Neal', last: 'Goldman' },
];

const lastSNames = names.filter((name) => name.last[0] === 'S');
console.log(lastSNames);
names.push({ first: 'Natasha', last: 'Charles' });
