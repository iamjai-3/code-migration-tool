let random = Math.random;

function deposit(balance, amount) {
    if (amount > 0) {
        balance += amount;
        return `Deposited $${amount}. New balance: $${balance}`;
    }
    return "Amount must be positive";
}

function withdraw(balance, amount) {
    if (amount > 0) {
        if (balance >= amount) {
            balance -= amount;
            return `Withdrew $${amount}. New balance: $${balance}`;
        }
        return "Insufficient funds";
    }
    return "Amount must be positive";
}

function calculateAreaOfCircle(radius) {
    if (radius > 0) {
        return 3.14159 * Math.pow(radius, 2);
    }
    return "Radius must be positive";
}

function generateRandomPassword(length) {
    if (length > 0) {
        const characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
        return Array.from({length: length}, () => characters.charAt(Math.floor(Math.random() * characters.length))).join('');
    }
    return "Length must be positive";
}

function reverseString(s) {
    return s.split('').reverse().join('');
}

function isPrime(num) {
    if (num < 2) {
        return false;
    }
    for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

function fibonacci(n) {
    if (n <= 0) {
        return [];
    }
    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
    }
    return fib.slice(0, n);
}

function convertCelsiusToFahrenheit(celsius) {
    return (celsius * 9 / 5) + 32;
}

function countVowels(s) {
    return [...s.toLowerCase()].reduce((count, char) => 
        "aeiou".includes(char) ? count + 1 : count, 0);
}

function findMax(numbers) {
    if (numbers.length > 0) {
        return Math.max(...numbers);
    }
    return "List is empty";
}

function factorial(n) {
    if (n < 0) {
        return "Number must be non-negative";
    }
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

function checkPalindrome(s) {
    return s === s.split('').reverse().join('');
}

function mergeTwoLists(list1, list2) {
    return [...list1, ...list2];
}

function sortNumbers(numbers) {
    return numbers.slice().sort((a, b) => a - b);
}

function findGcd(a, b) {
    while (b) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function generateEvenNumbers(limit) {
    return Array.from({length: limit + 1}, (_, i) => i).filter(num => num % 2 === 0);
}

function convertToUpperCase(s) {
    return s.toUpperCase();
}

function calculateBmi(weight, height) {
    if (height <= 0) {
        return "Height must be positive";
    }
    return weight / (height ** 2);
}

function countWords(s) {
    return s.split(' ').length;
}

function findMin(numbers) {
    if (numbers.length) {
        return Math.min(...numbers);
    }
    return "List is empty";
}

function removeDuplicates(numbers) {
    return Array.from(new Set(numbers));
}

function calculatePower(base, exponent) {
    return Math.pow(base, exponent);
}

function isEven(num) {
    return num % 2 === 0;
}

function isOdd(num) {
    return num % 2 !== 0;
}

const squareNumbers = (numbers) => {
    return numbers.map(num => num ** 2);
};

function isAnagram(s1, s2) {
    return s1.split('').sort().join('') === s2.split('').sort().join('');
}

function sumOfList(numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
}

function averageOfList(numbers) {
    if (numbers.length) {
        return numbers.reduce((a, b) => a + b, 0) / numbers.length;
    }
    return "List is empty";
}

function generateMultiplicationTable(number, limit) {
    return Array.from({ length: limit }, (_, i) => number * (i + 1));
}

function reverseList(lst) {
    return [...lst].reverse();
}

function capitalizeWords(s) {
    return s.split(" ").map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ");
}

function findUniqueElements(lst) {
    return Array.from(new Set(lst));
}

function flattenNestedList(nestedList) {
    return nestedList.reduce((flat, sublist) => flat.concat(sublist), []);
}

function countOccurrences(arr, value) {
    return arr.filter(element => element === value).length;
}

function getUniqueVowels(s) {
    return new Set([...s.toLowerCase()].filter(char => "aeiou".includes(char)));
}

function calculateSpeed(distance, time) {
    if (time <= 0) {
        return "Time must be positive";
    }
    return distance / time;
}

function multiplyList(numbers, multiplier) {
    return numbers.map(num => num * multiplier);
}

function findSecondLargest(numbers) {
    if (numbers.length < 2) {
        return "List must contain at least two elements";
    }
    const uniqueNumbers = [...new Set(numbers)];
    uniqueNumbers.sort((a, b) => b - a);
    return uniqueNumbers[1];
}