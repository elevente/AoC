const input = `zs-WO
zs-QJ
WO-zt
zs-DP
WO-end
gv-zt
iu-SK
HW-zs
iu-WO
gv-WO
gv-start
gv-DP
start-WO
HW-zt
iu-HW
gv-HW
zs-SK
HW-end
zs-end
DP-by
DP-iu
zt-start`;

// let allPaths = [];
let allPaths = 0;

function getAllPaths(u, d, isVisited, localPathList) {
	if (u == (d)) {
		// allPaths.push([...localPathList]);
		allPaths++;
		console.log(allPaths);
		return;
	}

	// Mark the current node
	if (u != u.toUpperCase()) {
		isVisited[u] = true;
	}

	const lowerCaseList = localPathList.filter(l => l != l.toUpperCase() && l != "start" && l != "end");
	const canVisitAgain = new Set(lowerCaseList).size === lowerCaseList.length;

	// Recur for all the vertices
	// adjacent to current vertex
	for (let i = 0; i < adjList[u].length; i++) {
		if ((!isVisited[adjList[u][i]] || canVisitAgain) && adjList[u][i] != localPathList[localPathList.length - 1]) {
			getAllPaths(adjList[u][i], d, isVisited, [...localPathList, adjList[u][i]]);
		}
	}

	// Mark the current node
	isVisited[u] = localPathList.filter(l => l != l.toUpperCase() && l == u).length > 1 ? true : false;
}

let adjList = [];
let isVisited = [];
input.split("\n").forEach(i => {
	if (!adjList[i.split("-")[0]]) adjList[i.split("-")[0]] = [];
	adjList[i.split("-")[0]].push(i.split("-")[1]);
	if (!adjList[i.split("-")[1]]) adjList[i.split("-")[1]] = [];
	adjList[i.split("-")[1]].push(i.split("-")[0]);
	isVisited[i.split("-")[0]] = false;
	isVisited[i.split("-")[1]] = false;
});

console.log(adjList);

const vertices = Object.keys(adjList).length;

let pathList = [];
pathList.push("start");

getAllPaths("start", "end", isVisited, pathList);
console.log("end");
console.log(allPaths);