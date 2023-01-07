// for every HTML rendered browser creates DOM
// DOM ( Document Object Model ) is tree of HTML tags 
// getElementById can be implemented by using BFS or DFS 

console.log(document.children[0]); //root element
function getMyElementById(node,candidateId){
    if (node.id === candidateId)return node;
    let arr = [];
    let explored = new Set();
    arr.push(node);

    explored.add(node);

    while (arr.length > 0){
        let temp = arr.shift();
        if (temp.id === candidateId) return temp;
        Array.from(temp.children).filter((n) => !explored.has(n)).forEach((n) => {explored.add(n);arr.push(n);}); 
    }
}
console.log(getMyElementById(document.children[0],"test")); //getElementById("test")