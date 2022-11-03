const  twoSum=(arr,sum)=>{
const obj={}
for (var f=0; f<=arr.length-1; f++){ 
if(Object.keys(obj).map(n=>parseInt(n)).includes(sum-arr[f])){
return [arr[f],arr[obj[sum-arr[f]]]]
}
obj[arr[f]]=f
}
return []
}
console.log(twoSum([3,5,-4,12,11,1,-1,6],18))