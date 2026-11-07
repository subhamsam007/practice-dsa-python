const prompt = require("prompt-sync")({ sigint: true });

// how to asingn an array size  and add the element of the array in a variable 

// let size=Number(prompt("write the size of the array"))
// let arr= new Array(size)
// let sum= 0

// for (let i=0;i<arr.length;i++){
//     arr[i] = Number(prompt("enter the elements of array"))
//     sum+=arr[i]

// }
// console.log(arr)
// console.log(sum)





// ------------------------------------------------------------
// find max element in the array 

// let arr=[12,45,45,78,46,974,654,65,57,5,7];
// max=arr[0];

// for(let i= 1;i<arr.length;i++){
//     if (arr[i]>max){
//         max=arr[i]
//     }
//  };
//  console.log(max)

// //  find the min element of the array
// let ar=[12,45,45,78,46,974,654,65,57,5,7];
// min=ar[0]
// for(let i=1;i<ar.length;i++){
//     if(ar[i]<min){
//         min=ar[i]
//     }
// };
// console.log(min);

// ----------------------------------------------------------------
// calculate the sum and the mean of  array elements
let arr=[10, 49, 4, 69, 20]
total=0
for(let i=0;i<arr.length;i++){
    total+=arr[i]
}
console.log(total)
let mean =total/arr.length
console.log(mean)

//min element in an array 
let min =arr[0]
for (let i=0;i<arr.length;i++){
    if (min>arr[i]){
        min=arr[i]
    }
}
console.log(min)