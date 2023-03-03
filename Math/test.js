// function func(arr) {
//     let n = arr.length;
//     let count = 0;
//     for (let i = 0; i < n; i++)
//         if(arr[i] !== 0)
//             arr[count++] = arr[i];
//
//     while (count < n)
//         arr[count++] = 0
//
//     return arr
//
// }
//
// console.log(func([1,2,4, 6, 0,0,2,1,3,0]))

// process.on('exit', function (code) {
//     console.log(code);
//     process.exit(0)
// })
// console.log("code rinning")
// throw new Error("Existing code")
// process.exit(0)
{
    console.time("loop");
    for(var i =0 ; i<1000000; i+=1){

    }
    console.timeEnd("loop")
}
// How would you kill your server or Node.js code in case of a fatal exception without affecting other async tasks?